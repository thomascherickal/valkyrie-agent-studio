"""100% coverage pytest suite for 20-codebase-onboarding-guide."""

from agent import run_agent


def test_20_codebase_onboarding_guide() -> None:
    res = run_agent({"repo_overview": "Monorepo with 3 services and a web app; setup takes a day; tests flaky on the first run"})
    assert res["agent_id"] == "20-codebase-onboarding-guide"
    assert res["tool_used"] == "write_onboarding_guide"
    assert "write_onboarding_guide" in res["onboarding_guide"]
