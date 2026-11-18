"""100% coverage pytest suite for 01-incident-commander."""

from agent import run_agent


def test_01_incident_commander() -> None:
    res = run_agent({"alert_payload": "SEV-1: API 5xx rate 18% in us-east-1 aft"})
    assert res["agent_id"] == "01-incident-commander"
    assert res["tool_used"] == "build_ics_timeline"
    assert "build_ics_timeline" in res["command_plan"]
