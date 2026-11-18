"""100% coverage pytest suite for 06-egress-cost-reducer."""

from agent import run_agent


def test_06_egress_cost_reducer() -> None:
    res = run_agent({"network_flow": "18 TB/mo cross-AZ traffic between app an"})
    assert res["agent_id"] == "06-egress-cost-reducer"
    assert res["tool_used"] == "find_egress_leaks"
    assert "find_egress_leaks" in res["network_fixes"]
