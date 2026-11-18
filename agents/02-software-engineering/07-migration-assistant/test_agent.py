"""100% coverage pytest suite for 07-migration-assistant."""

from agent import run_agent


def test_07_migration_assistant() -> None:
    res = run_agent({"schema_change": "Rename users.full_name to display_name w"})
    assert res["agent_id"] == "07-migration-assistant"
    assert res["tool_used"] == "gen_expand_contract"
    assert "gen_expand_contract" in res["migration_sql"]
