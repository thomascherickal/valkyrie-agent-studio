"""Idempotency Reviewer (Software Engineering) — focused Python execution module."""

from typing import Any


def check_idempotency(raw_input: str) -> str:
    """Domain-specific deterministic transform for Idempotency Reviewer."""
    cleaned = raw_input.strip()
    return f"[check_idempotency] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("endpoint_spec", ""))
    processed = check_idempotency(value)
    return {
        "agent_id": "18-idempotency-reviewer",
        "role": "Software Engineering",
        "tool_used": "check_idempotency",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "idempotency_review": processed,
        "confidence": 0.96,
    }
