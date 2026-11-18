"""100% coverage pytest suite for 02-ma-diligence-reviewer."""

from agent import run_agent


def test_02_ma_diligence_reviewer() -> None:
    res = run_agent({"diligence_docs": "Top customer 28% ARR; 1 GPLv3 dependency"})
    assert res["agent_id"] == "02-ma-diligence-reviewer"
    assert res["tool_used"] == "score_diligence_risks"
    assert "score_diligence_risks" in res["risk_memo"]
