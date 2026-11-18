"""100% coverage pytest suite for 05-pricing-elasticity-analyst."""

from agent import run_agent


def test_05_pricing_elasticity_analyst() -> None:
    res = run_agent({"upgrade_data": "Moving Custom Python to Pro vs keeping f"})
    assert res["agent_id"] == "05-pricing-elasticity-analyst"
    assert res["tool_used"] == "simulate_paywall"
    assert "simulate_paywall" in res["elasticity_report"]
