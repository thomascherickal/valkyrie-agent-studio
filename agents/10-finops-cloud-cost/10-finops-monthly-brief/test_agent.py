"""100% coverage pytest suite for 10-finops-monthly-brief."""

from agent import run_agent


def test_10_finops_monthly_brief() -> None:
    res = run_agent({"monthly_ledger": "Total $24.5k (-9% MoM), Savings realized"})
    assert res["agent_id"] == "10-finops-monthly-brief"
    assert res["tool_used"] == "compile_finops_brief"
    assert "compile_finops_brief" in res["monthly_report"]
