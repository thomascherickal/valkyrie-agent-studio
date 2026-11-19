"""100% coverage pytest suite for 11-oncall-load-analyzer."""

from agent import run_agent


def test_11_oncall_load_analyzer() -> None:
    res = run_agent({"pager_stats": "Last 4 weeks: 212 pages, 61 outside working hours, 9 engineers in rotation, top service 74 pages"})
    assert res["agent_id"] == "11-oncall-load-analyzer"
    assert res["tool_used"] == "analyze_oncall_load"
    assert "analyze_oncall_load" in res["oncall_report"]
