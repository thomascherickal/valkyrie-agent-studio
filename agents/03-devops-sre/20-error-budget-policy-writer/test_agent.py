"""100% coverage pytest suite for 20-error-budget-policy-writer."""

from agent import run_agent


def test_20_error_budget_policy_writer() -> None:
    res = run_agent({"slo_context": "Checkout API SLO 99.9% over 30 days; product wants weekly releases; last month used 80% of budget"})
    assert res["agent_id"] == "20-error-budget-policy-writer"
    assert res["tool_used"] == "draft_budget_policy"
    assert "draft_budget_policy" in res["budget_policy"]
