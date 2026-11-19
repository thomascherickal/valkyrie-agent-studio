"""Tests for scripts/clean_worktrees.py."""

import importlib.util
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("clean_worktrees", ROOT / "scripts" / "clean_worktrees.py")
assert spec and spec.loader
clean = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clean)

PORCELAIN = """worktree /repo
HEAD aaa
branch refs/heads/main

worktree /repo/.claude/worktrees/gone
HEAD bbb
branch refs/heads/worktree-gone
prunable gitdir file points to non-existent location

worktree /repo/.claude/worktrees/dead
HEAD ccc
branch refs/heads/worktree-dead
locked claude session dead (pid 111 start 5)

worktree /repo/.claude/worktrees/live
HEAD ddd
branch refs/heads/worktree-live
locked claude session live (pid 222 start 6)

worktree /repo/.claude/worktrees/plain
HEAD eee
detached
locked
"""


def test_parse_reads_paths_branches_locks_and_prunable() -> None:
    entries = clean.parse(PORCELAIN)
    assert [e["path"].rsplit("/", 1)[-1] for e in entries] == ["repo", "gone", "dead", "live", "plain"]
    assert entries[0]["branch"] == "main" and "prunable" in entries[1] and entries[2]["locked"].startswith("claude session dead")
    assert "branch" not in entries[4] and entries[4]["locked"] == ""


def test_only_locks_of_ended_sessions_with_a_missing_folder_are_stale() -> None:
    entries = clean.parse(PORCELAIN)
    nowhere = lambda path: False  # noqa: E731
    assert clean.dead_session_locks(entries, lambda pid: pid == 222, nowhere) == ["/repo/.claude/worktrees/dead"]
    assert clean.dead_session_locks(entries, lambda pid: True, nowhere) == []
    assert clean.dead_session_locks(entries, lambda pid: False, lambda path: True) == []  # the folder is there: in use, not stale
    assert clean.dead_session_locks([{"path": str(ROOT), "locked": "claude session x (pid 1 start 2)"}], lambda pid: False) == []  # real folder check


def test_alive_tells_a_running_process_from_an_ended_one(monkeypatch: pytest.MonkeyPatch) -> None:
    assert clean.alive(os.getpid()) is True
    monkeypatch.setattr(os, "kill", lambda pid, sig: (_ for _ in ()).throw(ProcessLookupError()))
    assert clean.alive(999999) is False
    monkeypatch.setattr(os, "kill", lambda pid, sig: (_ for _ in ()).throw(PermissionError()))
    assert clean.alive(1) is True  # a process we may not signal is still running
    monkeypatch.setattr(os, "name", "nt")
    assert clean.alive(1) is True  # where it cannot be checked, nothing is removed


def test_branches_checked_out_anywhere_and_main_are_never_deleted() -> None:
    merged = "* current\n+ in-other-worktree\n  main\n  old-feature\n  kept\n\n"
    assert clean.deletable_branches(merged, {"kept"}) == ["old-feature"]


def test_main_dry_run_changes_nothing_and_a_real_run_prunes_and_deletes(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    calls: list[tuple[str, ...]] = []

    def fake_git(*args: str) -> str:
        calls.append(args)
        if args[:2] == ("worktree", "list"):
            return PORCELAIN
        return "  old-feature\n  main\n" if args[0] == "branch" and args[1] == "--merged" else ""

    monkeypatch.setattr(clean, "git", fake_git)
    monkeypatch.setattr(clean, "alive", lambda pid: pid == 222)
    monkeypatch.setattr(Path, "exists", lambda self: False)
    assert clean.main(["--dry-run"]) == 0
    assert all(c[0] in ("fetch", "worktree", "branch") for c in calls) and ("worktree", "prune") not in calls and ("branch", "-d", "old-feature") not in calls
    out = capsys.readouterr().out
    assert "locked by ended sessions: 1" in out and "stale worktrees to prune: 2" in out and "delete old-feature" in out
    calls.clear()
    assert clean.main([]) == 0
    assert ("worktree", "unlock", "/repo/.claude/worktrees/dead") in calls and ("worktree", "prune") in calls and ("branch", "-d", "old-feature") in calls
