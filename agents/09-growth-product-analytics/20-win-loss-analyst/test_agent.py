"""100% coverage pytest suite for 20-win-loss-analyst."""

from agent import run_agent


def test_20_win_loss_analyst() -> None:
    res = run_agent({"deal_notes": "Lost 14 of 30 mid-market deals; reasons: price vs incumbent 6, missing SSO 5, slow security review 3"})
    assert res["agent_id"] == "20-win-loss-analyst"
    assert res["tool_used"] == "analyze_win_loss"
    assert "analyze_win_loss" in res["win_loss_themes"]
