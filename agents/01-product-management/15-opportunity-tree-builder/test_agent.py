"""100% coverage pytest suite for 15-opportunity-tree-builder."""

from agent import run_agent


def test_15_opportunity_tree_builder() -> None:
    res = run_agent({"desired_outcome": "Outcome: raise week-4 retention from 31% to 40%; customers say setup is long and reports are hard to share"})
    assert res["agent_id"] == "15-opportunity-tree-builder"
    assert res["tool_used"] == "build_ost"
    assert "build_ost" in res["opportunity_tree"]
