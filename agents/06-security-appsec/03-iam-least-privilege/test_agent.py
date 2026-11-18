"""100% coverage pytest suite for 03-iam-least-privilege."""

from agent import run_agent


def test_03_iam_least_privilege() -> None:
    res = run_agent({"iam_policy": "Action: s3:*, Resource: * for analytics-"})
    assert res["agent_id"] == "03-iam-least-privilege"
    assert res["tool_used"] == "narrow_iam_actions"
    assert "narrow_iam_actions" in res["scoped_policy"]
