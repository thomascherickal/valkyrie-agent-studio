"""100% coverage pytest suite for 19-saas-license-optimizer."""

from agent import run_agent


def test_19_saas_license_optimizer() -> None:
    res = run_agent({"license_usage": "CRM 480 seats, 61% active in 90 days; design tool 120 seats, 38 never opened; renewal in 70 days"})
    assert res["agent_id"] == "19-saas-license-optimizer"
    assert res["tool_used"] == "optimize_seats"
    assert "optimize_seats" in res["seat_plan"]
