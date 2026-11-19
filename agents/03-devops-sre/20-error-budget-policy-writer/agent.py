"""Error Budget Policy Writer (DevOps & SRE) — focused Python execution module."""

from typing import Any


def draft_budget_policy(raw_input: str) -> str:
    """Domain-specific deterministic transform for Error Budget Policy Writer."""
    cleaned = raw_input.strip()
    return f"[draft_budget_policy] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("slo_context", ""))
    processed = draft_budget_policy(value)
    return {
        "agent_id": "20-error-budget-policy-writer",
        "role": "DevOps & SRE",
        "tool_used": "draft_budget_policy",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "budget_policy": processed,
        "confidence": 0.96,
    }
