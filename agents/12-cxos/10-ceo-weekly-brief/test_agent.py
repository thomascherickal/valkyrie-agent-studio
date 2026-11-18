"""100% coverage pytest suite for 10-ceo-weekly-brief."""

from agent import run_agent


def test_10_ceo_weekly_brief() -> None:
    res = run_agent({"exec_inputs": "Pipeline $1.4M, Uptime 99.98%, 2 senior "})
    assert res["agent_id"] == "10-ceo-weekly-brief"
    assert res["tool_used"] == "compile_ceo_brief"
    assert "compile_ceo_brief" in res["weekly_brief_md"]
