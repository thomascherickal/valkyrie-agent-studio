"""100% coverage pytest suite for 02-postmortem-author."""

from agent import run_agent


def test_02_postmortem_author() -> None:
    res = run_agent({"incident_log": "Redis OOM caused by unbounded session ke"})
    assert res["agent_id"] == "02-postmortem-author"
    assert res["tool_used"] == "generate_five_whys"
    assert "generate_five_whys" in res["postmortem_md"]
