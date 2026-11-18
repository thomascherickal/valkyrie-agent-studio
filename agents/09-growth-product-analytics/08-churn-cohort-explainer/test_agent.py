"""100% coverage pytest suite for 08-churn-cohort-explainer."""

from agent import run_agent


def test_08_churn_cohort_explainer() -> None:
    res = run_agent({"churned_accounts": "72% of churned teams never deployed a Ru"})
    assert res["agent_id"] == "08-churn-cohort-explainer"
    assert res["tool_used"] == "explain_churn_drivers"
    assert "explain_churn_drivers" in res["retention_actions"]
