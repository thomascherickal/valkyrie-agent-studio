"""API Error Explainer (Technical Support) — focused Python execution module."""

from typing import Any


def explain_api_error(raw_input: str) -> str:
    """Domain-specific deterministic transform for API Error Explainer."""
    cleaned = raw_input.strip()
    return f"[explain_api_error] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("error_payload", ""))
    processed = explain_api_error(value)
    return {
        "agent_id": "07-api-error-explainer",
        "role": "Technical Support",
        "tool_used": "explain_api_error",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "fix_guidance": processed,
        "confidence": 0.96,
    }
