"""100% coverage pytest suite for 19-build-buy-evaluator."""

from agent import run_agent


def test_19_build_buy_evaluator() -> None:
    res = run_agent({"capability_request": "Need in-app e-signature within 2 quarters; vendor quotes 45k per year, in-house estimate 5 engineer-months"})
    assert res["agent_id"] == "19-build-buy-evaluator"
    assert res["tool_used"] == "compare_build_buy"
    assert "compare_build_buy" in res["decision_memo"]
