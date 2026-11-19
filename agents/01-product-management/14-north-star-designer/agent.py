"""North Star Metric Designer (Product Management) — focused Python execution module."""

from typing import Any


def define_north_star(raw_input: str) -> str:
    """Domain-specific deterministic transform for North Star Metric Designer."""
    cleaned = raw_input.strip()
    return f"[define_north_star] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("product_goals", ""))
    processed = define_north_star(value)
    return {
        "agent_id": "14-north-star-designer",
        "role": "Product Management",
        "tool_used": "define_north_star",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "metric_tree": processed,
        "confidence": 0.96,
    }
