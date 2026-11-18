"""Metric Layer Definer (Data Engineering) — focused Python execution module."""

from typing import Any


def define_semantic_metric(raw_input: str) -> str:
    """Domain-specific deterministic transform for Metric Layer Definer."""
    cleaned = raw_input.strip()
    return f"[define_semantic_metric] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("kpi_request", ""))
    processed = define_semantic_metric(value)
    return {
        "agent_id": "10-metric-layer-definer",
        "role": "Data Engineering",
        "tool_used": "define_semantic_metric",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "metric_yaml": processed,
        "confidence": 0.96,
    }
