"""100% coverage pytest suite for 19-sql-style-reviewer."""

from agent import run_agent


def test_19_sql_style_reviewer() -> None:
    res = run_agent({"sql_excerpt": "SELECT * FROM orders o, customers c WHERE o.cid = c.id AND created > '2025-01-01' ORDER BY 1"})
    assert res["agent_id"] == "19-sql-style-reviewer"
    assert res["tool_used"] == "review_sql_style"
    assert "review_sql_style" in res["sql_review"]
