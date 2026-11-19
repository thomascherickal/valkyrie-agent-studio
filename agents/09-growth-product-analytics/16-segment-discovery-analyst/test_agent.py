"""100% coverage pytest suite for 16-segment-discovery-analyst."""

from agent import run_agent


def test_16_segment_discovery_analyst() -> None:
    res = run_agent({"usage_summary": "4 clusters by usage: heavy API users, dashboard-only viewers, occasional exporters, trial tourists"})
    assert res["agent_id"] == "16-segment-discovery-analyst"
    assert res["tool_used"] == "find_segments"
    assert "find_segments" in res["segment_findings"]
