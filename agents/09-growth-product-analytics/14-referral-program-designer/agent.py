"""Referral Program Designer (Growth & Product Analytics) — focused Python execution module."""

from typing import Any


def design_referral(raw_input: str) -> str:
    """Domain-specific deterministic transform for Referral Program Designer."""
    cleaned = raw_input.strip()
    return f"[design_referral] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("referral_brief", ""))
    processed = design_referral(value)
    return {
        "agent_id": "14-referral-program-designer",
        "role": "Growth & Product Analytics",
        "tool_used": "design_referral",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "referral_design": processed,
        "confidence": 0.96,
    }
