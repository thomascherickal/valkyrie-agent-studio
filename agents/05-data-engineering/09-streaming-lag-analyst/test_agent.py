"""100% coverage pytest suite for 09-streaming-lag-analyst."""

from agent import run_agent


def test_09_streaming_lag_analyst() -> None:
    res = run_agent({"consumer_metrics": "Partition 3 lag: 450k msgs; Partitions 0"})
    assert res["agent_id"] == "09-streaming-lag-analyst"
    assert res["tool_used"] == "diagnose_partition_skew"
    assert "diagnose_partition_skew" in res["lag_remediation"]
