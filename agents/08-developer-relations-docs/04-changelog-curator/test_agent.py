"""100% coverage pytest suite for 04-changelog-curator."""

from agent import run_agent


def test_04_changelog_curator() -> None:
    res = run_agent({"release_diff": "Moved from web-only UI to standalone Ele"})
    assert res["agent_id"] == "04-changelog-curator"
    assert res["tool_used"] == "curate_dev_changelog"
    assert "curate_dev_changelog" in res["changelog_md"]
