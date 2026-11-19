"""100% coverage pytest suite for 14-referral-program-designer."""

from agent import run_agent


def test_14_referral_program_designer() -> None:
    res = run_agent({"referral_brief": "B2B SaaS, 5k active accounts, wants teams to refer peers; CAC 1,200; considering a 100 credit on both sides"})
    assert res["agent_id"] == "14-referral-program-designer"
    assert res["tool_used"] == "design_referral"
    assert "design_referral" in res["referral_design"]
