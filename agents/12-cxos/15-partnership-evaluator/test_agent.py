"""100% coverage pytest suite for 15-partnership-evaluator."""

from agent import run_agent


def test_15_partnership_evaluator() -> None:
    res = run_agent({"partnership_terms": "Channel partner offers access to 800 mid-market accounts for 25% revenue share; exclusivity 2 years; co-marketing"})
    assert res["agent_id"] == "15-partnership-evaluator"
    assert res["tool_used"] == "score_partnership"
    assert "score_partnership" in res["partner_memo"]
