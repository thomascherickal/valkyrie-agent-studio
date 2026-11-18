"""Ticket Triager (Technical Support) — focused Python execution module."""

from typing import Any


def classify_ticket_sla(raw_input: str) -> str:
    """Domain-specific deterministic transform for Ticket Triager."""
    cleaned = raw_input.strip()
    return f"[classify_ticket_sla] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("ticket_text", ""))
    processed = classify_ticket_sla(value)
    return {
        "agent_id": "01-ticket-triager",
        "role": "Technical Support",
        "tool_used": "classify_ticket_sla",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "routing_decision": processed,
        "confidence": 0.96,
    }
