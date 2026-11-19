"""Known Issue Matcher (Technical Support) — focused Python execution module."""

from typing import Any


def match_known_issues(raw_input: str) -> str:
    """Domain-specific deterministic transform for Known Issue Matcher."""
    cleaned = raw_input.strip()
    return f"[match_known_issues] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("symptom_report", ""))
    processed = match_known_issues(value)
    return {
        "agent_id": "17-known-issue-matcher",
        "role": "Technical Support",
        "tool_used": "match_known_issues",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "issue_match": processed,
        "confidence": 0.96,
    }
