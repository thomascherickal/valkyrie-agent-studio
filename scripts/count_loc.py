"""Count source files and lines by language. Usage: count_loc.py [REV]  (no REV: the working tree, tracked + untracked)."""

import subprocess
import sys
from collections import Counter
from pathlib import Path

LANG = {".py": "Python", ".ts": "TypeScript (`.ts`/`.tsx`)", ".tsx": "TypeScript (`.ts`/`.tsx`)", ".rs": "Rust", ".yaml": "YAML",
        ".yml": "YAML", ".md": "Markdown", ".toml": "TOML", ".css": "CSS", ".json": "JSON", ".svg": "SVG", ".html": "HTML"}
rev = sys.argv[1] if len(sys.argv) > 1 else None


def git(*a: str) -> bytes:
    return subprocess.run(["git", *a], capture_output=True, check=True).stdout


if rev:
    names = git("ls-tree", "-r", "--name-only", rev).decode().splitlines()
    read = lambda n: git("show", f"{rev}:{n}")
else:
    names = sorted(set(git("ls-files").decode().splitlines()) | set(git("ls-files", "-o", "--exclude-standard").decode().splitlines()))
    read = lambda n: Path(n).read_bytes()

files, lines = Counter(), Counter()
for n in names:
    ext = Path(n).suffix
    if ext not in LANG or n.endswith("package-lock.json") or not (rev or Path(n).exists()):
        continue
    data = read(n)
    files[LANG[ext]] += 1
    lines[LANG[ext]] += data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
for lang, c in sorted(files.items(), key=lambda kv: -lines[kv[0]]):
    print(f"| {lang} | {c:,} | {lines[lang]:,} |")
print(f"| **Total** | **{sum(files.values()):,}** | **{sum(lines.values()):,}** |")
