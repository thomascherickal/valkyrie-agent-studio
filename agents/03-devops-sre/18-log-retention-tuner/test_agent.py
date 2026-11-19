"""100% coverage pytest suite for 18-log-retention-tuner."""

from agent import run_agent


def test_18_log_retention_tuner() -> None:
    res = run_agent({"log_volumes": "Audit logs 2 TB/month kept 7 years, app logs 40 TB/month kept 90 days, debug 25 TB/month kept 30 days"})
    assert res["agent_id"] == "18-log-retention-tuner"
    assert res["tool_used"] == "tune_log_retention"
    assert "tune_log_retention" in res["retention_policy"]
