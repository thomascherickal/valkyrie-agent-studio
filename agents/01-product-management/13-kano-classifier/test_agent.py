"""100% coverage pytest suite for 13-kano-classifier."""

from agent import run_agent


def test_13_kano_classifier() -> None:
    res = run_agent({"survey_results": "SSO: 72% would be happy with it, 55% unhappy without it; dark mode: 40% happy, 6% unhappy without"})
    assert res["agent_id"] == "13-kano-classifier"
    assert res["tool_used"] == "classify_kano"
    assert "classify_kano" in res["kano_matrix"]
