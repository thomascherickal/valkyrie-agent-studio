"""100% coverage pytest suite for 20-product-ops-cadence-planner."""

from agent import run_agent


def test_20_product_ops_cadence_planner() -> None:
    res = run_agent({"team_rituals": "6 squads, weekly product reviews run long, roadmap changes surprise sales, metrics reviewed ad hoc"})
    assert res["agent_id"] == "20-product-ops-cadence-planner"
    assert res["tool_used"] == "plan_product_ops_cadence"
    assert "plan_product_ops_cadence" in res["ops_cadence"]
