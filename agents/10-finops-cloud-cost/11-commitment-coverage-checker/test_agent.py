"""100% coverage pytest suite for 11-commitment-coverage-checker."""

from agent import run_agent


def test_11_commitment_coverage_checker() -> None:
    res = run_agent({"usage_summary": "Compute 410k a month on demand; commitments cover 52%, utilization 97%; baseline steady 70% of spend"})
    assert res["agent_id"] == "11-commitment-coverage-checker"
    assert res["tool_used"] == "check_commitment_coverage"
    assert "check_commitment_coverage" in res["coverage_report"]
