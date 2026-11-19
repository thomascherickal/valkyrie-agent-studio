"""100% coverage pytest suite for 12-api-sunset-planner."""

from agent import run_agent


def test_12_api_sunset_planner() -> None:
    res = run_agent({"api_usage": "v1 receives 2.1M calls a day from 140 clients; top 5 clients are 70% of traffic; v2 is stable"})
    assert res["agent_id"] == "12-api-sunset-planner"
    assert res["tool_used"] == "plan_api_sunset"
    assert "plan_api_sunset" in res["sunset_schedule"]
