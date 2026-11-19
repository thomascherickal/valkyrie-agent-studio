"""Step-by-step tracing. Every step of a run is kept in memory, appended to a JSONL log and streamed to the Command Centre.

Keys never reach a trace: values of the provider key variables and anything that looks like `key=...` or a bearer
token is replaced with `***` before an event is stored, logged or sent.
"""

from __future__ import annotations

from collections import deque
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timezone
import json
import logging
import os
import re
import threading
import time
from collections.abc import Iterator
from typing import Any
import uuid

from valkyrie.storage import logs_dir

MAX_EVENTS = 2000
MAX_TEXT = 4000
MAX_LOG_BYTES = 5_000_000
SECRET_VARS = ("GEMINI_API_KEY", "OPENROUTER_API_KEY", "OPENCODE_API_KEY")
_SECRET_SHAPES = re.compile(r"((?:key=|Bearer\s+)|(?:x-goog-api-key['\"]?\s*[:=]\s*['\"]?))[^&\s'\"]+", re.IGNORECASE)
log = logging.getLogger("valkyrie.trace")


def redact(value: Any) -> Any:
    """A copy of `value` with secrets hidden and long text cut to MAX_TEXT characters."""
    if isinstance(value, str):
        for name in SECRET_VARS:
            secret = os.environ.get(name)
            if secret and secret in value:
                value = value.replace(secret, "***")
        value = _SECRET_SHAPES.sub(r"\1***", value)
        return value if len(value) <= MAX_TEXT else f"{value[:MAX_TEXT]}… ({len(value)} characters)"
    if isinstance(value, dict):
        return {str(k): redact(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [redact(v) for v in value]
    if value is None or isinstance(value, (bool, int, float)):
        return value
    return redact(str(value))


class TraceStore:
    """The most recent events, newest last. Safe to use from several threads."""

    def __init__(self) -> None:
        self._events: deque[dict[str, Any]] = deque(maxlen=MAX_EVENTS)
        self._lock = threading.Lock()
        self._next = 1

    def add(self, run: str, agent: str, stage: str, message: str, status: str, ms: float, detail: dict[str, Any]) -> dict[str, Any]:
        with self._lock:
            event = {
                "id": self._next,
                "at": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                "run": run,
                "agent": agent,
                "stage": stage,
                "message": redact(message),
                "status": status,
                "ms": ms,
                "detail": detail,
            }
            self._next += 1
            self._events.append(event)
        _write_log(event)
        return event

    def since(self, after: int = 0, run: str | None = None) -> list[dict[str, Any]]:
        with self._lock:
            return [e for e in self._events if e["id"] > after and (run is None or e["run"] == run)]

    def clear(self) -> int:
        """Forget the events in memory. The log file on disk is kept."""
        with self._lock:
            count = len(self._events)
            self._events.clear()
            return count


def _write_log(event: dict[str, Any]) -> None:
    """Append one line to the JSONL log. A full disk or a read-only folder must never break a run."""
    try:
        path = logs_dir() / "trace.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and path.stat().st_size > MAX_LOG_BYTES:
            path.replace(path.with_suffix(".jsonl.1"))
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    except OSError as exc:
        log.warning("could not write the trace log: %s", exc)
    log.info("%s %s %s %s", event["run"], event["stage"], event["status"], event["message"])


STORE = TraceStore()


class Tracer:
    """Records the steps of one run. `ms` on each event is the time since the run started."""

    def __init__(self, agent: str, run: str | None = None) -> None:
        self.run = run or uuid.uuid4().hex[:8]
        self.agent = agent
        self.started = time.perf_counter()

    def step(self, stage: str, message: str, status: str = "info", /, **detail: Any) -> dict[str, Any]:
        elapsed = round((time.perf_counter() - self.started) * 1000, 1)
        return STORE.add(self.run, self.agent, stage, message, status, elapsed, redact(detail))


_CURRENT: ContextVar[Tracer | None] = ContextVar("valkyrie_tracer", default=None)


@contextmanager
def traced_run(agent: str) -> Iterator[Tracer]:
    """Everything traced inside this block belongs to one run."""
    tracer = Tracer(agent)
    token = _CURRENT.set(tracer)
    try:
        yield tracer
    finally:
        _CURRENT.reset(token)


def step(stage: str, message: str, status: str = "info", /, **detail: Any) -> dict[str, Any]:
    """Record a step in the current run, or under the run "system" when there is none (a button, not a run).

    The first three arguments are positional only, so a detail field may have any name (even stage, message or status).
    """
    return (_CURRENT.get() or Tracer("system", run="system")).step(stage, message, status, **detail)
