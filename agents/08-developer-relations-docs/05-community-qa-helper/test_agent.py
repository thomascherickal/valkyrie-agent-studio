"""100% coverage pytest suite for 05-community-qa-helper."""

from agent import run_agent


def test_05_community_qa_helper() -> None:
    res = run_agent({"question_text": "How do I switch between OpenRouter free "})
    assert res["agent_id"] == "05-community-qa-helper"
    assert res["tool_used"] == "compose_community_reply"
    assert "compose_community_reply" in res["reply_md"]
