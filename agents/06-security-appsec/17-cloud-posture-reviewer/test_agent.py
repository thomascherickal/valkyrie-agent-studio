"""100% coverage pytest suite for 17-cloud-posture-reviewer."""

from agent import run_agent


def test_17_cloud_posture_reviewer() -> None:
    res = run_agent({"cloud_config": "3 public storage buckets, 14 security groups open to 0.0.0.0/0, CloudTrail off in 2 regions, root has no MFA"})
    assert res["agent_id"] == "17-cloud-posture-reviewer"
    assert res["tool_used"] == "review_cloud_posture"
    assert "review_cloud_posture" in res["posture_report"]
