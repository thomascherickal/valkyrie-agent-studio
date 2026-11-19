"""Exploratory Charter Writer (QA & Test Automation) — focused Python execution module."""

from typing import Any


def write_charters(raw_input: str) -> str:
    """Domain-specific deterministic transform for Exploratory Charter Writer."""
    cleaned = raw_input.strip()
    return f"[write_charters] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("feature_summary", ""))
    processed = write_charters(value)
    return {
        "agent_id": "17-exploratory-charter-writer",
        "role": "QA & Test Automation",
        "tool_used": "write_charters",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "session_charters": processed,
        "confidence": 0.96,
    }
