"""100% coverage pytest suite for 07-capacity-planner."""

from agent import run_agent


def test_07_capacity_planner() -> None:
    res = run_agent({"traffic_forecast": "Current: 4k QPS @ 62% CPU; Q4 forecast: "})
    assert res["agent_id"] == "07-capacity-planner"
    assert res["tool_used"] == "model_headroom"
    assert "model_headroom" in res["scaling_plan"]
