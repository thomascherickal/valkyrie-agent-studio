"""Sandboxed Python execution & custom agent script runner."""

from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Any


FORBIDDEN_TOKENS = ("import os", "import subprocess", "open(", "__import__", "eval(", "exec(")


@dataclass(frozen=True)
class SandboxResult:
    """Result of executing a custom Python hook in the sandbox."""

    ok: bool
    output: dict[str, Any]
    latency_ms: float
    error: str | None = None


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

