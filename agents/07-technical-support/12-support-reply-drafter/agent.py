"""Customer Reply Drafter (Technical Support) — focused Python execution module."""

from typing import Any


def draft_support_reply(raw_input: str) -> str:
    """Domain-specific deterministic transform for Customer Reply Drafter."""
    cleaned = raw_input.strip()
    return f"[draft_support_reply] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("ticket_thread", ""))
    processed = draft_support_reply(value)
    return {
        "agent_id": "12-support-reply-drafter",
        "role": "Technical Support",
        "tool_used": "draft_support_reply",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "reply_draft": processed,
        "confidence": 0.96,
    }
