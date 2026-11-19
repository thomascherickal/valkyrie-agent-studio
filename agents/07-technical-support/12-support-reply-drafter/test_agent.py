"""100% coverage pytest suite for 12-support-reply-drafter."""

from agent import run_agent


def test_12_support_reply_drafter() -> None:
    res = run_agent({"ticket_thread": "Customer: webhooks stopped arriving since Tuesday, production orders are stuck. Second message, no reply for 6 hours"})
    assert res["agent_id"] == "12-support-reply-drafter"
    assert res["tool_used"] == "draft_support_reply"
    assert "draft_support_reply" in res["reply_draft"]
