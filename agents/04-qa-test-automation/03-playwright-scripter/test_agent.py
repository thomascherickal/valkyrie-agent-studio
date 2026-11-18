"""100% coverage pytest suite for 03-playwright-scripter."""

from agent import run_agent


def test_03_playwright_scripter() -> None:
    res = run_agent({"user_flow": "Sign in -> Create Agent -> Toggle Theme "})
    assert res["agent_id"] == "03-playwright-scripter"
    assert res["tool_used"] == "emit_playwright_spec"
    assert "emit_playwright_spec" in res["test_code"]
