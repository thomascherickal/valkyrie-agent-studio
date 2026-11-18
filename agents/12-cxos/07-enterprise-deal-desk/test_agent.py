"""100% coverage pytest suite for 07-enterprise-deal-desk."""

from agent import run_agent


def test_07_enterprise_deal_desk() -> None:
    res = run_agent({"deal_terms": "$250k/yr 3-yr deal requesting 99.99% SLA"})
    assert res["agent_id"] == "07-enterprise-deal-desk"
    assert res["tool_used"] == "score_deal_margin"
    assert "score_deal_margin" in res["deal_approval"]
