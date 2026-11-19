"""100% coverage pytest suite for 13-conflict-mediation-guide."""

from agent import run_agent


def test_13_conflict_mediation_guide() -> None:
    res = run_agent({"conflict_summary": "Two senior engineers disagree on ownership of the auth service; reviews have turned sharp; 3 teammates raised concerns"})
    assert res["agent_id"] == "13-conflict-mediation-guide"
    assert res["tool_used"] == "plan_mediation"
    assert "plan_mediation" in res["mediation_plan"]
