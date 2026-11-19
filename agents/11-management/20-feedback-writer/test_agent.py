"""100% coverage pytest suite for 20-feedback-writer."""

from agent import run_agent


def test_20_feedback_writer() -> None:
    res = run_agent({"observed_behavior": "In Tuesday's design review you interrupted two juniors; they stopped presenting; the design missed two edge cases"})
    assert res["agent_id"] == "20-feedback-writer"
    assert res["tool_used"] == "write_feedback"
    assert "write_feedback" in res["feedback_draft"]
