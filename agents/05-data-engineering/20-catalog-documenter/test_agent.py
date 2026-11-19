"""100% coverage pytest suite for 20-catalog-documenter."""

from agent import run_agent


def test_20_catalog_documenter() -> None:
    res = run_agent({"table_metadata": "fct_subscriptions: one row per subscription per month, columns mrr, plan_id, started_at, churned_at"})
    assert res["agent_id"] == "20-catalog-documenter"
    assert res["tool_used"] == "document_dataset"
    assert "document_dataset" in res["catalog_entry"]
