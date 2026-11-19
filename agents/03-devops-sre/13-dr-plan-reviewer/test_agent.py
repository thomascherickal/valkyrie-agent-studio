"""100% coverage pytest suite for 13-dr-plan-reviewer."""

from agent import run_agent


def test_13_dr_plan_reviewer() -> None:
    res = run_agent({"dr_plan": "Primary region us-east-1, nightly backups to the same region, restore never tested, RTO 4h, RPO 1h"})
    assert res["agent_id"] == "13-dr-plan-reviewer"
    assert res["tool_used"] == "review_dr_plan"
    assert "review_dr_plan" in res["dr_gaps"]
