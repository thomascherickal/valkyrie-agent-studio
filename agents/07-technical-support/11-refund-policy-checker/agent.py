"""Refund Policy Checker (Technical Support) — focused Python execution module."""

from typing import Any


def check_refund_policy(raw_input: str) -> str:
    """Domain-specific deterministic transform for Refund Policy Checker."""
    cleaned = raw_input.strip()
    return f"[check_refund_policy] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("refund_request", ""))
    processed = check_refund_policy(value)
    return {
        "agent_id": "11-refund-policy-checker",
        "role": "Technical Support",
        "tool_used": "check_refund_policy",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "refund_decision": processed,
        "confidence": 0.96,
    }
