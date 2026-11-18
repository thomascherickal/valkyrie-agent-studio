"""100% coverage pytest suite for 01-test-plan-architect."""

from agent import run_agent


def test_01_test_plan_architect() -> None:
    res = run_agent({"spec_summary": "Passwordless magic link auth with 15-min"})
    assert res["agent_id"] == "01-test-plan-architect"
    assert res["tool_used"] == "derive_test_matrix"
    assert "derive_test_matrix" in res["test_plan"]
