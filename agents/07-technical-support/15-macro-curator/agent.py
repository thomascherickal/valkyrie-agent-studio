"""Support Macro Curator (Technical Support) — focused Python execution module."""

from typing import Any


def curate_macros(raw_input: str) -> str:
    """Domain-specific deterministic transform for Support Macro Curator."""
    cleaned = raw_input.strip()
    return f"[curate_macros] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("macro_usage", ""))
    processed = curate_macros(value)
    return {
        "agent_id": "15-macro-curator",
        "role": "Technical Support",
        "tool_used": "curate_macros",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "macro_plan": processed,
        "confidence": 0.96,
    }
