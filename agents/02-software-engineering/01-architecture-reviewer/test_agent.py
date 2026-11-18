"""100% coverage pytest suite for 01-architecture-reviewer."""

from agent import run_agent


def test_01_architecture_reviewer() -> None:
    res = run_agent({"rfc_summary": "Event-driven billing worker consuming Ka"})
    assert res["agent_id"] == "01-architecture-reviewer"
    assert res["tool_used"] == "check_failure_modes"
    assert "check_failure_modes" in res["review_findings"]
