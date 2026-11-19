"""100% coverage pytest suite for 11-error-handling-auditor."""

from agent import run_agent


def test_11_error_handling_auditor() -> None:
    res = run_agent({"code_excerpt": "try: charge(card) except Exception: pass  # then marks the order paid"})
    assert res["agent_id"] == "11-error-handling-auditor"
    assert res["tool_used"] == "audit_error_paths"
    assert "audit_error_paths" in res["error_audit"]
