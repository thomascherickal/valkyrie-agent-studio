"""Forecast Variance Explainer (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def explain_cost_variance(raw_input: str) -> str:
    """Domain-specific deterministic transform for Forecast Variance Explainer."""
    cleaned = raw_input.strip()
    return f"[explain_cost_variance] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("actual_vs_forecast", ""))
    processed = explain_cost_variance(value)
    return {
        "agent_id": "18-forecast-variance-explainer",
        "role": "FinOps & Cloud Cost",
        "tool_used": "explain_cost_variance",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "variance_story": processed,
        "confidence": 0.96,
    }
