"""100% coverage pytest suite for 04-api-contract-designer."""

from agent import run_agent


def test_04_api_contract_designer() -> None:
    res = run_agent({"endpoint_spec": "POST /v2/agents/{id}/deploy returning cr"})
    assert res["agent_id"] == "04-api-contract-designer"
    assert res["tool_used"] == "validate_openapi_diff"
    assert "validate_openapi_diff" in res["contract_yaml"]
