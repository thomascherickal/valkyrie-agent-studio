"""100% coverage pytest suite for 11-api-security-reviewer."""

from agent import run_agent


def test_11_api_security_reviewer() -> None:
    res = run_agent({"api_spec": "GET /invoices/{id} returns any invoice for any logged-in user; list endpoint has no pagination limit"})
    assert res["agent_id"] == "11-api-security-reviewer"
    assert res["tool_used"] == "review_api_security"
    assert "review_api_security" in res["api_findings"]
