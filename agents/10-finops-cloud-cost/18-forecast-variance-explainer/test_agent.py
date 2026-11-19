"""100% coverage pytest suite for 18-forecast-variance-explainer."""

from agent import run_agent


def test_18_forecast_variance_explainer() -> None:
    res = run_agent({"actual_vs_forecast": "Forecast 1.20M, actual 1.38M (+15%); traffic +9%, new region launch, one-off 40k migration; reservation discount lower than planned"})
    assert res["agent_id"] == "18-forecast-variance-explainer"
    assert res["tool_used"] == "explain_cost_variance"
    assert "explain_cost_variance" in res["variance_story"]
