"""100% coverage pytest suite for 09-load-test-modeler."""

from agent import run_agent


def test_09_load_test_modeler() -> None:
    res = run_agent({"target_sla": "Target 1,200 RPS, p95 < 120ms, error rat"})
    assert res["agent_id"] == "09-load-test-modeler"
    assert res["tool_used"] == "build_k6_profile"
    assert "build_k6_profile" in res["load_script"]
