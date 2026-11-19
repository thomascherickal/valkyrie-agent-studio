"""100% coverage pytest suite for 17-earnings-call-prep-coach."""

from agent import run_agent


def test_17_earnings_call_prep_coach() -> None:
    res = run_agent({"quarter_results": "Revenue +22% (guide +25%), gross margin down 1.8 points, guidance cut for next quarter, one-time charge"})
    assert res["agent_id"] == "17-earnings-call-prep-coach"
    assert res["tool_used"] == "prep_earnings_call"
    assert "prep_earnings_call" in res["qa_prep"]
