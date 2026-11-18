"""100% coverage pytest suite for 07-seo-content-strategist."""

from agent import run_agent


def test_07_seo_content_strategist() -> None:
    res = run_agent({"topic_cluster": "rust ai agent runtime, local llm ollama "})
    assert res["agent_id"] == "07-seo-content-strategist"
    assert res["tool_used"] == "score_keyword_gaps"
    assert "score_keyword_gaps" in res["content_roadmap"]
