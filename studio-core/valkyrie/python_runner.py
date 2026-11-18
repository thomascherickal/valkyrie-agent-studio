"""Sandboxed Python execution & custom agent script runner."""

from __future__ import annotations

from dataclasses import dataclass
from types import SimpleNamespace
import time
import typing
from typing import Any


FORBIDDEN_TOKENS = ("import os", "import subprocess", "open(", "__import__", "eval(", "exec(")


@dataclass(frozen=True)
class SandboxResult:
    """Result of executing a custom Python hook in the sandbox."""

    ok: bool
    output: dict[str, Any]
    latency_ms: float
    error: str | None = None


def _sandbox_import(name: str, globals: Any = None, locals: Any = None, fromlist: Any = (), level: int = 0) -> Any:
    """Allow `import typing` and nothing else.

    Returns a namespace of typing's public names rather than the module itself, so the module's own
    imports (`typing.sys`, and through it `sys.modules`) stay out of reach.
    ponytail: this sandbox catches mistakes in your own code; it is not a security boundary.
    """
    if name == "typing" and level == 0:
        return SimpleNamespace(**{n: getattr(typing, n) for n in typing.__all__})
    raise ImportError(f"Import of {name!r} is not allowed in the sandbox (only typing)")


def validate_python_source(source: str) -> None:
    """Reject unsafe constructs before sandboxed execution."""
    for token in FORBIDDEN_TOKENS:
        if token in source:
            raise ValueError(f"Forbidden construct in custom Python: {token}")


def run_custom_python(source: str, payload: dict[str, Any]) -> SandboxResult:
    """Execute custom Python `run_agent(payload)` in a restricted namespace."""
    start = time.perf_counter()
    try:
        validate_python_source(source)
        safe_builtins: dict[str, Any] = {
            "__import__": _sandbox_import,
            "len": len,
            "str": str,
            "int": int,
            "float": float,
            "bool": bool,
            "list": list,
            "dict": dict,
            "min": min,
            "max": max,
            "sum": sum,
            "sorted": sorted,
            "enumerate": enumerate,
        }
        namespace: dict[str, Any] = {"__builtins__": safe_builtins}
        exec(compile(source, "<valkyrie-sandbox>", "exec"), namespace, namespace)
        fn = namespace.get("run_agent")
        if not callable(fn):
            raise ValueError("Custom Python must define a callable `run_agent(payload)` function")
        result = fn(payload)
        if not isinstance(result, dict):
            raise ValueError("`run_agent(payload)` must return a dict")
        elapsed = (time.perf_counter() - start) * 1000.0
        return SandboxResult(ok=True, output=result, latency_ms=round(elapsed, 3))
    except Exception as exc:  # noqa: BLE001
        elapsed = (time.perf_counter() - start) * 1000.0
        return SandboxResult(ok=False, output={}, latency_ms=round(elapsed, 3), error=str(exc))

