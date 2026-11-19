"""100% coverage pytest suite for 20-security-test-case-writer."""

from agent import run_agent


def test_20_security_test_case_writer() -> None:
    res = run_agent({"feature_flow": "Password reset by email link; link valid 1 hour; any user can request unlimited resets"})
    assert res["agent_id"] == "20-security-test-case-writer"
    assert res["tool_used"] == "write_security_tests"
    assert "write_security_tests" in res["security_cases"]
