"""100% coverage pytest suite for 03-okr-alignment-checker."""

from agent import run_agent


def test_03_okr_alignment_checker() -> None:
    res = run_agent({"epics_vs_okrs": "Epic: Custom dark theme; OKR1: Cut p99 l"})
    assert res["agent_id"] == "03-okr-alignment-checker"
    assert res["tool_used"] == "score_okr_fit"
    assert "score_okr_fit" in res["alignment_report"]
