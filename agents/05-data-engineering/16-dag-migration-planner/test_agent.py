"""100% coverage pytest suite for 16-dag-migration-planner."""

from agent import run_agent


def test_16_dag_migration_planner() -> None:
    res = run_agent({"legacy_jobs": "420 cron jobs on 6 servers, 60 with hidden dependencies, nightly batch window 5 hours, moving to Airflow"})
    assert res["agent_id"] == "16-dag-migration-planner"
    assert res["tool_used"] == "plan_dag_migration"
    assert "plan_dag_migration" in res["migration_plan"]
