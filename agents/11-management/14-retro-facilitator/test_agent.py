"""100% coverage pytest suite for 14-retro-facilitator."""

from agent import run_agent


def test_14_retro_facilitator() -> None:
    res = run_agent({"retro_notes": "Sprint 42: 3 incidents, review wait 2 days, good pairing, unclear priorities; last retro's 4 actions: 1 done"})
    assert res["agent_id"] == "14-retro-facilitator"
    assert res["tool_used"] == "facilitate_retro"
    assert "facilitate_retro" in res["retro_actions"]
