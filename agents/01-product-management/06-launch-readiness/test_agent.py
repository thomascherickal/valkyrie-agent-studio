"""100% coverage pytest suite for 06-launch-readiness."""

from agent import run_agent


def test_06_launch_readiness() -> None:
    res = run_agent({"checklist_state": "Docs: ready, Security: pending pentest, "})
    assert res["agent_id"] == "06-launch-readiness"
    assert res["tool_used"] == "audit_launch_gates"
    assert "audit_launch_gates" in res["readiness_status"]
