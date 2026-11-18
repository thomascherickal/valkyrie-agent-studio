"""100% coverage pytest suite for 09-release-notes-writer."""

from agent import run_agent


def test_09_release_notes_writer() -> None:
    res = run_agent({"pr_log": "feat: add Rust transpiler; fix: OAuth to"})
    assert res["agent_id"] == "09-release-notes-writer"
    assert res["tool_used"] == "format_changelog"
    assert "format_changelog" in res["release_notes"]
