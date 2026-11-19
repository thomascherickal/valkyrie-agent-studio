"""100% coverage pytest suite for 15-devrel-metrics-reporter."""

from agent import run_agent


def test_15_devrel_metrics_reporter() -> None:
    res = run_agent({"community_stats": "Docs visits 180k, new API keys 2.1k, 38% reach first call, Discord 6.4k members, 14 talks given"})
    assert res["agent_id"] == "15-devrel-metrics-reporter"
    assert res["tool_used"] == "report_devrel_metrics"
    assert "report_devrel_metrics" in res["devrel_report"]
