"""100% coverage pytest suite for 09-concurrency-debugger."""

from agent import run_agent


def test_09_concurrency_debugger() -> None:
    res = run_agent({"async_trace": "Task A holds lock1->lock2 while Task B h"})
    assert res["agent_id"] == "09-concurrency-debugger"
    assert res["tool_used"] == "analyze_lock_graph"
    assert "analyze_lock_graph" in res["deadlock_report"]
