"""100% coverage pytest suite for 03-schema-drift-detector."""

from agent import run_agent


def test_03_schema_drift_detector() -> None:
    res = run_agent({"schema_diff": "Removed column: user_tier; Added: plan_c"})
    assert res["agent_id"] == "03-schema-drift-detector"
    assert res["tool_used"] == "analyze_schema_drift"
    assert "analyze_schema_drift" in res["drift_alert"]
