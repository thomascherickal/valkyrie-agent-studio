"""100% coverage pytest suite for 08-runbook-generator."""

from agent import run_agent


def test_08_runbook_generator() -> None:
    res = run_agent({"alert_rule": "HighPostgresConnections > 85% for 5m"})
    assert res["agent_id"] == "08-runbook-generator"
    assert res["tool_used"] == "compile_runbook"
    assert "compile_runbook" in res["runbook_md"]
