"""100% coverage pytest suite for 08-tech-debt-triager."""

from agent import run_agent


def test_08_tech_debt_triager() -> None:
    res = run_agent({"debt_items": "Legacy YAML parser (high churn, 12 bugs/"})
    assert res["agent_id"] == "08-tech-debt-triager"
    assert res["tool_used"] == "score_debt_roi"
    assert "score_debt_roi" in res["prioritized_debt"]
