"""FinOps Monthly Brief (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def compile_finops_brief(raw_input: str) -> str:
    """Domain-specific deterministic transform for FinOps Monthly Brief."""
    cleaned = raw_input.strip()
    return f"[compile_finops_brief] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("monthly_ledger", ""))
    processed = compile_finops_brief(value)
    return {
        "agent_id": "10-finops-monthly-brief",
        "role": "FinOps & Cloud Cost",
        "tool_used": "compile_finops_brief",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "monthly_report": processed,
        "confidence": 0.96,
    }
