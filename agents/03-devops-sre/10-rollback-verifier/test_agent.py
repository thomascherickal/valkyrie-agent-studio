"""100% coverage pytest suite for 10-rollback-verifier."""

from agent import run_agent


def test_10_rollback_verifier() -> None:
    res = run_agent({"canary_stats": "Canary p99: 420ms vs Baseline p99: 95ms"})
    assert res["agent_id"] == "10-rollback-verifier"
    assert res["tool_used"] == "eval_canary_gate"
    assert "eval_canary_gate" in res["rollback_action"]
