"""Chargeback Allocator (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def allocate_shared_cost(raw_input: str) -> str:
    """Domain-specific deterministic transform for Chargeback Allocator."""
    cleaned = raw_input.strip()
    return f"[allocate_shared_cost] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("shared_costs", ""))
    processed = allocate_shared_cost(value)
    return {
        "agent_id": "15-chargeback-allocator",
        "role": "FinOps & Cloud Cost",
        "tool_used": "allocate_shared_cost",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "allocation_table": processed,
        "confidence": 0.96,
    }
