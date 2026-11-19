"""Remove stale git worktrees and the local branches that are already merged into main.

A worktree is stale when its folder is gone: git marks it prunable, or it is locked by a Claude session whose process
has ended (a dead process alone is not enough, because a live session may not be visible as a process: the folder must be gone too).
Usage: python3 scripts/clean_worktrees.py [--dry-run]     (also: make clean-worktrees)
It never touches the worktree you run it from, the main checkout, or a branch with unmerged commits.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MAIN_BRANCH = "main"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True, cwd=ROOT).stdout


def parse(porcelain: str) -> list[dict[str, str]]:
    """The entries of `git worktree list --porcelain`: path, branch (short name), locked (reason) and prunable (reason)."""
    entries: list[dict[str, str]] = []
    for line in porcelain.splitlines():
        key, _, value = line.partition(" ")
        if key == "worktree":
            entries.append({"path": value})
        elif entries and key in ("branch", "locked", "prunable"):
            entries[-1][key] = value.removeprefix("refs/heads/")
    return entries


def alive(pid: int) -> bool:
    """True when a process with this id is running. Where that cannot be checked, assume it is."""
    if os.name != "posix":
        return True
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def dead_session_locks(entries: list[dict[str, str]], is_alive=None, exists=None) -> list[str]:
    """Paths of worktrees locked by a session whose process has ended and whose folder is gone."""
    is_alive, exists = is_alive or alive, exists or (lambda path: Path(path).exists())
    stale = []
    for entry in entries:
        found = re.search(r"pid (\d+)", entry.get("locked", ""))
        if found and not is_alive(int(found.group(1))) and not exists(entry["path"]):
            stale.append(entry["path"])
    return stale


def deletable_branches(merged: str, keep: set[str]) -> list[str]:
    """Branch names from `git branch --merged` that are safe to delete: not checked out anywhere, not main, not kept."""
    names = []
    for line in merged.splitlines():
        if line[:1] in ("*", "+"):  # checked out here or in another worktree
            continue
        name = line.strip()
        if name and name != MAIN_BRANCH and name not in keep:
            names.append(name)
    return names


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    git("fetch", "--prune", "origin")
    entries = parse(git("worktree", "list", "--porcelain"))
    unlock = dead_session_locks(entries)
    print(f"worktrees locked by ended sessions: {len(unlock)}")
    for path in unlock:
        print(f"  unlock {path}")
        if not dry:
            git("worktree", "unlock", path)
    stale = sum(1 for e in entries if "prunable" in e) + len(unlock)
    print(f"stale worktrees to prune: {stale}")
    if not dry:
        git("worktree", "prune")
    branches = deletable_branches(git("branch", "--merged", f"origin/{MAIN_BRANCH}"), set())
    print(f"merged local branches to delete: {len(branches)}")
    for name in branches:
        print(f"  delete {name}")
        if not dry:
            git("branch", "-d", name)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
