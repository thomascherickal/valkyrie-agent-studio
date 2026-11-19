"""100% coverage pytest suite for 17-deploy-freeze-advisor."""

from agent import run_agent


def test_17_deploy_freeze_advisor() -> None:
    res = run_agent({"change_calendar": "Black Friday week, 31 changes queued, error budget 38% left, two incidents last week"})
    assert res["agent_id"] == "17-deploy-freeze-advisor"
    assert res["tool_used"] == "decide_freeze"
    assert "decide_freeze" in res["freeze_decision"]
