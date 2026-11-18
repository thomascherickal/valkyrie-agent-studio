"""100% coverage pytest suite for 10-exec-kpi-narrator."""

from agent import run_agent


def test_10_exec_kpi_narrator() -> None:
    res = run_agent({"kpi_table": "WAU +14% WoW, Free-to-Paid 4.8%, Median "})
    assert res["agent_id"] == "10-exec-kpi-narrator"
    assert res["tool_used"] == "narrate_weekly_kpis"
    assert "narrate_weekly_kpis" in res["kpi_memo"]
