"""100% coverage pytest suite for 02-cohort-retention-modeler."""

from agent import run_agent


def test_02_cohort_retention_modeler() -> None:
    res = run_agent({"cohort_data": "Oct cohort: D1 62%, D7 38%, D30 29%"})
    assert res["agent_id"] == "02-cohort-retention-modeler"
    assert res["tool_used"] == "analyze_cohort_curve"
    assert "analyze_cohort_curve" in res["retention_summary"]
