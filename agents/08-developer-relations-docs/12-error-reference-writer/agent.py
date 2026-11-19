"""Error Reference Writer (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def write_error_reference(raw_input: str) -> str:
    """Domain-specific deterministic transform for Error Reference Writer."""
    cleaned = raw_input.strip()
    return f"[write_error_reference] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("error_catalog", ""))
    processed = write_error_reference(value)
    return {
        "agent_id": "12-error-reference-writer",
        "role": "Developer Relations & Docs",
        "tool_used": "write_error_reference",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "error_reference": processed,
        "confidence": 0.96,
    }
