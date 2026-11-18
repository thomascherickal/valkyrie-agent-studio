"""100% coverage pytest suite for 02-k8s-rightsizing-advisor."""

from agent import run_agent


def test_02_k8s_rightsizing_advisor() -> None:
    res = run_agent({"pod_metrics": "worker-api requests 4 vCPU, p95 usage 0."})
    assert res["agent_id"] == "02-k8s-rightsizing-advisor"
    assert res["tool_used"] == "compute_rightsize"
    assert "compute_rightsize" in res["rightsize_patch"]
