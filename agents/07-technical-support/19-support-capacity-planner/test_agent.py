"""100% coverage pytest suite for 19-support-capacity-planner."""

from agent import run_agent


def test_19_support_capacity_planner() -> None:
    res = run_agent({"ticket_volume": "2,400 tickets a week, 14 min average handling, 30% shrinkage, volume growing 6% a month"})
    assert res["agent_id"] == "19-support-capacity-planner"
    assert res["tool_used"] == "plan_support_staffing"
    assert "plan_support_staffing" in res["staffing_plan"]
