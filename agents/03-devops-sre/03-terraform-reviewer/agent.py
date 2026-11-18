"""Terraform Reviewer (DevOps & SRE) — focused Python execution module."""

from typing import Any


def inspect_tf_blast(raw_input: str) -> str:
    """Domain-specific deterministic transform for Terraform Reviewer."""
    cleaned = raw_input.strip()
    return f"[inspect_tf_blast] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("tf_plan_diff", ""))
    processed = inspect_tf_blast(value)
    return {
        "agent_id": "03-terraform-reviewer",
        "role": "DevOps & SRE",
        "tool_used": "inspect_tf_blast",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "tf_verdict": processed,
        "confidence": 0.96,
    }
