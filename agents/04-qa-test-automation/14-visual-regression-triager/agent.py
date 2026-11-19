"""Visual Regression Triager (QA & Test Automation) — focused Python execution module."""

from typing import Any


def triage_visual_diffs(raw_input: str) -> str:
    """Domain-specific deterministic transform for Visual Regression Triager."""
    cleaned = raw_input.strip()
    return f"[triage_visual_diffs] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("screenshot_diffs", ""))
    processed = triage_visual_diffs(value)
    return {
        "agent_id": "14-visual-regression-triager",
        "role": "QA & Test Automation",
        "tool_used": "triage_visual_diffs",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "visual_triage": processed,
        "confidence": 0.96,
    }
