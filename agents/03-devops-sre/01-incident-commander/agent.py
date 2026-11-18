"""Incident Commander (DevOps & SRE) — focused Python execution module."""

from typing import Any


def build_ics_timeline(raw_input: str) -> str:
    """Domain-specific deterministic transform for Incident Commander."""
    cleaned = raw_input.strip()
    return f"[build_ics_timeline] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("alert_payload", ""))
    processed = build_ics_timeline(value)
    return {
        "agent_id": "01-incident-commander",
        "role": "DevOps & SRE",
        "tool_used": "build_ics_timeline",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "command_plan": processed,
        "confidence": 0.96,
    }
