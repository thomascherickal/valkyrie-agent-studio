"""100% coverage pytest suite for 10-stakeholder-brief."""

from agent import run_agent


def test_10_stakeholder_brief() -> None:
    res = run_agent({"weekly_updates": "Shipped v2.1 API; p99 latency down 38%; "})
    assert res["agent_id"] == "10-stakeholder-brief"
    assert res["tool_used"] == "summarize_exec_digest"
    assert "summarize_exec_digest" in res["brief_text"]
