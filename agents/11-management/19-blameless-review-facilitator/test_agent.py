"""100% coverage pytest suite for 19-blameless-review-facilitator."""

from agent import run_agent


def test_19_blameless_review_facilitator() -> None:
    res = run_agent({"incident_timeline": "Checkout down 47 minutes after a config push at 14:05; rollback delayed by missing runbook; alert fired 9 minutes late"})
    assert res["agent_id"] == "19-blameless-review-facilitator"
    assert res["tool_used"] == "run_blameless_review"
    assert "run_blameless_review" in res["review_agenda"]
