"""Refactor Planner (Software Engineering) — focused Python execution module."""

from typing import Any


def plan_strangler_steps(raw_input: str) -> str:
    """Domain-specific deterministic transform for Refactor Planner."""
    cleaned = raw_input.strip()
    return f"[plan_strangler_steps] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("module_metrics", ""))
    processed = plan_strangler_steps(value)
    return {
        "agent_id": "03-refactor-planner",
        "role": "Software Engineering",
        "tool_used": "plan_strangler_steps",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "refactor_plan": processed,
        "confidence": 0.96,
    }
