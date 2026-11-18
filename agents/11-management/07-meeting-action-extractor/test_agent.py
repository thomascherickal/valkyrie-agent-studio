"""100% coverage pytest suite for 07-meeting-action-extractor."""

from agent import run_agent


def test_07_meeting_action_extractor() -> None:
    res = run_agent({"meeting_notes": "Alice to ship Cargo workspace by Fri; Bo"})
    assert res["agent_id"] == "07-meeting-action-extractor"
    assert res["tool_used"] == "extract_action_items"
    assert "extract_action_items" in res["action_table"]
