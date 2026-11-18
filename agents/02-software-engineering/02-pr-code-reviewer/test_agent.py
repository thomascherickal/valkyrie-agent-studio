"""100% coverage pytest suite for 02-pr-code-reviewer."""

from agent import run_agent


def test_02_pr_code_reviewer() -> None:
    res = run_agent({"diff_snippet": "for item in items: db.query(item.id) # N"})
    assert res["agent_id"] == "02-pr-code-reviewer"
    assert res["tool_used"] == "detect_antipatterns"
    assert "detect_antipatterns" in res["review_comments"]
