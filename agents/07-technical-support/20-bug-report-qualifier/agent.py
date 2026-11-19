"""Bug Report Qualifier (Technical Support) — focused Python execution module."""

from typing import Any


def qualify_bug_report(raw_input: str) -> str:
    """Domain-specific deterministic transform for Bug Report Qualifier."""
    cleaned = raw_input.strip()
    return f"[qualify_bug_report] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("customer_report", ""))
    processed = qualify_bug_report(value)
    return {
        "agent_id": "20-bug-report-qualifier",
        "role": "Technical Support",
        "tool_used": "qualify_bug_report",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "qualified_bug": processed,
        "confidence": 0.96,
    }
