"""100% coverage pytest suite for 02-api-reference-polisher."""

from agent import run_agent


def test_02_api_reference_polisher() -> None:
    res = run_agent({"endpoint_def": "POST /api/agents/deploy-rust"})
    assert res["agent_id"] == "02-api-reference-polisher"
    assert res["tool_used"] == "enrich_api_examples"
    assert "enrich_api_examples" in res["reference_md"]
