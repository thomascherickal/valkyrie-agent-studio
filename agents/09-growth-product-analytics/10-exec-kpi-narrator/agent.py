"""Exec KPI Narrator (Growth & Product Analytics) — focused Python execution module."""

from typing import Any


def narrate_weekly_kpis(raw_input: str) -> str:
    """Domain-specific deterministic transform for Exec KPI Narrator."""
    cleaned = raw_input.strip()
    return f"[narrate_weekly_kpis] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("kpi_table", ""))
    processed = narrate_weekly_kpis(value)
    return {
        "agent_id": "10-exec-kpi-narrator",
        "role": "Growth & Product Analytics",
        "tool_used": "narrate_weekly_kpis",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "kpi_memo": processed,
        "confidence": 0.96,
    }
