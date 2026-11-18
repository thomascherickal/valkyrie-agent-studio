"""100% coverage pytest suite for 06-dependency-auditor."""

from agent import run_agent


def test_06_dependency_auditor() -> None:
    res = run_agent({"dependencies": "requests==2.32.0, pyyaml==6.0.2, gpl-lib"})
    assert res["agent_id"] == "06-dependency-auditor"
    assert res["tool_used"] == "scan_licenses"
    assert "scan_licenses" in res["audit_report"]
