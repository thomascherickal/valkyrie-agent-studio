"""100% coverage pytest suite for 12-test-data-synthesizer."""

from agent import run_agent


def test_12_test_data_synthesizer() -> None:
    res = run_agent({"schema_rules": "users(id, email unique, country, plan), orders(user_id FK, amount > 0); production has 2M users, 9M orders"})
    assert res["agent_id"] == "12-test-data-synthesizer"
    assert res["tool_used"] == "synthesize_test_data"
    assert "synthesize_test_data" in res["data_plan"]
