"""100% coverage pytest suite for 18-pmf-survey-analyst."""

from agent import run_agent


def test_18_pmf_survey_analyst() -> None:
    res = run_agent({"survey_counts": "150 responses: 54 very disappointed, 63 somewhat, 33 not disappointed; strongest in agencies"})
    assert res["agent_id"] == "18-pmf-survey-analyst"
    assert res["tool_used"] == "score_pmf_survey"
    assert "score_pmf_survey" in res["pmf_readout"]
