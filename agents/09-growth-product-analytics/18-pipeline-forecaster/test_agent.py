"""100% coverage pytest suite for 18-pipeline-forecaster."""

from agent import run_agent


def test_18_pipeline_forecaster() -> None:
    res = run_agent({"pipeline_snapshot": "Q4 pipeline: 80 deals, 24 in proposal, 9 in negotiation; average deal 38k; 3 deals older than 120 days"})
    assert res["agent_id"] == "18-pipeline-forecaster"
    assert res["tool_used"] == "forecast_pipeline"
    assert "forecast_pipeline" in res["forecast"]
