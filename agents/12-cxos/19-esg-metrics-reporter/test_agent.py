"""100% coverage pytest suite for 19-esg-metrics-reporter."""

from agent import run_agent


def test_19_esg_metrics_reporter() -> None:
    res = run_agent({"esg_inputs": "Cloud 1,900 MWh, offices 420 MWh, travel 310 tCO2e; 58% renewable power; target net zero by 2040"})
    assert res["agent_id"] == "19-esg-metrics-reporter"
    assert res["tool_used"] == "compile_esg_metrics"
    assert "compile_esg_metrics" in res["esg_summary"]
