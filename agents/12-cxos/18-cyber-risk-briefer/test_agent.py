"""100% coverage pytest suite for 18-cyber-risk-briefer."""

from agent import run_agent


def test_18_cyber_risk_briefer() -> None:
    res = run_agent({"security_summary": "3 critical findings open, MFA on 91% of staff, last restore test 14 months ago, ransomware drill planned"})
    assert res["agent_id"] == "18-cyber-risk-briefer"
    assert res["tool_used"] == "brief_cyber_risk"
    assert "brief_cyber_risk" in res["exec_risk_brief"]
