"""100% coverage pytest suite for 03-escalation-packager."""

from agent import run_agent


def test_03_escalation_packager() -> None:
    res = run_agent({"case_notes": "Customer v2.4.1 on Ubuntu 24.04; trace_i"})
    assert res["agent_id"] == "03-escalation-packager"
    assert res["tool_used"] == "package_l3_handoff"
    assert "package_l3_handoff" in res["escalation_card"]
