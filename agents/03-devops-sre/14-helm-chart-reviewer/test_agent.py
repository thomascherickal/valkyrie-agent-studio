"""100% coverage pytest suite for 14-helm-chart-reviewer."""

from agent import run_agent


def test_14_helm_chart_reviewer() -> None:
    res = run_agent({"helm_values": "replicaCount: 1; image.tag: latest; resources: {}; ingress.enabled: true; no podDisruptionBudget"})
    assert res["agent_id"] == "14-helm-chart-reviewer"
    assert res["tool_used"] == "review_helm_values"
    assert "review_helm_values" in res["chart_review"]
