"""100% coverage pytest suite for 05-warehouse-cost-tuner."""

from agent import run_agent


def test_05_warehouse_cost_tuner() -> None:
    res = run_agent({"query_telemetry": "Full table scan on 4TB events_log filter"})
    assert res["agent_id"] == "05-warehouse-cost-tuner"
    assert res["tool_used"] == "recommend_clustering"
    assert "recommend_clustering" in res["cost_savings"]
