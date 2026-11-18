"""100% coverage pytest suite for 03-ab-test-interpreter."""

from agent import run_agent


def test_03_ab_test_interpreter() -> None:
    res = run_agent({"ab_results": "Control: 12.1% (n=5000), Variant: 14.4% "})
    assert res["agent_id"] == "03-ab-test-interpreter"
    assert res["tool_used"] == "evaluate_ab_stats"
    assert "evaluate_ab_stats" in res["experiment_verdict"]
