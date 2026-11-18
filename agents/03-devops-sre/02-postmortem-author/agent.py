"""Postmortem Author (DevOps & SRE) — focused Python execution module."""

from typing import Any


def generate_five_whys(raw_input: str) -> str:
    """Domain-specific deterministic transform for Postmortem Author."""
    cleaned = raw_input.strip()
    return f"[generate_five_whys] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("incident_log", ""))
    processed = generate_five_whys(value)
    return {
        "agent_id": "02-postmortem-author",
        "role": "DevOps & SRE",
        "tool_used": "generate_five_whys",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "postmortem_md": processed,
        "confidence": 0.96,
    }
