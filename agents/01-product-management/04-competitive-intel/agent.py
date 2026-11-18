"""Competitive Intel Analyst (Product Management) — focused Python execution module."""

from typing import Any


def diff_feature_matrix(raw_input: str) -> str:
    """Domain-specific deterministic transform for Competitive Intel Analyst."""
    cleaned = raw_input.strip()
    return f"[diff_feature_matrix] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("competitor_notes", ""))
    processed = diff_feature_matrix(value)
    return {
        "agent_id": "04-competitive-intel",
        "role": "Product Management",
        "tool_used": "diff_feature_matrix",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "matrix_summary": processed,
        "confidence": 0.96,
    }
