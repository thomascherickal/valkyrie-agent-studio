"""100% coverage pytest suite for 16-csat-feedback-analyst."""

from agent import run_agent


def test_16_csat_feedback_analyst() -> None:
    res = run_agent({"csat_comments": "Responses 620, score 4.1; low scores cite slow replies and repeated questions; praise for clear steps"})
    assert res["agent_id"] == "16-csat-feedback-analyst"
    assert res["tool_used"] == "analyze_csat"
    assert "analyze_csat" in res["csat_insights"]
