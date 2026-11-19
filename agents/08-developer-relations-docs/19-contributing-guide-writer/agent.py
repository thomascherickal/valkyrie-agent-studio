"""OSS Contribution Guide Writer (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def write_contributing_guide(raw_input: str) -> str:
    """Domain-specific deterministic transform for OSS Contribution Guide Writer."""
    cleaned = raw_input.strip()
    return f"[write_contributing_guide] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("project_facts", ""))
    processed = write_contributing_guide(value)
    return {
        "agent_id": "19-contributing-guide-writer",
        "role": "Developer Relations & Docs",
        "tool_used": "write_contributing_guide",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "contributing_guide": processed,
        "confidence": 0.96,
    }
