"""100% coverage pytest suite for 03-refactor-planner."""

from agent import run_agent


def test_03_refactor_planner() -> None:
    res = run_agent({"module_metrics": "monolith_auth.py: 1850 LOC, 14 callers, "})
    assert res["agent_id"] == "03-refactor-planner"
    assert res["tool_used"] == "plan_strangler_steps"
    assert "plan_strangler_steps" in res["refactor_plan"]
