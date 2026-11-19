"""100% coverage pytest suite for 15-logging-quality-reviewer."""

from agent import run_agent


def test_15_logging_quality_reviewer() -> None:
    res = run_agent({"log_samples": "logger.info(\"user \" + email + \" paid \" + card_number); logger.debug(\"here\")"})
    assert res["agent_id"] == "15-logging-quality-reviewer"
    assert res["tool_used"] == "review_log_statements"
    assert "review_log_statements" in res["logging_review"]
