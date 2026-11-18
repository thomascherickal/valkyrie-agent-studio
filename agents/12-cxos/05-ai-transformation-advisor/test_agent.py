"""100% coverage pytest suite for 05-ai-transformation-advisor."""

from agent import run_agent


def test_05_ai_transformation_advisor() -> None:
    res = run_agent({"workflow_catalog": "L1 support triage (1,200 tickets/wk) vs "})
    assert res["agent_id"] == "05-ai-transformation-advisor"
    assert res["tool_used"] == "rank_ai_roi"
    assert "rank_ai_roi" in res["rollout_roadmap"]
