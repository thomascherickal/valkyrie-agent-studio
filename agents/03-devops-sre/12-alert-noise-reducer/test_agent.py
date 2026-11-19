"""100% coverage pytest suite for 12-alert-noise-reducer."""

from agent import run_agent


def test_12_alert_noise_reducer() -> None:
    res = run_agent({"alert_history": "CPUHigh fired 310 times, 4 led to action; DiskSlow 95 times, 60 actioned; QueueLag 40 times, 38 actioned"})
    assert res["agent_id"] == "12-alert-noise-reducer"
    assert res["tool_used"] == "rank_noisy_alerts"
    assert "rank_noisy_alerts" in res["noise_plan"]
