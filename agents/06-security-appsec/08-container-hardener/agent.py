"""Container Hardener (Security & AppSec) — focused Python execution module."""

from typing import Any


def lint_dockerfile(raw_input: str) -> str:
    """Domain-specific deterministic transform for Container Hardener."""
    cleaned = raw_input.strip()
    return f"[lint_dockerfile] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("dockerfile_text", ""))
    processed = lint_dockerfile(value)
    return {
        "agent_id": "08-container-hardener",
        "role": "Security & AppSec",
        "tool_used": "lint_dockerfile",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "hardened_diff": processed,
        "confidence": 0.96,
    }
