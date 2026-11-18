"""Hiring Rubric Builder (Engineering & Product Management) — focused Python execution module."""

from typing import Any


def build_rubric_grid(raw_input: str) -> str:
    """Domain-specific deterministic transform for Hiring Rubric Builder."""
    cleaned = raw_input.strip()
    return f"[build_rubric_grid] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("role_level", ""))
    processed = build_rubric_grid(value)
    return {
        "agent_id": "04-hiring-rubric-builder",
        "role": "Engineering & Product Management",
        "tool_used": "build_rubric_grid",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "rubric_md": processed,
        "confidence": 0.96,
    }
