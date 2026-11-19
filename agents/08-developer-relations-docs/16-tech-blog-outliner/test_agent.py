"""100% coverage pytest suite for 16-tech-blog-outliner."""

from agent import run_agent


def test_16_tech_blog_outliner() -> None:
    res = run_agent({"topic_brief": "How we cut p99 latency 40% by moving session lookups from Postgres to a read-through cache"})
    assert res["agent_id"] == "16-tech-blog-outliner"
    assert res["tool_used"] == "outline_tech_post"
    assert "outline_tech_post" in res["post_outline"]
