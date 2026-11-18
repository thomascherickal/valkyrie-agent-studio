"""100% coverage pytest suite for 07-regression-selector."""

from agent import run_agent


def test_07_regression_selector() -> None:
    res = run_agent({"changed_files": "studio-core/valkyrie/subscription_manage"})
    assert res["agent_id"] == "07-regression-selector"
    assert res["tool_used"] == "map_impacted_tests"
    assert "map_impacted_tests" in res["selected_tests"]
