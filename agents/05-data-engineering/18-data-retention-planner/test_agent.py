"""100% coverage pytest suite for 18-data-retention-planner."""

from agent import run_agent


def test_18_data_retention_planner() -> None:
    res = run_agent({"dataset_catalog": "Clickstream 80 TB/yr kept forever, invoices 7 yrs required, support chats with personal data kept forever"})
    assert res["agent_id"] == "18-data-retention-planner"
    assert res["tool_used"] == "plan_retention"
    assert "plan_retention" in res["retention_plan"]
