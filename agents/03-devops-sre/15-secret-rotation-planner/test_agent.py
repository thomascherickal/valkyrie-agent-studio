"""100% coverage pytest suite for 15-secret-rotation-planner."""

from agent import run_agent


def test_15_secret_rotation_planner() -> None:
    res = run_agent({"secret_inventory": "86 secrets: 23 older than 1 year, 9 shared by several services, 14 database passwords, no owner on 11"})
    assert res["agent_id"] == "15-secret-rotation-planner"
    assert res["tool_used"] == "plan_secret_rotation"
    assert "plan_secret_rotation" in res["rotation_plan"]
