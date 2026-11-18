"""100% coverage pytest suite for 04-flaky-test-triager."""

from agent import run_agent


def test_04_flaky_test_triager() -> None:
    res = run_agent({"failure_logs": "Timeout waiting for modal backdrop; fail"})
    assert res["agent_id"] == "04-flaky-test-triager"
    assert res["tool_used"] == "classify_flakiness"
    assert "classify_flakiness" in res["triage_report"]
