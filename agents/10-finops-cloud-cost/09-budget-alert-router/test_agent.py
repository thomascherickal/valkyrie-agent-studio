"""100% coverage pytest suite for 09-budget-alert-router."""

from agent import run_agent


def test_09_budget_alert_router() -> None:
    res = run_agent({"budget_status": "Team Data-Eng at 88% of monthly budget o"})
    assert res["agent_id"] == "09-budget-alert-router"
    assert res["tool_used"] == "route_budget_warning"
    assert "route_budget_warning" in res["alert_payload"]
