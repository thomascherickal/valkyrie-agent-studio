"""Sandboxed Python execution & custom agent script runner.

ponytail: this sandbox catches mistakes in your own code (blocked imports, runaway loops). It is NOT a
security boundary: deliberate code can escape it, and it runs with the API's own permissions.
"""

from __future__ import annotations

import builtins
from dataclasses import dataclass
import json
import math
import re
import sys
import time
from types import ModuleType, SimpleNamespace
import typing
from typing import Any, Callable

FORBIDDEN_TOKENS = ("import os", "import subprocess", "open(", "__import__", "eval(", "exec(")
TIME_LIMIT_S = 5.0
_FILENAME = "<valkyrie-sandbox>"
_MODULES: dict[str, ModuleType] = {"typing": typing, "re": re, "json": json, "math": math}

# Pure helpers only: nothing that opens files, reaches the network, or inspects objects (no getattr, type, vars).
_BUILTINS: dict[str, Any] = {
    name: getattr(builtins, name)
    for name in (
        "len str int float bool list dict set tuple min max sum sorted enumerate range zip reversed map filter "
        "any all abs round divmod pow isinstance ord chr repr "
        "Exception ValueError KeyError IndexError TypeError AttributeError ZeroDivisionError"
    ).split()
}


@dataclass(frozen=True)
class SandboxResult:
    """Result of executing a custom Python hook in the sandbox."""

    ok: bool
    output: dict[str, Any]
    latency_ms: float
    error: str | None = None
    line: int | None = None


class SandboxTimeout(BaseException):
    """Raised inside user code that runs past the time limit. A BaseException so `except Exception` cannot hide it."""


def _public(module: ModuleType) -> SimpleNamespace:
    """A namespace of the module's public names, without submodules, so `typing.sys` or `re.enum` are unreachable."""
    names = getattr(module, "__all__", None) or dir(module)
    values = {n: getattr(module, n) for n in names if not n.startswith("_")}
    return SimpleNamespace(**{n: v for n, v in values.items() if not isinstance(v, ModuleType)})


def _sandbox_import(name: str, globals: Any = None, locals: Any = None, fromlist: Any = (), level: int = 0) -> Any:
    """Allow `typing`, `re`, `json` and `math`, as namespaces of their public names. Nothing else."""
    if level == 0 and name in _MODULES:
        return _public(_MODULES[name])
    raise ImportError(f"Import of {name!r} is not allowed in the sandbox (only typing, re, json, math)")


def validate_python_source(source: str) -> None:
    """Reject unsafe constructs before sandboxed execution."""
    for token in FORBIDDEN_TOKENS:
        if token in source:
            raise ValueError(f"Forbidden construct in custom Python: {token}")


def _line_of(exc: BaseException) -> int | None:
    """The line in the user's code where the error happened, if there is one."""
    if isinstance(exc, SyntaxError):
        return exc.lineno
    line = None
    tb = exc.__traceback__
    while tb is not None:
        if tb.tb_frame.f_code.co_filename == _FILENAME:
            line = tb.tb_lineno
        tb = tb.tb_next
    return line


def _describe(exc: BaseException, line: int | None) -> str:
    text = exc.msg if isinstance(exc, SyntaxError) else str(exc)
    where = f" (line {line})" if line else ""
    return f"{type(exc).__name__}: {text}{where}"


def _model_call(model: Callable[[str], str | None] | None, deadline: list[float]) -> Callable[[str], str | None]:
    """The `model(prompt)` the sandbox sees: text or None. A slow call does not eat the code's time limit."""

    def call(prompt: str) -> str | None:
        started = time.perf_counter()
        try:
            text = model(str(prompt)) if model else None
        except Exception:  # noqa: BLE001  ponytail: a failed call is "no answer", so Hybrid falls back to its draft
            text = None
        deadline[0] += time.perf_counter() - started
        return text if isinstance(text, str) and text.strip() else None

    return call


def _deadline_tracer(deadline: list[float]) -> Any:
    """Stop code that runs past the deadline (a one-item list so model calls can extend it). Replaces any tracer."""

    def tracer(frame: Any, event: str, arg: Any) -> Any:
        if event == "call" and frame.f_code.co_filename != _FILENAME:
            return None  # helper code (like the model call) is not the user's loop, so it is not timed
        if time.perf_counter() > deadline[0]:
            raise SandboxTimeout("The code ran past the time limit")
        return tracer

    return tracer


def run_custom_python(
    source: str,
    payload: dict[str, Any],
    time_limit: float = TIME_LIMIT_S,
    model: Callable[[str], str | None] | None = None,
) -> SandboxResult:
    """Execute custom Python `run_agent(payload)` in a restricted namespace, with a time limit.

    The code can call `model(prompt)`: it returns the model's text, or None when there is no model or no key.
    """
    start = time.perf_counter()
    previous_trace = sys.gettrace()
    try:
        validate_python_source(source)
        deadline = [time.perf_counter() + time_limit]
        builtins = {**_BUILTINS, "__import__": _sandbox_import, "__build_class__": __build_class__, "model": _model_call(model, deadline)}
        namespace: dict[str, Any] = {"__builtins__": builtins, "__name__": "agent"}
        code = compile(source, _FILENAME, "exec")
        sys.settrace(_deadline_tracer(deadline))
        exec(code, namespace, namespace)
        fn = namespace.get("run_agent")
        if not callable(fn):
            raise ValueError("Custom Python must define a callable `run_agent(payload)` function")
        result = fn(payload)
        sys.settrace(previous_trace)
        if not isinstance(result, dict):
            raise ValueError("`run_agent(payload)` must return a dict")
        elapsed = (time.perf_counter() - start) * 1000.0
        return SandboxResult(ok=True, output=result, latency_ms=round(elapsed, 3))
    except (Exception, SandboxTimeout) as exc:  # noqa: BLE001
        sys.settrace(previous_trace)
        elapsed = (time.perf_counter() - start) * 1000.0
        line = _line_of(exc)
        return SandboxResult(ok=False, output={}, latency_ms=round(elapsed, 3), error=_describe(exc, line), line=line)
