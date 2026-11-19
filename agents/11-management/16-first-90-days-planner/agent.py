"""30-60-90 Day Planner (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def plan_first_quarter(raw_input: str) -> str:
    """Domain-specific deterministic transform for 30-60-90 Day Planner."""
    cleaned = raw_input.strip()
    return f"[plan_first_quarter] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("role_context", ""))
    processed = plan_first_quarter(value)
    return {
        "agent_id": "16-first-90-days-planner",
        "role": "Engineering & Product Management",
        "tool_used": "plan_first_quarter",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "onboarding_plan": processed,
        "confidence": 0.96,
    }
