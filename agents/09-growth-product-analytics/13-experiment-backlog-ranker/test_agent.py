"""100% coverage pytest suite for 13-experiment-backlog-ranker."""

from agent import run_agent


def test_13_experiment_backlog_ranker() -> None:
    res = run_agent({"experiment_ideas": "Ideas: shorter signup form, annual plan banner, onboarding checklist, referral prompt; 40k visitors a week"})
    assert res["agent_id"] == "13-experiment-backlog-ranker"
    assert res["tool_used"] == "rank_experiments"
    assert "rank_experiments" in res["ranked_backlog"]
