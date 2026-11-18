"""100% coverage pytest suite for 04-kb-article-drafter."""

from agent import run_agent


def test_04_kb_article_drafter() -> None:
    res = run_agent({"resolution_notes": "Fixed Ollama CORS by setting OLLAMA_ORIG"})
    assert res["agent_id"] == "04-kb-article-drafter"
    assert res["tool_used"] == "format_kb_markdown"
    assert "format_kb_markdown" in res["kb_article"]
