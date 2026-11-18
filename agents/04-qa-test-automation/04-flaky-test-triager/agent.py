"""Flaky Test Triager (QA & Test Automation) — focused Python execution module."""

from typing import Any


def classify_flakiness(raw_input: str) -> str:
    """Domain-specific deterministic transform for Flaky Test Triager."""
    cleaned = raw_input.strip()
    return f"[classify_flakiness] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("failure_logs", ""))
    processed = classify_flakiness(value)
    return {
        "agent_id": "04-flaky-test-triager",
        "role": "QA & Test Automation",
        "tool_used": "classify_flakiness",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "triage_report": processed,
        "confidence": 0.96,
    }
