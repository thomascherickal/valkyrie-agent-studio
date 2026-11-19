"""Migration Guide Writer (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def write_migration_guide(raw_input: str) -> str:
    """Domain-specific deterministic transform for Migration Guide Writer."""
    cleaned = raw_input.strip()
    return f"[write_migration_guide] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("breaking_changes", ""))
    processed = write_migration_guide(value)
    return {
        "agent_id": "11-migration-guide-writer",
        "role": "Developer Relations & Docs",
        "tool_used": "write_migration_guide",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "migration_guide": processed,
        "confidence": 0.96,
    }
