"""100% coverage pytest suite for 04-activation-metric-finder."""

from agent import run_agent


def test_04_activation_metric_finder() -> None:
    res = run_agent({"behavior_events": "Users who run >=3 sandbox tests in 48h r"})
    assert res["agent_id"] == "04-activation-metric-finder"
    assert res["tool_used"] == "rank_activation_signals"
    assert "rank_activation_signals" in res["aha_moment"]
