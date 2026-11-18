"""100% coverage pytest suite for 10-security-advisory-writer."""

from agent import run_agent


def test_10_security_advisory_writer() -> None:
    res = run_agent({"advisory_input": "Patched path traversal in export endpoin"})
    assert res["agent_id"] == "10-security-advisory-writer"
    assert res["tool_used"] == "format_advisory_md"
    assert "format_advisory_md" in res["advisory_doc"]
