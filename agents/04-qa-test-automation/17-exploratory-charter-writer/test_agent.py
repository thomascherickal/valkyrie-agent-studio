"""100% coverage pytest suite for 17-exploratory-charter-writer."""

from agent import run_agent


def test_17_exploratory_charter_writer() -> None:
    res = run_agent({"feature_summary": "New bulk-import feature: CSV up to 50k rows, duplicate detection, email report on completion"})
    assert res["agent_id"] == "17-exploratory-charter-writer"
    assert res["tool_used"] == "write_charters"
    assert "write_charters" in res["session_charters"]
