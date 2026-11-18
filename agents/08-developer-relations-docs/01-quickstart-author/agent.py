"""Quickstart Author (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def structure_quickstart(raw_input: str) -> str:
    """Domain-specific deterministic transform for Quickstart Author."""
    cleaned = raw_input.strip()
    return f"[structure_quickstart] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("feature_name", ""))
    processed = structure_quickstart(value)
    return {
        "agent_id": "01-quickstart-author",
        "role": "Developer Relations & Docs",
        "tool_used": "structure_quickstart",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "quickstart_md": processed,
        "confidence": 0.96,
    }
