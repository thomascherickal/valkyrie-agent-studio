"""Feedback Writer (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def write_feedback(raw_input: str) -> str:
    """Domain-specific deterministic transform for Feedback Writer."""
    cleaned = raw_input.strip()
    return f"[write_feedback] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("observed_behavior", ""))
    processed = write_feedback(value)
    return {
        "agent_id": "20-feedback-writer",
        "role": "Engineering & Product Management",
        "tool_used": "write_feedback",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "feedback_draft": processed,
        "confidence": 0.96,
    }
