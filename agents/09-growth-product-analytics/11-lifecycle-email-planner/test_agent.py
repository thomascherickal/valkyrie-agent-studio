"""100% coverage pytest suite for 11-lifecycle-email-planner."""

from agent import run_agent


def test_11_lifecycle_email_planner() -> None:
    res = run_agent({"lifecycle_goals": "Goal: lift week-1 activation; 38% finish setup; users who invite a teammate retain 2x; trial lasts 14 days"})
    assert res["agent_id"] == "11-lifecycle-email-planner"
    assert res["tool_used"] == "plan_lifecycle_emails"
    assert "plan_lifecycle_emails" in res["email_plan"]
