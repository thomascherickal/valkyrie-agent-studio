"""100% coverage pytest suite for 18-sample-app-reviewer."""

from agent import run_agent


def test_18_sample_app_reviewer() -> None:
    res = run_agent({"sample_readme": "README: clone, npm install, add .env with API key, npm start; hard-coded test key in config.js; no tests"})
    assert res["agent_id"] == "18-sample-app-reviewer"
    assert res["tool_used"] == "review_sample_app"
    assert "review_sample_app" in res["sample_review"]
