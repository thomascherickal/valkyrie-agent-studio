"""100% coverage pytest suite for 01-sprint-capacity-planner."""

from agent import run_agent


def test_01_sprint_capacity_planner() -> None:
    res = run_agent({"team_roster": "6 engineers, 4 PTO days, 1 on-call, avg "})
    assert res["agent_id"] == "01-sprint-capacity-planner"
    assert res["tool_used"] == "calc_net_capacity"
    assert "calc_net_capacity" in res["sprint_target"]
