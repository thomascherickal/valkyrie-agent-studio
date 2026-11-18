"""Security Advisory Writer (Security & AppSec) — focused Python execution module."""

from typing import Any


def format_advisory_md(raw_input: str) -> str:
    """Domain-specific deterministic transform for Security Advisory Writer."""
    cleaned = raw_input.strip()
    return f"[format_advisory_md] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("advisory_input", ""))
    processed = format_advisory_md(value)
    return {
        "agent_id": "10-security-advisory-writer",
        "role": "Security & AppSec",
        "tool_used": "format_advisory_md",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "advisory_doc": processed,
        "confidence": 0.96,
    }
