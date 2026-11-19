"""100% coverage pytest suite for 11-contract-test-designer."""

from agent import run_agent


def test_11_contract_test_designer() -> None:
    res = run_agent({"api_contract": "Orders service consumes GET /customers/{id} (fields id, email, tier) from Customers; 3 other consumers"})
    assert res["agent_id"] == "11-contract-test-designer"
    assert res["tool_used"] == "design_contract_tests"
    assert "design_contract_tests" in res["contract_suite"]
