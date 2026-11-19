"""100% coverage pytest suite for 17-tradeoff-advisor."""

from agent import run_agent


def test_17_tradeoff_advisor() -> None:
    res = run_agent({"competing_asks": "Sales wants a custom export for a 300k deal; support wants fixes for 40 tickets; platform wants a 3-week upgrade"})
    assert res["agent_id"] == "17-tradeoff-advisor"
    assert res["tool_used"] == "weigh_tradeoffs"
    assert "weigh_tradeoffs" in res["tradeoff_memo"]
