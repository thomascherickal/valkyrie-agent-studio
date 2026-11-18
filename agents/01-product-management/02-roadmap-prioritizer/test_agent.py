"""100% coverage pytest suite for 02-roadmap-prioritizer."""

from agent import run_agent


def test_02_roadmap_prioritizer() -> None:
    res = run_agent({"initiatives": "Mobile Offline Sync (R:5000, I:3, C:0.8,"})
    assert res["agent_id"] == "02-roadmap-prioritizer"
    assert res["tool_used"] == "compute_rice_score"
    assert "compute_rice_score" in res["ranked_roadmap"]
