"""100% coverage pytest suite for 11-delegation-coach."""

from agent import run_agent


def test_11_delegation_coach() -> None:
    res = run_agent({"task_list": "My tasks: weekly metrics report, vendor negotiation, hiring screens, incident reviews, roadmap draft"})
    assert res["agent_id"] == "11-delegation-coach"
    assert res["tool_used"] == "plan_delegation"
    assert "plan_delegation" in res["delegation_plan"]
