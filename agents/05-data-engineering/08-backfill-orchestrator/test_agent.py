"""100% coverage pytest suite for 08-backfill-orchestrator."""

from agent import run_agent


def test_08_backfill_orchestrator() -> None:
    res = run_agent({"backfill_window": "2024-01-01 to 2026-11-01, max 4 concurre"})
    assert res["agent_id"] == "08-backfill-orchestrator"
    assert res["tool_used"] == "chunk_date_windows"
    assert "chunk_date_windows" in res["backfill_plan"]
