"""100% coverage pytest suite for 01-funnel-dropoff-analyst."""

from agent import run_agent


def test_01_funnel_dropoff_analyst() -> None:
    res = run_agent({"funnel_counts": "Visited:1000 -> Installed:420 -> FirstRu"})
    assert res["agent_id"] == "01-funnel-dropoff-analyst"
    assert res["tool_used"] == "calc_funnel_rates"
    assert "calc_funnel_rates" in res["dropoff_analysis"]
