"""100% coverage pytest suite for 10-quarterly-roadmap-brief."""

from agent import run_agent


def test_10_quarterly_roadmap_brief() -> None:
    res = run_agent({"qbr_inputs": "Q4: 9/10 milestones on track; Rust CLI 1"})
    assert res["agent_id"] == "10-quarterly-roadmap-brief"
    assert res["tool_used"] == "format_qbr_brief"
    assert "format_qbr_brief" in res["qbr_summary"]
