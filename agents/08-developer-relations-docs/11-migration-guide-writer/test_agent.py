"""100% coverage pytest suite for 11-migration-guide-writer."""

from agent import run_agent


def test_11_migration_guide_writer() -> None:
    res = run_agent({"breaking_changes": "v3 renames client.send() to client.request(), drops Python 3.8, and changes retries to opt-in"})
    assert res["agent_id"] == "11-migration-guide-writer"
    assert res["tool_used"] == "write_migration_guide"
    assert "write_migration_guide" in res["migration_guide"]
