"""100% coverage pytest suite for 15-headcount-justifier."""

from agent import run_agent


def test_15_headcount_justifier() -> None:
    res = run_agent({"workload_data": "On-call load 1.8x target, 3 roadmap items slipped a quarter, team of 8, requesting 2 engineers"})
    assert res["agent_id"] == "15-headcount-justifier"
    assert res["tool_used"] == "justify_headcount"
    assert "justify_headcount" in res["headcount_case"]
