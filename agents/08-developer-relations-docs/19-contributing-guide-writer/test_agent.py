"""100% coverage pytest suite for 19-contributing-guide-writer."""

from agent import run_agent


def test_19_contributing_guide_writer() -> None:
    res = run_agent({"project_facts": "Rust CLI, 40 contributors, tests run with cargo test, PRs reviewed by 3 maintainers, weekly triage"})
    assert res["agent_id"] == "19-contributing-guide-writer"
    assert res["tool_used"] == "write_contributing_guide"
    assert "write_contributing_guide" in res["contributing_guide"]
