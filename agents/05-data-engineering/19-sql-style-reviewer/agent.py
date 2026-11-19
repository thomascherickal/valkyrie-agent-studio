"""SQL Style Reviewer (Data Engineering) — focused Python execution module."""

from typing import Any


def review_sql_style(raw_input: str) -> str:
    """Domain-specific deterministic transform for SQL Style Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_sql_style] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("sql_excerpt", ""))
    processed = review_sql_style(value)
    return {
        "agent_id": "19-sql-style-reviewer",
        "role": "Data Engineering",
        "tool_used": "review_sql_style",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "sql_review": processed,
        "confidence": 0.96,
    }
