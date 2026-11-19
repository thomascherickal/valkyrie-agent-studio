"""100% coverage pytest suite for 12-data-contract-author."""

from agent import run_agent


def test_12_data_contract_author() -> None:
    res = run_agent({"dataset_spec": "orders_daily: one row per order, order_id unique, amount in cents, refreshed by 06:00 UTC, owner Payments"})
    assert res["agent_id"] == "12-data-contract-author"
    assert res["tool_used"] == "draft_data_contract"
    assert "draft_data_contract" in res["contract_doc"]
