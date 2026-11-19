"""100% coverage pytest suite for 18-idempotency-reviewer."""

from agent import run_agent


def test_18_idempotency_reviewer() -> None:
    res = run_agent({"endpoint_spec": "POST /payments creates a charge; mobile app retries on timeout; webhook consumer processes events"})
    assert res["agent_id"] == "18-idempotency-reviewer"
    assert res["tool_used"] == "check_idempotency"
    assert "check_idempotency" in res["idempotency_review"]
