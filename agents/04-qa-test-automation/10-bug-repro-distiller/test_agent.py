"""100% coverage pytest suite for 10-bug-repro-distiller."""

from agent import run_agent


def test_10_bug_repro_distiller() -> None:
    res = run_agent({"bug_thread": "App crashes when switching from dark mod"})
    assert res["agent_id"] == "10-bug-repro-distiller"
    assert res["tool_used"] == "distill_min_repro"
    assert "distill_min_repro" in res["repro_steps"]
