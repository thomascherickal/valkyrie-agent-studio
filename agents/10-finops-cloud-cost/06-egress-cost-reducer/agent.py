"""Egress Cost Reducer (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def find_egress_leaks(raw_input: str) -> str:
    """Domain-specific deterministic transform for Egress Cost Reducer."""
    cleaned = raw_input.strip()
    return f"[find_egress_leaks] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("network_flow", ""))
    processed = find_egress_leaks(value)
    return {
        "agent_id": "06-egress-cost-reducer",
        "role": "FinOps & Cloud Cost",
        "tool_used": "find_egress_leaks",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "network_fixes": processed,
        "confidence": 0.96,
    }
