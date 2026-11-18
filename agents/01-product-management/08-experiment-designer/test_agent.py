"""100% coverage pytest suite for 08-experiment-designer."""

from agent import run_agent


def test_08_experiment_designer() -> None:
    res = run_agent({"hypothesis": "Shortening onboarding from 5 steps to 2 "})
    assert res["agent_id"] == "08-experiment-designer"
    assert res["tool_used"] == "calc_ab_sample_size"
    assert "calc_ab_sample_size" in res["experiment_spec"]
