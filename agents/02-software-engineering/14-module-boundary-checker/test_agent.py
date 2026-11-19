"""100% coverage pytest suite for 14-module-boundary-checker."""

from agent import run_agent


def test_14_module_boundary_checker() -> None:
    res = run_agent({"dependency_graph": "billing imports orders; orders imports billing; reports reads the orders table directly"})
    assert res["agent_id"] == "14-module-boundary-checker"
    assert res["tool_used"] == "check_module_boundaries"
    assert "check_module_boundaries" in res["boundary_report"]
