"""100% coverage pytest suite for 07-pricing-modeler."""

from agent import run_agent


def test_07_pricing_modeler() -> None:
    res = run_agent({"tier_assumptions": "Pro: $29/seat, 100k tokens included, COG"})
    assert res["agent_id"] == "07-pricing-modeler"
    assert res["tool_used"] == "simulate_unit_margin"
    assert "simulate_unit_margin" in res["margin_report"]
