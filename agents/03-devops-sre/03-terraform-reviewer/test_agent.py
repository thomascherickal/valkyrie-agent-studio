"""100% coverage pytest suite for 03-terraform-reviewer."""

from agent import run_agent


def test_03_terraform_reviewer() -> None:
    res = run_agent({"tf_plan_diff": "+/- aws_rds_cluster.main (forces replace"})
    assert res["agent_id"] == "03-terraform-reviewer"
    assert res["tool_used"] == "inspect_tf_blast"
    assert "inspect_tf_blast" in res["tf_verdict"]
