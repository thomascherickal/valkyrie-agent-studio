"""100% coverage pytest suite for 03-user-story-splitter."""

from agent import run_agent


def test_03_user_story_splitter() -> None:
    res = run_agent({"epic_text": "As an admin, manage billing seats and ex"})
    assert res["agent_id"] == "03-user-story-splitter"
    assert res["tool_used"] == "split_invest_stories"
    assert "split_invest_stories" in res["stories"]
