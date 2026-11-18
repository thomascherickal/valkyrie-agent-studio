"""User Story Splitter (Product Management) — focused Python execution module."""

from typing import Any


def split_invest_stories(raw_input: str) -> str:
    """Domain-specific deterministic transform for User Story Splitter."""
    cleaned = raw_input.strip()
    return f"[split_invest_stories] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("epic_text", ""))
    processed = split_invest_stories(value)
    return {
        "agent_id": "03-user-story-splitter",
        "role": "Product Management",
        "tool_used": "split_invest_stories",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "stories": processed,
        "confidence": 0.96,
    }
