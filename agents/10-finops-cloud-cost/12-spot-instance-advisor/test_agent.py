"""100% coverage pytest suite for 12-spot-instance-advisor."""

from agent import run_agent


def test_12_spot_instance_advisor() -> None:
    res = run_agent({"workload_profile": "Batch ETL 120 vCPU nightly, CI runners 60 vCPU, stateless API 200 vCPU; interruptions tolerated for batch and CI"})
    assert res["agent_id"] == "12-spot-instance-advisor"
    assert res["tool_used"] == "assess_spot_fit"
    assert "assess_spot_fit" in res["spot_plan"]
