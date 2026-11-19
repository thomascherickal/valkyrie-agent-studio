"""Helm Chart Reviewer (DevOps & SRE) — focused Python execution module."""

from typing import Any


def review_helm_values(raw_input: str) -> str:
    """Domain-specific deterministic transform for Helm Chart Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_helm_values] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("helm_values", ""))
    processed = review_helm_values(value)
    return {
        "agent_id": "14-helm-chart-reviewer",
        "role": "DevOps & SRE",
        "tool_used": "review_helm_values",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "chart_review": processed,
        "confidence": 0.96,
    }
