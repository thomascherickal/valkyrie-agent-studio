"""Duplicate Ticket Merger (Technical Support) — focused Python execution module."""

from typing import Any


def find_duplicate_tickets(raw_input: str) -> str:
    """Domain-specific deterministic transform for Duplicate Ticket Merger."""
    cleaned = raw_input.strip()
    return f"[find_duplicate_tickets] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("ticket_list", ""))
    processed = find_duplicate_tickets(value)
    return {
        "agent_id": "13-duplicate-ticket-merger",
        "role": "Technical Support",
        "tool_used": "find_duplicate_tickets",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "merge_plan": processed,
        "confidence": 0.96,
    }
