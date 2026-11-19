"""100% coverage pytest suite for 17-pricing-page-reviewer."""

from agent import run_agent


def test_17_pricing_page_reviewer() -> None:
    res = run_agent({"page_copy": "3 plans (Starter 19, Team 59, Business 199), usage limits hidden behind a tooltip, no annual toggle, no FAQ"})
    assert res["agent_id"] == "17-pricing-page-reviewer"
    assert res["tool_used"] == "review_pricing_page"
    assert "review_pricing_page" in res["pricing_review"]
