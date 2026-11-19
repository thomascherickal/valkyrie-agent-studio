"""100% coverage pytest suite for 14-dedup-strategy-designer."""

from agent import run_agent


def test_14_dedup_strategy_designer() -> None:
    res = run_agent({"duplicate_report": "Events table: 3.4% duplicate event_ids from client retries; customers: 11% near-duplicate names and emails"})
    assert res["agent_id"] == "14-dedup-strategy-designer"
    assert res["tool_used"] == "design_dedup"
    assert "design_dedup" in res["dedup_plan"]
