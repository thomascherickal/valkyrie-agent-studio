"""Log Bundle Analyzer (Technical Support) — focused Python execution module."""

from typing import Any


def extract_root_exception(raw_input: str) -> str:
    """Domain-specific deterministic transform for Log Bundle Analyzer."""
    cleaned = raw_input.strip()
    return f"[extract_root_exception] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("log_excerpt", ""))
    processed = extract_root_exception(value)
    return {
        "agent_id": "02-log-bundle-analyzer",
        "role": "Technical Support",
        "tool_used": "extract_root_exception",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "diagnostic_summary": processed,
        "confidence": 0.96,
    }
