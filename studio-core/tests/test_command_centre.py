"""Tests for CommandCentre lifecycle, visual traces, and admin actions."""

from valkyrie.command_centre import CommandCentre


def test_command_centre_lifecycle_and_admin() -> None:
    cc = CommandCentre()
    t1 = cc.start_agent("01-prd-architect")
    assert t1.state == "running"
    assert "running" in t1.steps

    t2 = cc.start_agent("02-pr-code-reviewer")
    assert len(cc.list_traces()) == 2

    cc.stop_agent("01-prd-architect")
    assert t1.state == "stopped"

    # Admin stop all remaining running agents
    stopped_count = cc.admin_stop_all()
    assert stopped_count == 1
    assert t2.state == "stopped"

