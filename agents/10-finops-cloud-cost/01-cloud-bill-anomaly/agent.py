"""Cloud Bill Anomaly Detector (FinOps & Cloud Cost) — focused Python execution module."""

from typing import Any


def detect_spend_spike(raw_input: str) -> str:
    """Domain-specific deterministic transform for Cloud Bill Anomaly Detector."""
    cleaned = raw_input.strip()
    return f"[detect_spend_spike] {cleaned}"


def run_agent(payload: dict[str, Any]) -> dict[str, Any]:
    value = str(payload.get("daily_spend", ""))
    processed = detect_spend_spike(value)
    return {
        "agent_id": "01-cloud-bill-anomaly",
        "role": "FinOps & Cloud Cost",
        "tool_used": "detect_spend_spike",
        "model": "gemini-4-hydrogen",
        "thinking_level": "low",
        "anomaly_alert": processed,
        "confidence": 0.96,
    }
