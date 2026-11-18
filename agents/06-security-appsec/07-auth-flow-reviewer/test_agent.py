"""100% coverage pytest suite for 07-auth-flow-reviewer."""

from agent import run_agent


def test_07_auth_flow_reviewer() -> None:
    res = run_agent({"auth_spec": "OAuth2 Authorization Code flow without P"})
    assert res["agent_id"] == "07-auth-flow-reviewer"
    assert res["tool_used"] == "audit_oauth_flow"
    assert "audit_oauth_flow" in res["auth_findings"]
