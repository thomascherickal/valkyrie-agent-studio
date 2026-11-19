"""100% coverage pytest suite for 14-docs-ia-reviewer."""

from agent import run_agent


def test_14_docs_ia_reviewer() -> None:
    res = run_agent({"site_map": "410 pages, 9 top-level sections, 3 pages named Overview, quickstart is 4 clicks from the home page"})
    assert res["agent_id"] == "14-docs-ia-reviewer"
    assert res["tool_used"] == "review_docs_ia"
    assert "review_docs_ia" in res["ia_review"]
