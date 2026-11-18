"""Escalation Packager (Technical Support) — focused Python execution module."""

from typing import Any


def package_l3_handoff(raw_input: str) -> str:
    """Domain-specific deterministic transform for Escalation Packager."""
    cleaned = raw_input.strip()
    return f"[package_l3_handoff] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("case_notes", ""))
    processed = package_l3_handoff(value)
    return {
        "agent_id": "03-escalation-packager",
        "role": "Technical Support",
        "tool_used": "package_l3_handoff",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "escalation_card": processed,
        "confidence": 0.96,
    }
