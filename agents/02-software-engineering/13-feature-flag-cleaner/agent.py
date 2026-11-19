"""Feature Flag Cleaner (Software Engineering) — focused Python execution module."""

from typing import Any


def find_stale_flags(raw_input: str) -> str:
    """Domain-specific deterministic transform for Feature Flag Cleaner."""
    cleaned = raw_input.strip()
    return f"[find_stale_flags] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("flag_inventory", ""))
    processed = find_stale_flags(value)
    return {
        "agent_id": "13-feature-flag-cleaner",
        "role": "Software Engineering",
        "tool_used": "find_stale_flags",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "cleanup_plan": processed,
        "confidence": 0.96,
    }
