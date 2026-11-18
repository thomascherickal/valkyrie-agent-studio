"""100% coverage pytest suite for 06-ci-pipeline-optimizer."""

from agent import run_agent


def test_06_ci_pipeline_optimizer() -> None:
    res = run_agent({"ci_timings": "npm install: 4m, cargo build: 9m (no scc"})
    assert res["agent_id"] == "06-ci-pipeline-optimizer"
    assert res["tool_used"] == "optimize_dag"
    assert "optimize_dag" in res["pipeline_savings"]
