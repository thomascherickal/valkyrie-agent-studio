"""Perf Review Synthesizer (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def synthesize_feedback(raw_input: str) -> str:
    """Domain-specific deterministic transform for Perf Review Synthesizer."""
    cleaned = raw_input.strip()
    return f"[synthesize_feedback] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("feedback_notes", ""))
    processed = synthesize_feedback(value)
    return {
        "agent_id": "05-perf-review-synthesizer",
        "role": "Engineering & Product Management",
        "tool_used": "synthesize_feedback",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "review_draft": processed,
        "confidence": 0.96,
    }
