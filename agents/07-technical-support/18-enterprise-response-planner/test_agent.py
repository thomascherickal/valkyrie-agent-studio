"""100% coverage pytest suite for 18-enterprise-response-planner."""

from agent import run_agent


def test_18_enterprise_response_planner() -> None:
    res = run_agent({"account_issue": "Acme (ARR 480k, renewal in 60 days): 3 severity-2 tickets in 2 weeks; exec sponsor emailed the CEO"})
    assert res["agent_id"] == "18-enterprise-response-planner"
    assert res["tool_used"] == "plan_enterprise_response"
    assert "plan_enterprise_response" in res["escalation_path"]
