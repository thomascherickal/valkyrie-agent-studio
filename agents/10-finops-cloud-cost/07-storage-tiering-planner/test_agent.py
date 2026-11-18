"""100% coverage pytest suite for 07-storage-tiering-planner."""

from agent import run_agent


def test_07_storage_tiering_planner() -> None:
    res = run_agent({"bucket_stats": "45 TB logs older than 90 days stored in "})
    assert res["agent_id"] == "07-storage-tiering-planner"
    assert res["tool_used"] == "design_lifecycle_rule"
    assert "design_lifecycle_rule" in res["storage_savings"]
