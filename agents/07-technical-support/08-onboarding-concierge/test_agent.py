"""100% coverage pytest suite for 08-onboarding-concierge."""

from agent import run_agent


def test_08_onboarding_concierge() -> None:
    res = run_agent({"customer_profile": "50-person eng org using GitHub, Okta, an"})
    assert res["agent_id"] == "08-onboarding-concierge"
    assert res["tool_used"] == "generate_setup_plan"
    assert "generate_setup_plan" in res["onboarding_plan"]
