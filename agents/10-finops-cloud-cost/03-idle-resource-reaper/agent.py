"""Idle Resource Reaper (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def flag_idle_assets(raw_input: str) -> str:
    """Domain-specific deterministic transform for Idle Resource Reaper."""
    cleaned = raw_input.strip()
    return f"[flag_idle_assets] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("infra_inventory", ""))
    processed = flag_idle_assets(value)
    return {
        "agent_id": "03-idle-resource-reaper",
        "role": "FinOps & Cloud Cost",
        "tool_used": "flag_idle_assets",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "reap_candidates": processed,
        "confidence": 0.96,
    }
