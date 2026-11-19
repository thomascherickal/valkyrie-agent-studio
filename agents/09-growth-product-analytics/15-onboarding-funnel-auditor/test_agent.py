"""100% coverage pytest suite for 15-onboarding-funnel-auditor."""

from agent import run_agent


def test_15_onboarding_funnel_auditor() -> None:
    res = run_agent({"onboarding_steps": "Signup, verify email, create workspace, invite team, connect data, first report; 61% drop at connect data"})
    assert res["agent_id"] == "15-onboarding-funnel-auditor"
    assert res["tool_used"] == "audit_onboarding"
    assert "audit_onboarding" in res["onboarding_audit"]
