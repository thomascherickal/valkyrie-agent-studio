"""Architecture Reviewer (Software Engineering) — focused Python execution module."""

from typing import Any


def check_failure_modes(raw_input: str) -> str:
    """Domain-specific deterministic transform for Architecture Reviewer."""
    cleaned = raw_input.strip()
    return f"[check_failure_modes] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("rfc_summary", ""))
    processed = check_failure_modes(value)
    return {
        "agent_id": "01-architecture-reviewer",
        "role": "Software Engineering",
        "tool_used": "check_failure_modes",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "review_findings": processed,
        "confidence": 0.96,
    }
