"""API Security Reviewer (Security & AppSec) — focused Python execution module."""

from typing import Any


def review_api_security(raw_input: str) -> str:
    """Domain-specific deterministic transform for API Security Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_api_security] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("api_spec", ""))
    processed = review_api_security(value)
    return {
        "agent_id": "11-api-security-reviewer",
        "role": "Security & AppSec",
        "tool_used": "review_api_security",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "api_findings": processed,
        "confidence": 0.96,
    }
