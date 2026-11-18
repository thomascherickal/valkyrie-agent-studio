"""100% coverage pytest suite for 04-competitive-intel."""

from agent import run_agent


def test_04_competitive_intel() -> None:
    res = run_agent({"competitor_notes": "Competitor X launched usage-based meteri"})
    assert res["agent_id"] == "04-competitive-intel"
    assert res["tool_used"] == "diff_feature_matrix"
    assert "diff_feature_matrix" in res["matrix_summary"]
