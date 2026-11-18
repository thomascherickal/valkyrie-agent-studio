"""100% coverage pytest suite for 10-dev-survey-analyst."""

from agent import run_agent


def test_10_dev_survey_analyst() -> None:
    res = run_agent({"survey_responses": "Top pain: setting up Rust toolchain; Top"})
    assert res["agent_id"] == "10-dev-survey-analyst"
    assert res["tool_used"] == "summarize_dx_metrics"
    assert "summarize_dx_metrics" in res["dx_report"]
