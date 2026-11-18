"""Budget Alert Router (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def route_budget_warning(raw_input: str) -> str:
    """Domain-specific deterministic transform for Budget Alert Router."""
    cleaned = raw_input.strip()
    return f"[route_budget_warning] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("budget_status", ""))
    processed = route_budget_warning(value)
    return {
        "agent_id": "09-budget-alert-router",
        "role": "FinOps & Cloud Cost",
        "tool_used": "route_budget_warning",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "alert_payload": processed,
        "confidence": 0.96,
    }
