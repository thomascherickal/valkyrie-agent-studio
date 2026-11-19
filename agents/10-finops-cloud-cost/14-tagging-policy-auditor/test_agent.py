"""100% coverage pytest suite for 14-tagging-policy-auditor."""

from agent import run_agent


def test_14_tagging_policy_auditor() -> None:
    res = run_agent({"resource_tags": "12,400 resources: 71% have owner, 58% have cost-center, 9 spellings of environment, 3.1k untagged by spend"})
    assert res["agent_id"] == "14-tagging-policy-auditor"
    assert res["tool_used"] == "audit_tags"
    assert "audit_tags" in res["tag_report"]
