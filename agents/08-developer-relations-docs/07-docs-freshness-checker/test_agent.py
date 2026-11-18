"""100% coverage pytest suite for 07-docs-freshness-checker."""

from agent import run_agent


def test_07_docs_freshness_checker() -> None:
    res = run_agent({"docs_vs_code": "Docs say /run-agent; api_server.py expos"})
    assert res["agent_id"] == "07-docs-freshness-checker"
    assert res["tool_used"] == "detect_doc_drift"
    assert "detect_doc_drift" in res["drift_report"]
