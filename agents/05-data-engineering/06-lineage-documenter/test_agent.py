"""100% coverage pytest suite for 06-lineage-documenter."""

from agent import run_agent


def test_06_lineage_documenter() -> None:
    res = run_agent({"sql_graph": "mart_arr derives from dim_subs + fct_pay"})
    assert res["agent_id"] == "06-lineage-documenter"
    assert res["tool_used"] == "trace_column_lineage"
    assert "trace_column_lineage" in res["lineage_map"]
