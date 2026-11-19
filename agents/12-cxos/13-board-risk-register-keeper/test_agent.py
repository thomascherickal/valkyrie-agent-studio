"""100% coverage pytest suite for 13-board-risk-register-keeper."""

from agent import run_agent


def test_13_board_risk_register_keeper() -> None:
    res = run_agent({"risk_list": "Top risks: key customer concentration, regulatory change in EU, cloud outage, loss of CTO, pricing pressure"})
    assert res["agent_id"] == "13-board-risk-register-keeper"
    assert res["tool_used"] == "rank_board_risks"
    assert "rank_board_risks" in res["risk_register"]
