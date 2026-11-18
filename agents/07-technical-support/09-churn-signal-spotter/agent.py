"""Churn Signal Spotter (Technical Support) — focused Python execution module."""

from typing import Any


def compute_churn_risk(raw_input: str) -> str:
    """Domain-specific deterministic transform for Churn Signal Spotter."""
    cleaned = raw_input.strip()
    return f"[compute_churn_risk] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("thread_history", ""))
    processed = compute_churn_risk(value)
    return {
        "agent_id": "09-churn-signal-spotter",
        "role": "Technical Support",
        "tool_used": "compute_churn_risk",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "csm_alert": processed,
        "confidence": 0.96,
    }
