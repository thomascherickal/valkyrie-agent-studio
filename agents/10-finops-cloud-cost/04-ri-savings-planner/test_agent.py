"""100% coverage pytest suite for 04-ri-savings-planner."""

from agent import run_agent


def test_04_ri_savings_planner() -> None:
    res = run_agent({"compute_baseline": "Steady 120 vCPU baseline; currently 100%"})
    assert res["agent_id"] == "04-ri-savings-planner"
    assert res["tool_used"] == "model_commitment_roi"
    assert "model_commitment_roi" in res["savings_plan"]
