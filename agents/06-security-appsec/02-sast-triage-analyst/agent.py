"""SAST Triage Analyst (Security & AppSec) — focused Python execution module."""

from typing import Any


def assess_reachability(raw_input: str) -> str:
    """Domain-specific deterministic transform for SAST Triage Analyst."""
    cleaned = raw_input.strip()
    return f"[assess_reachability] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("sast_finding", ""))
    processed = assess_reachability(value)
    return {
        "agent_id": "02-sast-triage-analyst",
        "role": "Security & AppSec",
        "tool_used": "assess_reachability",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "triage_verdict": processed,
        "confidence": 0.96,
    }
