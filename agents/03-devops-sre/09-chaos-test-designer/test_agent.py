"""100% coverage pytest suite for 09-chaos-test-designer."""

from agent import run_agent


def test_09_chaos_test_designer() -> None:
    res = run_agent({"target_service": "Payment gateway failover to secondary re"})
    assert res["agent_id"] == "09-chaos-test-designer"
    assert res["tool_used"] == "design_chaos_drill"
    assert "design_chaos_drill" in res["chaos_spec"]
