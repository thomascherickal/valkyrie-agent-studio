"""Vendor Security Reviewer (Security & AppSec) — focused Python execution module."""

from typing import Any


def review_vendor_security(raw_input: str) -> str:
    """Domain-specific deterministic transform for Vendor Security Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_vendor_security] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("vendor_answers", ""))
    processed = review_vendor_security(value)
    return {
        "agent_id": "15-vendor-security-reviewer",
        "role": "Security & AppSec",
        "tool_used": "review_vendor_security",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "vendor_risk": processed,
        "confidence": 0.96,
    }
