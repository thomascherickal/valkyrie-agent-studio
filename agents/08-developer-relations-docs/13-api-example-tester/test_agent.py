"""100% coverage pytest suite for 13-api-example-tester."""

from agent import run_agent


def test_13_api_example_tester() -> None:
    res = run_agent({"code_examples": "140 examples in 6 languages, 31 reported broken last quarter, SDK v4 released with renamed methods"})
    assert res["agent_id"] == "13-api-example-tester"
    assert res["tool_used"] == "test_api_examples"
    assert "test_api_examples" in res["example_report"]
