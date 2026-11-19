"""100% coverage pytest suite for 15-scd-modeler."""

from agent import run_agent


def test_15_scd_modeler() -> None:
    res = run_agent({"dimension_changes": "Customer tier changes ~8% of customers a month; reports need revenue by the tier at the time of sale"})
    assert res["agent_id"] == "15-scd-modeler"
    assert res["tool_used"] == "model_scd"
    assert "model_scd" in res["scd_design"]
