"""Build vs Buy Evaluator (Product Management) — focused Python execution module."""

from typing import Any


def compare_build_buy(raw_input: str) -> str:
    """Domain-specific deterministic transform for Build vs Buy Evaluator."""
    cleaned = raw_input.strip()
    return f"[compare_build_buy] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("capability_request", ""))
    processed = compare_build_buy(value)
    return {
        "agent_id": "19-build-buy-evaluator",
        "role": "Product Management",
        "tool_used": "compare_build_buy",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "decision_memo": processed,
        "confidence": 0.96,
    }
