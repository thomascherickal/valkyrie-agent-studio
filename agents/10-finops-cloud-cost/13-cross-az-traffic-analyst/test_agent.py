"""100% coverage pytest suite for 13-cross-az-traffic-analyst."""

from agent import run_agent


def test_13_cross_az_traffic_analyst() -> None:
    res = run_agent({"traffic_matrix": "Service mesh sends 62% of traffic across zones; Kafka replication 140 TB/month; one analytics job crosses regions"})
    assert res["agent_id"] == "13-cross-az-traffic-analyst"
    assert res["tool_used"] == "analyze_az_traffic"
    assert "analyze_az_traffic" in res["az_plan"]
