"""100% coverage pytest suite for 20-strategic-bet-reviewer."""

from agent import run_agent


def test_20_strategic_bet_reviewer() -> None:
    res = run_agent({"bet_proposal": "Enter the healthcare vertical: 4M investment over 18 months, new compliance burden, 3 design partners signed"})
    assert res["agent_id"] == "20-strategic-bet-reviewer"
    assert res["tool_used"] == "review_strategic_bet"
    assert "review_strategic_bet" in res["bet_review"]
