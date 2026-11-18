"""100% coverage pytest suite for 05-voice-of-customer."""

from agent import run_agent


def test_05_voice_of_customer() -> None:
    res = run_agent({"feedback_batch": "Export CSV times out on >50k rows; dark "})
    assert res["agent_id"] == "05-voice-of-customer"
    assert res["tool_used"] == "cluster_verbatims"
    assert "cluster_verbatims" in res["top_themes"]
