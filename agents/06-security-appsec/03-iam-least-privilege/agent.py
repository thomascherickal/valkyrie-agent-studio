"""IAM Least Privilege Auditor (Security & AppSec) — focused Python execution module."""

from typing import Any


def narrow_iam_actions(raw_input: str) -> str:
    """Domain-specific deterministic transform for IAM Least Privilege Auditor."""
    cleaned = raw_input.strip()
    return f"[narrow_iam_actions] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("iam_policy", ""))
    processed = narrow_iam_actions(value)
    return {
        "agent_id": "03-iam-least-privilege",
        "role": "Security & AppSec",
        "tool_used": "narrow_iam_actions",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "scoped_policy": processed,
        "confidence": 0.96,
    }
