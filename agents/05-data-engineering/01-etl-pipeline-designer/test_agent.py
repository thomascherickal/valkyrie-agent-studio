"""100% coverage pytest suite for 01-etl-pipeline-designer."""

from agent import run_agent


def test_01_etl_pipeline_designer() -> None:
    res = run_agent({"source_spec": "Hourly Stripe webhook events -> BigQuery"})
    assert res["agent_id"] == "01-etl-pipeline-designer"
    assert res["tool_used"] == "design_idempotent_dag"
    assert "design_idempotent_dag" in res["dag_spec"]
