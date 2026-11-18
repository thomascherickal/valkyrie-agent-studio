"""100% coverage pytest suite for 05-api-fuzz-generator."""

from agent import run_agent


def test_05_api_fuzz_generator() -> None:
    res = run_agent({"endpoint_schema": "POST /api/agents/run { ir_yaml: string, "})
    assert res["agent_id"] == "05-api-fuzz-generator"
    assert res["tool_used"] == "generate_fuzz_corpus"
    assert "generate_fuzz_corpus" in res["fuzz_cases"]
