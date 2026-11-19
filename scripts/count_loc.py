"""Count source files and lines by language, as the Markdown table METRICS.md holds.

Usage: python3 scripts/count_loc.py [REV]   (no REV: the working tree, tracked and untracked files)
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]  # git is always asked from here, so the cwd does not matter
LANG = {".py": "Python", ".ts": "TypeScript (`.ts`/`.tsx`)", ".tsx": "TypeScript (`.ts`/`.tsx`)", ".rs": "Rust", ".yaml": "YAML",
        ".yml": "YAML", ".md": "Markdown", ".toml": "TOML", ".css": "CSS", ".json": "JSON", ".svg": "SVG", ".html": "HTML"}


def _git(*args: str) -> bytes:
    return subprocess.run(["git", *args], capture_output=True, check=True, cwd=ROOT).stdout


def table(rev: str | None = None) -> str:
    """The summary table rows, most lines first, ending with the total row."""
    if rev:
        names = _git("ls-tree", "-r", "--name-only", rev).decode().splitlines()
        read = lambda name: _git("show", f"{rev}:{name}")  # noqa: E731
    else:
        names = sorted(set(_git("ls-files").decode().splitlines()) | set(_git("ls-files", "-o", "--exclude-standard").decode().splitlines()))
        read = lambda name: (ROOT / name).read_bytes()  # noqa: E731
    files: Counter[str] = Counter()
    lines: Counter[str] = Counter()
    for name in names:
        ext = Path(name).suffix
        if ext not in LANG or name.endswith("package-lock.json") or not (rev or (ROOT / name).exists()):
            continue
        data = read(name)
        files[LANG[ext]] += 1
        lines[LANG[ext]] += data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
    rows = [f"| {lang} | {count:,} | {lines[lang]:,} |" for lang, count in sorted(files.items(), key=lambda kv: -lines[kv[0]])]
    return "\n".join([*rows, f"| **Total** | **{sum(files.values()):,}** | **{sum(lines.values()):,}** |"])


if __name__ == "__main__":
    print(table(sys.argv[1] if len(sys.argv) > 1 else None))
