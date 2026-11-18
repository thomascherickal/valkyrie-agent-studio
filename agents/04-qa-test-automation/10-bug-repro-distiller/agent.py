"""Bug Repro Distiller (QA & Test Automation) — focused Python execution module."""

from typing import Any


def distill_min_repro(raw_input: str) -> str:
    """Domain-specific deterministic transform for Bug Repro Distiller."""
    cleaned = raw_input.strip()
    return f"[distill_min_repro] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("bug_thread", ""))
    processed = distill_min_repro(value)
    return {
        "agent_id": "10-bug-repro-distiller",
        "role": "QA & Test Automation",
        "tool_used": "distill_min_repro",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "repro_steps": processed,
        "confidence": 0.96,
    }
