"""100% coverage pytest suite for 01-prd-architect."""

from agent import run_agent


def test_01_prd_architect() -> None:
    res = run_agent({"feature_brief": "Add SSO login with SAML 2.0 for enterpri"})
    assert res["agent_id"] == "01-prd-architect"
    assert res["tool_used"] == "extract_requirements"
    assert "extract_requirements" in res["prd_markdown"]
