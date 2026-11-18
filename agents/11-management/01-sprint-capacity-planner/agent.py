"""Sprint Capacity Planner (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def calc_net_capacity(raw_input: str) -> str:
    """Domain-specific deterministic transform for Sprint Capacity Planner."""
    cleaned = raw_input.strip()
    return f"[calc_net_capacity] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("team_roster", ""))
    processed = calc_net_capacity(value)
    return {
        "agent_id": "01-sprint-capacity-planner",
        "role": "Engineering & Product Management",
        "tool_used": "calc_net_capacity",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "sprint_target": processed,
        "confidence": 0.96,
    }
