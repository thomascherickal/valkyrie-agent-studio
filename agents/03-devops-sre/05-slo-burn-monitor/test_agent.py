"""100% coverage pytest suite for 05-slo-burn-monitor."""

from agent import run_agent


def test_05_slo_burn_monitor() -> None:
    res = run_agent({"sli_metrics": "SLO: 99.9%, 1h error rate: 1.2%, remaini"})
    assert res["agent_id"] == "05-slo-burn-monitor"
    assert res["tool_used"] == "calc_burn_rate"
    assert "calc_burn_rate" in res["paging_decision"]
