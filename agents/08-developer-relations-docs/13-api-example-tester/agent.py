"""API Example Tester (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def test_api_examples(raw_input: str) -> str:
    """Domain-specific deterministic transform for API Example Tester."""
    cleaned = raw_input.strip()
    return f"[test_api_examples] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("code_examples", ""))
    processed = test_api_examples(value)
    return {
        "agent_id": "13-api-example-tester",
        "role": "Developer Relations & Docs",
        "tool_used": "test_api_examples",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "example_report": processed,
        "confidence": 0.96,
    }
