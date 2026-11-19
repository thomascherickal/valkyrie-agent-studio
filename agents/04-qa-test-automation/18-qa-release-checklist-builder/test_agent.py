"""100% coverage pytest suite for 18-qa-release-checklist-builder."""

from agent import run_agent


def test_18_qa_release_checklist_builder() -> None:
    res = run_agent({"release_scope": "Release 4.12: new payment provider, 14 tickets, database migration, mobile app update on the same day"})
    assert res["agent_id"] == "18-qa-release-checklist-builder"
    assert res["tool_used"] == "build_release_checklist"
    assert "build_release_checklist" in res["qa_checklist"]
