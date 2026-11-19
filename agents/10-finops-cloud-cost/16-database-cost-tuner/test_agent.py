"""100% coverage pytest suite for 16-database-cost-tuner."""

from agent import run_agent


def test_16_database_cost_tuner() -> None:
    res = run_agent({"db_usage": "3 production clusters at 18% CPU, provisioned IOPS 4x used, 9 dev databases running 24/7, backups kept 90 days"})
    assert res["agent_id"] == "16-database-cost-tuner"
    assert res["tool_used"] == "tune_db_cost"
    assert "tune_db_cost" in res["db_savings"]
