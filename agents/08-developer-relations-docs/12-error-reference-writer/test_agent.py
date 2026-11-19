"""100% coverage pytest suite for 12-error-reference-writer."""

from agent import run_agent


def test_12_error_reference_writer() -> None:
    res = run_agent({"error_catalog": "E1042 rate_limit_exceeded: 429 when more than 600 requests per minute; E2001 invalid_signature: webhook hash mismatch"})
    assert res["agent_id"] == "12-error-reference-writer"
    assert res["tool_used"] == "write_error_reference"
    assert "write_error_reference" in res["error_reference"]
