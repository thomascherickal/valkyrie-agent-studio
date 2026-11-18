"""100% coverage pytest suite for 05-sla-breach-predictor."""

from agent import run_agent


def test_05_sla_breach_predictor() -> None:
    res = run_agent({"queue_snapshot": "Ticket #8821: Enterprise P1, unassigned "})
    assert res["agent_id"] == "05-sla-breach-predictor"
    assert res["tool_used"] == "score_sla_risk"
    assert "score_sla_risk" in res["escalation_alerts"]
