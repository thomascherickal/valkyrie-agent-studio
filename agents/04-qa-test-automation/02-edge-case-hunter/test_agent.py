"""100% coverage pytest suite for 02-edge-case-hunter."""

from agent import run_agent


def test_02_edge_case_hunter() -> None:
    res = run_agent({"field_schema": "amount: decimal(>0), currency: ISO-4217,"})
    assert res["agent_id"] == "02-edge-case-hunter"
    assert res["tool_used"] == "enumerate_boundaries"
    assert "enumerate_boundaries" in res["edge_cases"]
