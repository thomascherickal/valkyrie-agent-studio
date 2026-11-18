"""100% coverage pytest suite for 05-perf-review-synthesizer."""

from agent import run_agent


def test_05_perf_review_synthesizer() -> None:
    res = run_agent({"feedback_notes": "Strong systems design; can delegate code"})
    assert res["agent_id"] == "05-perf-review-synthesizer"
    assert res["tool_used"] == "synthesize_feedback"
    assert "synthesize_feedback" in res["review_draft"]
