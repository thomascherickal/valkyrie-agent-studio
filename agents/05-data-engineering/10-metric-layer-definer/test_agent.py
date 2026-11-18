"""100% coverage pytest suite for 10-metric-layer-definer."""

from agent import run_agent


def test_10_metric_layer_definer() -> None:
    res = run_agent({"kpi_request": "Net Revenue Retention trailing 12 months"})
    assert res["agent_id"] == "10-metric-layer-definer"
    assert res["tool_used"] == "define_semantic_metric"
    assert "define_semantic_metric" in res["metric_yaml"]
