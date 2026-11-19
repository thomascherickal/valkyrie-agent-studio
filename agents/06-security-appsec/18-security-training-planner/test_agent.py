"""100% coverage pytest suite for 18-security-training-planner."""

from agent import run_agent


def test_18_security_training_planner() -> None:
    res = run_agent({"team_profile": "420 staff: 90 engineers, 40 support with customer data access, 20 finance; phishing click rate 11%"})
    assert res["agent_id"] == "18-security-training-planner"
    assert res["tool_used"] == "plan_security_training"
    assert "plan_security_training" in res["training_plan"]
