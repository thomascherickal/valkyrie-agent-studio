"""100% coverage pytest suite for 16-blast-radius-mapper."""

from agent import run_agent


def test_16_blast_radius_mapper() -> None:
    res = run_agent({"service_map": "auth-service is called by 14 services; 6 have no cache or fallback; it runs in one region"})
    assert res["agent_id"] == "16-blast-radius-mapper"
    assert res["tool_used"] == "map_blast_radius"
    assert "map_blast_radius" in res["outage_map"]
