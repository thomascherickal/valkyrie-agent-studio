"""100% coverage pytest suite for 16-first-90-days-planner."""

from agent import run_agent


def test_16_first_90_days_planner() -> None:
    res = run_agent({"role_context": "New engineering manager for a 9-person platform team, two open incidents, roadmap behind, one low-morale report"})
    assert res["agent_id"] == "16-first-90-days-planner"
    assert res["tool_used"] == "plan_first_quarter"
    assert "plan_first_quarter" in res["onboarding_plan"]
