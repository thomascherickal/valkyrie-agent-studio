"""100% coverage pytest suite for 04-k8s-manifest-linter."""

from agent import run_agent


def test_04_k8s_manifest_linter() -> None:
    res = run_agent({"k8s_yaml": "kind: Deployment, replicas: 3, resources"})
    assert res["agent_id"] == "04-k8s-manifest-linter"
    assert res["tool_used"] == "lint_k8s_spec"
    assert "lint_k8s_spec" in res["lint_findings"]
