"""100% coverage pytest suite for 17-observability-cost-reducer."""

from agent import run_agent


def test_17_observability_cost_reducer() -> None:
    res = run_agent({"telemetry_volumes": "Logs 38 TB/month, 2.4M active metric series (40% unused), traces sampled at 100%, vendor bill 96k a month"})
    assert res["agent_id"] == "17-observability-cost-reducer"
    assert res["tool_used"] == "trim_telemetry_cost"
    assert "trim_telemetry_cost" in res["telemetry_plan"]
