"""Docs Information Architecture Reviewer (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def review_docs_ia(raw_input: str) -> str:
    """Domain-specific deterministic transform for Docs Information Architecture Reviewer."""
    cleaned = raw_input.strip()
    return f"[review_docs_ia] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("site_map", ""))
    processed = review_docs_ia(value)
    return {
        "agent_id": "14-docs-ia-reviewer",
        "role": "Developer Relations & Docs",
        "tool_used": "review_docs_ia",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "ia_review": processed,
        "confidence": 0.96,
    }
