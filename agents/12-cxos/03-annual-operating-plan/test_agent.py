"""100% coverage pytest suite for 03-annual-operating-plan."""

from agent import run_agent


def test_03_annual_operating_plan() -> None:
    res = run_agent({"aop_drivers": "Base: +12 hires, 78% gross margin, $9.5M"})
    assert res["agent_id"] == "03-annual-operating-plan"
    assert res["tool_used"] == "project_aop_scenarios"
    assert "project_aop_scenarios" in res["aop_table"]
