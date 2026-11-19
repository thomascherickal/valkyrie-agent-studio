"""100% coverage pytest suite for 15-chargeback-allocator."""

from agent import run_agent


def test_15_chargeback_allocator() -> None:
    res = run_agent({"shared_costs": "Shared Kubernetes 84k, networking 31k, observability 52k, support 19k a month; 6 product teams"})
    assert res["agent_id"] == "15-chargeback-allocator"
    assert res["tool_used"] == "allocate_shared_cost"
    assert "allocate_shared_cost" in res["allocation_table"]
