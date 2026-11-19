"""100% coverage pytest suite for 17-sunset-planner."""

from agent import run_agent


def test_17_sunset_planner() -> None:
    res = run_agent({"feature_usage": "Legacy CSV exporter: 3% of accounts, 180 weekly runs, replaced by the scheduled-reports API"})
    assert res["agent_id"] == "17-sunset-planner"
    assert res["tool_used"] == "plan_sunset"
    assert "plan_sunset" in res["sunset_plan"]
