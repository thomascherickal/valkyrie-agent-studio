"""100% coverage pytest suite for 11-refund-policy-checker."""

from agent import run_agent


def test_11_refund_policy_checker() -> None:
    res = run_agent({"refund_request": "Annual plan bought 41 days ago, 3 logins, customer says the integration never worked; asks for full refund"})
    assert res["agent_id"] == "11-refund-policy-checker"
    assert res["tool_used"] == "check_refund_policy"
    assert "check_refund_policy" in res["refund_decision"]
