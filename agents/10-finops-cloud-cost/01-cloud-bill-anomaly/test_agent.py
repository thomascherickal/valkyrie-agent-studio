"""100% coverage pytest suite for 01-cloud-bill-anomaly."""

from agent import run_agent


def test_01_cloud_bill_anomaly() -> None:
    res = run_agent({"daily_spend": "NAT Gateway us-east-1 jumped from $42/da"})
    assert res["agent_id"] == "01-cloud-bill-anomaly"
    assert res["tool_used"] == "detect_spend_spike"
    assert "detect_spend_spike" in res["anomaly_alert"]
