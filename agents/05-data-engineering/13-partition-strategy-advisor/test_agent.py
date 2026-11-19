"""100% coverage pytest suite for 13-partition-strategy-advisor."""

from agent import run_agent


def test_13_partition_strategy_advisor() -> None:
    res = run_agent({"table_profile": "events: 6 TB, 2.1B rows, 90% of queries filter on the last 7 days and customer_id"})
    assert res["agent_id"] == "13-partition-strategy-advisor"
    assert res["tool_used"] == "choose_partitioning"
    assert "choose_partitioning" in res["partition_plan"]
