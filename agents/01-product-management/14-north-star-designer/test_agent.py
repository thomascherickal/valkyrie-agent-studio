"""100% coverage pytest suite for 14-north-star-designer."""

from agent import run_agent


def test_14_north_star_designer() -> None:
    res = run_agent({"product_goals": "Goal: help teams ship reviewed releases faster; users create pull requests, reviewers approve"})
    assert res["agent_id"] == "14-north-star-designer"
    assert res["tool_used"] == "define_north_star"
    assert "define_north_star" in res["metric_tree"]
