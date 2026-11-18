"""100% coverage pytest suite for 04-secret-leak-scanner."""

from agent import run_agent


def test_04_secret_leak_scanner() -> None:
    res = run_agent({"diff_text": "GEMINI_API_KEY=AIzaSyDummyExampleToken12"})
    assert res["agent_id"] == "04-secret-leak-scanner"
    assert res["tool_used"] == "scan_secret_patterns"
    assert "scan_secret_patterns" in res["leak_alert"]
