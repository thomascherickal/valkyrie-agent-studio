"""100% coverage pytest suite for 08-tech-strategy-summarizer."""

from agent import run_agent


def test_08_tech_strategy_summarizer() -> None:
    res = run_agent({"rfc_outline": "Adopt Universal Agent IR + Rust transpil"})
    assert res["agent_id"] == "08-tech-strategy-summarizer"
    assert res["tool_used"] == "distill_decision_memo"
    assert "distill_decision_memo" in res["memo_md"]
