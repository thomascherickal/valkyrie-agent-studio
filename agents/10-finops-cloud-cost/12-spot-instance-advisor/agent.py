"""Spot Instance Advisor (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def assess_spot_fit(raw_input: str) -> str:
    """Domain-specific deterministic transform for Spot Instance Advisor."""
    cleaned = raw_input.strip()
    return f"[assess_spot_fit] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("workload_profile", ""))
    processed = assess_spot_fit(value)
    return {
        "agent_id": "12-spot-instance-advisor",
        "role": "FinOps & Cloud Cost",
        "tool_used": "assess_spot_fit",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "spot_plan": processed,
        "confidence": 0.96,
    }
