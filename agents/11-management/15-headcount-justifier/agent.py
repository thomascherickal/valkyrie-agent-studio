"""Headcount Justifier (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def justify_headcount(raw_input: str) -> str:
    """Domain-specific deterministic transform for Headcount Justifier."""
    cleaned = raw_input.strip()
    return f"[justify_headcount] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("workload_data", ""))
    processed = justify_headcount(value)
    return {
        "agent_id": "15-headcount-justifier",
        "role": "Engineering & Product Management",
        "tool_used": "justify_headcount",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "headcount_case": processed,
        "confidence": 0.96,
    }
