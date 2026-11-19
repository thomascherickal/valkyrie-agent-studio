"""100% coverage pytest suite for 12-ltv-cac-modeler."""

from agent import run_agent


def test_12_ltv_cac_modeler() -> None:
    res = run_agent({"unit_inputs": "ARPA 120 per month, gross margin 78%, monthly churn 2.5%, CAC 1,400 blended, 9 months payback goal"})
    assert res["agent_id"] == "12-ltv-cac-modeler"
    assert res["tool_used"] == "model_ltv_cac"
    assert "model_ltv_cac" in res["ltv_cac_readout"]
