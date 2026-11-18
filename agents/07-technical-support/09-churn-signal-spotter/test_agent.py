"""100% coverage pytest suite for 09-churn-signal-spotter."""

from agent import run_agent


def test_09_churn_signal_spotter() -> None:
    res = run_agent({"thread_history": "3rd escalation this month on rate-limit "})
    assert res["agent_id"] == "09-churn-signal-spotter"
    assert res["tool_used"] == "compute_churn_risk"
    assert "compute_churn_risk" in res["csm_alert"]
