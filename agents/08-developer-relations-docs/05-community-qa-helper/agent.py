"""Community Q&A Helper (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def compose_community_reply(raw_input: str) -> str:
    """Domain-specific deterministic transform for Community Q&A Helper."""
    cleaned = raw_input.strip()
    return f"[compose_community_reply] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("question_text", ""))
    processed = compose_community_reply(value)
    return {
        "agent_id": "05-community-qa-helper",
        "role": "Developer Relations & Docs",
        "tool_used": "compose_community_reply",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "reply_md": processed,
        "confidence": 0.96,
    }
