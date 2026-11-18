"""KB Article Drafter (Technical Support) — focused Python execution module."""

from typing import Any


def format_kb_markdown(raw_input: str) -> str:
    """Domain-specific deterministic transform for KB Article Drafter."""
    cleaned = raw_input.strip()
    return f"[format_kb_markdown] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("resolution_notes", ""))
    processed = format_kb_markdown(value)
    return {
        "agent_id": "04-kb-article-drafter",
        "role": "Technical Support",
        "tool_used": "format_kb_markdown",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "kb_article": processed,
        "confidence": 0.96,
    }
