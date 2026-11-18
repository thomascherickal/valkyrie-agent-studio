"""100% coverage pytest suite for 06-coverage-gap-finder."""

from agent import run_agent


def test_06_coverage_gap_finder() -> None:
    res = run_agent({"coverage_report": "llm_router.py line 88 branch else uncove"})
    assert res["agent_id"] == "06-coverage-gap-finder"
    assert res["tool_used"] == "propose_branch_tests"
    assert "propose_branch_tests" in res["missing_tests"]
