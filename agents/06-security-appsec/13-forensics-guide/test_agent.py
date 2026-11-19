"""100% coverage pytest suite for 13-forensics-guide."""

from agent import run_agent


def test_13_forensics_guide() -> None:
    res = run_agent({"incident_summary": "Suspected credential theft on 3 production hosts, first alert 02:10 UTC, logs kept 14 days"})
    assert res["agent_id"] == "13-forensics-guide"
    assert res["tool_used"] == "plan_forensics"
    assert "plan_forensics" in res["forensics_plan"]
