"""100% coverage pytest suite for 14-executive-pricing-strategist."""

from agent import run_agent


def test_14_executive_pricing_strategist() -> None:
    res = run_agent({"pricing_context": "Considering a 12% price rise on the Team plan; competitors flat; 4% monthly churn risk if the rise lands badly"})
    assert res["agent_id"] == "14-executive-pricing-strategist"
    assert res["tool_used"] == "assess_pricing_strategy"
    assert "assess_pricing_strategy" in res["pricing_brief"]
