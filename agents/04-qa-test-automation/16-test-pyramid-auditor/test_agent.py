"""100% coverage pytest suite for 16-test-pyramid-auditor."""

from agent import run_agent


def test_16_test_pyramid_auditor() -> None:
    res = run_agent({"test_counts": "Unit 1,800 (3 min), integration 240 (14 min), end-to-end 160 (52 min, 9% flaky)"})
    assert res["agent_id"] == "16-test-pyramid-auditor"
    assert res["tool_used"] == "audit_test_pyramid"
    assert "audit_test_pyramid" in res["pyramid_report"]
