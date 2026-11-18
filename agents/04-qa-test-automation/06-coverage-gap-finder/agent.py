"""Coverage Gap Finder (QA & Test Automation) — focused Python execution module."""

from typing import Any


def propose_branch_tests(raw_input: str) -> str:
    """Domain-specific deterministic transform for Coverage Gap Finder."""
    cleaned = raw_input.strip()
    return f"[propose_branch_tests] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("coverage_report", ""))
    processed = propose_branch_tests(value)
    return {
        "agent_id": "06-coverage-gap-finder",
        "role": "QA & Test Automation",
        "tool_used": "propose_branch_tests",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "missing_tests": processed,
        "confidence": 0.96,
    }
