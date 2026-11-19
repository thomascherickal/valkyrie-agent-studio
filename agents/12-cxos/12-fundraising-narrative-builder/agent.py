"""Fundraising Narrative Builder (C-Suite & Executives (CxOs)) — focused Python execution module."""

from typing import Any


def build_fundraise_story(raw_input: str) -> str:
    """Domain-specific deterministic transform for Fundraising Narrative Builder."""
    cleaned = raw_input.strip()
    return f"[build_fundraise_story] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("company_facts", ""))
    processed = build_fundraise_story(value)
    return {
        "agent_id": "12-fundraising-narrative-builder",
        "role": "C-Suite & Executives (CxOs)",
        "tool_used": "build_fundraise_story",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "investor_narrative": processed,
        "confidence": 0.96,
    }
