"""100% coverage pytest suite for 11-cdc-pipeline-designer."""

from agent import run_agent


def test_11_cdc_pipeline_designer() -> None:
    res = run_agent({"source_tables": "Postgres orders (4M rows, 300 updates/s peak), customers, payments; target warehouse within 5 minutes"})
    assert res["agent_id"] == "11-cdc-pipeline-designer"
    assert res["tool_used"] == "design_cdc_flow"
    assert "design_cdc_flow" in res["cdc_design"]
