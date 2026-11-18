"""100% coverage pytest suite for 04-data-quality-guardian."""

from agent import run_agent


def test_04_data_quality_guardian() -> None:
    res = run_agent({"dataset_profile": "fact_invoices: ~120k rows/day, 0% null i"})
    assert res["agent_id"] == "04-data-quality-guardian"
    assert res["tool_used"] == "build_dq_assertions"
    assert "build_dq_assertions" in res["dq_rules"]
