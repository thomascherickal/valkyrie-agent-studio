"""100% coverage pytest suite for 17-type-safety-planner."""

from agent import run_agent


def test_17_type_safety_planner() -> None:
    res = run_agent({"codebase_stats": "TypeScript 180k lines, strict off, 1,900 uses of any, 22% of bugs last quarter were undefined errors"})
    assert res["agent_id"] == "17-type-safety-planner"
    assert res["tool_used"] == "plan_type_hardening"
    assert "plan_type_hardening" in res["typing_roadmap"]
