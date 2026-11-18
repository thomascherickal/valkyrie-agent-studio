"""Experiment Designer (Product Management) — focused Python execution module."""

from typing import Any


def calc_ab_sample_size(raw_input: str) -> str:
    """Domain-specific deterministic transform for Experiment Designer."""
    cleaned = raw_input.strip()
    return f"[calc_ab_sample_size] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("hypothesis", ""))
    processed = calc_ab_sample_size(value)
    return {
        "agent_id": "08-experiment-designer",
        "role": "Product Management",
        "tool_used": "calc_ab_sample_size",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "experiment_spec": processed,
        "confidence": 0.96,
    }
