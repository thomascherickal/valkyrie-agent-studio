"""100% coverage pytest suite for 07-api-error-explainer."""

from agent import run_agent


def test_07_api_error_explainer() -> None:
    res = run_agent({"error_payload": "429 RESOURCE_EXHAUSTED on gemini-4-hydro"})
    assert res["agent_id"] == "07-api-error-explainer"
    assert res["tool_used"] == "explain_api_error"
    assert "explain_api_error" in res["fix_guidance"]
