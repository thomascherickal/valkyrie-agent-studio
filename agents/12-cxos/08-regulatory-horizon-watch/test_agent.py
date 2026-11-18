"""100% coverage pytest suite for 08-regulatory-horizon-watch."""

from agent import run_agent


def test_08_regulatory_horizon_watch() -> None:
    res = run_agent({"policy_scope": "Autonomous agent audit trails & human-in"})
    assert res["agent_id"] == "08-regulatory-horizon-watch"
    assert res["tool_used"] == "map_compliance_gaps"
    assert "map_compliance_gaps" in res["regulatory_brief"]
