"""API Reference Polisher (Developer Relations & Docs) — focused Python execution module."""

from typing import Any


def enrich_api_examples(raw_input: str) -> str:
    """Domain-specific deterministic transform for API Reference Polisher."""
    cleaned = raw_input.strip()
    return f"[enrich_api_examples] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("endpoint_def", ""))
    processed = enrich_api_examples(value)
    return {
        "agent_id": "02-api-reference-polisher",
        "role": "Developer Relations & Docs",
        "tool_used": "enrich_api_examples",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "reference_md": processed,
        "confidence": 0.96,
    }
