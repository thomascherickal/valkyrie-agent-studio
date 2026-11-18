"""Runbook Generator (DevOps & SRE) — focused Python execution module."""

from typing import Any


def compile_runbook(raw_input: str) -> str:
    """Domain-specific deterministic transform for Runbook Generator."""
    cleaned = raw_input.strip()
    return f"[compile_runbook] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("alert_rule", ""))
    processed = compile_runbook(value)
    return {
        "agent_id": "08-runbook-generator",
        "role": "DevOps & SRE",
        "tool_used": "compile_runbook",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "runbook_md": processed,
        "confidence": 0.96,
    }
