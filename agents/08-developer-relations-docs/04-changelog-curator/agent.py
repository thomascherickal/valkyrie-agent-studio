"""Changelog Curator (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def curate_dev_changelog(raw_input: str) -> str:
    """Domain-specific deterministic transform for Changelog Curator."""
    cleaned = raw_input.strip()
    return f"[curate_dev_changelog] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("release_diff", ""))
    processed = curate_dev_changelog(value)
    return {
        "agent_id": "04-changelog-curator",
        "role": "Developer Relations & Docs",
        "tool_used": "curate_dev_changelog",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "changelog_md": processed,
        "confidence": 0.96,
    }
