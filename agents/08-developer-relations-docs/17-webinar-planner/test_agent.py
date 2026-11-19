"""100% coverage pytest suite for 17-webinar-planner."""

from agent import run_agent


def test_17_webinar_planner() -> None:
    res = run_agent({"webinar_brief": "Live build of a webhook-driven workflow, 45 minutes, target 400 registrants, 2 speakers, recording afterwards"})
    assert res["agent_id"] == "17-webinar-planner"
    assert res["tool_used"] == "plan_webinar"
    assert "plan_webinar" in res["webinar_plan"]
