"""100% coverage pytest suite for 10-status-page-updater."""

from agent import run_agent


def test_10_status_page_updater() -> None:
    res = run_agent({"incident_state": "Investigating elevated latency on US-Wes"})
    assert res["agent_id"] == "10-status-page-updater"
    assert res["tool_used"] == "draft_status_update"
    assert "draft_status_update" in res["status_message"]
