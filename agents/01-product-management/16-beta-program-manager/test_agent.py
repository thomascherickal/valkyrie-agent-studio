"""100% coverage pytest suite for 16-beta-program-manager."""

from agent import run_agent


def test_16_beta_program_manager() -> None:
    res = run_agent({"beta_plan_brief": "Beta of the new reporting module for 40 accounts over 6 weeks; need a go or no-go by the end"})
    assert res["agent_id"] == "16-beta-program-manager"
    assert res["tool_used"] == "plan_beta_program"
    assert "plan_beta_program" in res["beta_playbook"]
