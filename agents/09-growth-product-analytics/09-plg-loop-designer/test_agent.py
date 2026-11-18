"""100% coverage pytest suite for 09-plg-loop-designer."""

from agent import run_agent


def test_09_plg_loop_designer() -> None:
    res = run_agent({"product_surface": "Shareable agent.ir.yaml + demo.svg previ"})
    assert res["agent_id"] == "09-plg-loop-designer"
    assert res["tool_used"] == "model_viral_k_factor"
    assert "model_viral_k_factor" in res["loop_spec"]
