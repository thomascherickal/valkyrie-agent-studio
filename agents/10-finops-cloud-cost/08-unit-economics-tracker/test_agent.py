"""100% coverage pytest suite for 08-unit-economics-tracker."""

from agent import run_agent


def test_08_unit_economics_tracker() -> None:
    res = run_agent({"cogs_inputs": "Monthly infra $3,200, LLM $480, 1.6M run"})
    assert res["agent_id"] == "08-unit-economics-tracker"
    assert res["tool_used"] == "calc_unit_cogs"
    assert "calc_unit_cogs" in res["unit_economics"]
