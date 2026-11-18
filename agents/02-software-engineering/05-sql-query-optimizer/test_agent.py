"""100% coverage pytest suite for 05-sql-query-optimizer."""

from agent import run_agent


def test_05_sql_query_optimizer() -> None:
    res = run_agent({"sql_query": "SELECT * FROM runs WHERE org_id = $1 ORD"})
    assert res["agent_id"] == "05-sql-query-optimizer"
    assert res["tool_used"] == "suggest_indexes"
    assert "suggest_indexes" in res["optimization_plan"]
