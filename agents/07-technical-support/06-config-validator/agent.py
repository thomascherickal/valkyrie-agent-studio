"""Config Validator (Technical Support) — focused Python execution module."""

from typing import Any


def validate_customer_yaml(raw_input: str) -> str:
    """Domain-specific deterministic transform for Config Validator."""
    cleaned = raw_input.strip()
    return f"[validate_customer_yaml] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("yaml_snippet", ""))
    processed = validate_customer_yaml(value)
    return {
        "agent_id": "06-config-validator",
        "role": "Technical Support",
        "tool_used": "validate_customer_yaml",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "validation_hints": processed,
        "confidence": 0.96,
    }
