"""100% coverage pytest suite for 06-investor-update-writer."""

from agent import run_agent


def test_06_investor_update_writer() -> None:
    res = run_agent({"monthly_highlights": "Launched Valkyrie 120-agent studio; seek"})
    assert res["agent_id"] == "06-investor-update-writer"
    assert res["tool_used"] == "format_investor_email"
    assert "format_investor_email" in res["investor_update"]
