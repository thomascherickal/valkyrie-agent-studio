"""Codebase Onboarding Guide (Software Engineering) — focused Python execution module."""

from typing import Any


def write_onboarding_guide(raw_input: str) -> str:
    """Domain-specific deterministic transform for Codebase Onboarding Guide."""
    cleaned = raw_input.strip()
    return f"[write_onboarding_guide] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("repo_overview", ""))
    processed = write_onboarding_guide(value)
    return {
        "agent_id": "20-codebase-onboarding-guide",
        "role": "Software Engineering",
        "tool_used": "write_onboarding_guide",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "onboarding_guide": processed,
        "confidence": 0.96,
    }
