"""100% coverage pytest suite for 09-team-health-pulse."""

from agent import run_agent


def test_09_team_health_pulse() -> None:
    res = run_agent({"dora_snapshot": "Deploy freq: daily, Lead time: 3h, CFR: "})
    assert res["agent_id"] == "09-team-health-pulse"
    assert res["tool_used"] == "evaluate_dora_tier"
    assert "evaluate_dora_tier" in res["health_report"]
