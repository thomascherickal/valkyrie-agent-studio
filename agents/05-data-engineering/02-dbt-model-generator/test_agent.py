"""100% coverage pytest suite for 02-dbt-model-generator."""

from agent import run_agent


def test_02_dbt_model_generator() -> None:
    res = run_agent({"table_contract": "stg_orders(order_id, customer_id, total_"})
    assert res["agent_id"] == "02-dbt-model-generator"
    assert res["tool_used"] == "emit_dbt_model"
    assert "emit_dbt_model" in res["dbt_files"]
