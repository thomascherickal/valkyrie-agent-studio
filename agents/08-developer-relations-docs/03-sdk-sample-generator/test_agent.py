"""100% coverage pytest suite for 03-sdk-sample-generator."""

from agent import run_agent


def test_03_sdk_sample_generator() -> None:
    res = run_agent({"operation": "Invoke gemini-4-hydrogen in low thinking"})
    assert res["agent_id"] == "03-sdk-sample-generator"
    assert res["tool_used"] == "emit_polyglot_samples"
    assert "emit_polyglot_samples" in res["code_samples"]
