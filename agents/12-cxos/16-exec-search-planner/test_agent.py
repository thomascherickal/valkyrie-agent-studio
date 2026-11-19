"""100% coverage pytest suite for 16-exec-search-planner."""

from agent import run_agent


def test_16_exec_search_planner() -> None:
    res = run_agent({"role_need": "Need a VP Sales for a 6M to 25M ARR journey; enterprise motion new; current head of sales leaving in 3 months"})
    assert res["agent_id"] == "16-exec-search-planner"
    assert res["tool_used"] == "plan_exec_search"
    assert "plan_exec_search" in res["search_plan"]
