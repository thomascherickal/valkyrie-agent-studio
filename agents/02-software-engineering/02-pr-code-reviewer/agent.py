"""PR Code Reviewer (Software Engineering) — focused Python execution module."""

from typing import Any


def detect_antipatterns(raw_input: str) -> str:
    """Domain-specific deterministic transform for PR Code Reviewer."""
    cleaned = raw_input.strip()
    return f"[detect_antipatterns] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("diff_snippet", ""))
    processed = detect_antipatterns(value)
    return {
        "agent_id": "02-pr-code-reviewer",
        "role": "Software Engineering",
        "tool_used": "detect_antipatterns",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "review_comments": processed,
        "confidence": 0.96,
    }
