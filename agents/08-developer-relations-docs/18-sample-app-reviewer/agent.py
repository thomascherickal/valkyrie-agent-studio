"""Sample App Reviewer (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def review_sample_app(raw_input: str) -> str:
    """Domain-specific deterministic transform for Sample App Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_sample_app] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("sample_readme", ""))
    processed = review_sample_app(value)
    return {
        "agent_id": "18-sample-app-reviewer",
        "role": "Developer Relations & Docs",
        "tool_used": "review_sample_app",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "sample_review": processed,
        "confidence": 0.96,
    }
