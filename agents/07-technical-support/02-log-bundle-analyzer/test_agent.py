"""100% coverage pytest suite for 02-log-bundle-analyzer."""

from agent import run_agent


def test_02_log_bundle_analyzer() -> None:
    res = run_agent({"log_excerpt": "2026-11-18T10:12Z ERROR ConnectionResetE"})
    assert res["agent_id"] == "02-log-bundle-analyzer"
    assert res["tool_used"] == "extract_root_exception"
    assert "extract_root_exception" in res["diagnostic_summary"]
