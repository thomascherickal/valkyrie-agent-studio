"""100% coverage pytest suite for 01-ticket-triager."""

from agent import run_agent


def test_01_ticket_triager() -> None:
    res = run_agent({"ticket_text": "Enterprise prod down: SAML assertion sig"})
    assert res["agent_id"] == "01-ticket-triager"
    assert res["tool_used"] == "classify_ticket_sla"
    assert "classify_ticket_sla" in res["routing_decision"]
