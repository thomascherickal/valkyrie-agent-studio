"""Release Notes Writer (Product Management) — focused Python execution module."""

from typing import Any


def format_changelog(raw_input: str) -> str:
    """Domain-specific deterministic transform for Release Notes Writer."""
    cleaned = raw_input.strip()
    return f"[format_changelog] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("pr_log", ""))
    processed = format_changelog(value)
    return {
        "agent_id": "09-release-notes-writer",
        "role": "Product Management",
        "tool_used": "format_changelog",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "release_notes": processed,
        "confidence": 0.96,
    }
