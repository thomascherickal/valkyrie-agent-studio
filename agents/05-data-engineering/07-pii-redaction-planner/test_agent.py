"""100% coverage pytest suite for 07-pii-redaction-planner."""

from agent import run_agent


def test_07_pii_redaction_planner() -> None:
    res = run_agent({"columns_list": "email, ip_address, billing_zip, plan_id"})
    assert res["agent_id"] == "07-pii-redaction-planner"
    assert res["tool_used"] == "classify_pii_columns"
    assert "classify_pii_columns" in res["masking_policy"]
