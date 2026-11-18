"""100% coverage pytest suite for 04-crisis-comms-strategist."""

from agent import run_agent


def test_04_crisis_comms_strategist() -> None:
    res = run_agent({"crisis_brief": "Third-party auth outage affecting 12% of"})
    assert res["agent_id"] == "04-crisis-comms-strategist"
    assert res["tool_used"] == "draft_comms_matrix"
    assert "draft_comms_matrix" in res["comms_playbook"]
