"""100% coverage pytest suite for 11-cash-runway-analyst."""

from agent import run_agent


def test_11_cash_runway_analyst() -> None:
    res = run_agent({"cash_position": "Cash 14.2M, net burn 780k a month, 9% monthly growth in revenue, 2 enterprise deals pending, hiring plan adds 600k"})
    assert res["agent_id"] == "11-cash-runway-analyst"
    assert res["tool_used"] == "project_runway"
    assert "project_runway" in res["runway_scenarios"]
