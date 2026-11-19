"""100% coverage pytest suite for 18-skip-level-prep-assistant."""

from agent import run_agent


def test_18_skip_level_prep_assistant() -> None:
    res = run_agent({"team_signals": "Team of 14 under 2 managers; engagement dip in the survey; reports mention unclear priorities and slow decisions"})
    assert res["agent_id"] == "18-skip-level-prep-assistant"
    assert res["tool_used"] == "prep_skip_level"
    assert "prep_skip_level" in res["skip_level_agenda"]
