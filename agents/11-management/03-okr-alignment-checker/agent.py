"""OKR Alignment Checker (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def score_okr_fit(raw_input: str) -> str:
    """Domain-specific deterministic transform for OKR Alignment Checker."""
    cleaned = raw_input.strip()
    return f"[score_okr_fit] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("epics_vs_okrs", ""))
    processed = score_okr_fit(value)
    return {
        "agent_id": "03-okr-alignment-checker",
        "role": "Engineering & Product Management",
        "tool_used": "score_okr_fit",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "alignment_report": processed,
        "confidence": 0.96,
    }
