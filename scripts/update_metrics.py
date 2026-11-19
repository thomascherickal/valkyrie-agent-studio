"""Keep the per-language table in METRICS.md equal to the real counts. Run by the git hooks.

Usage: python3 scripts/update_metrics.py          rewrite the table if it is out of date
       python3 scripts/update_metrics.py --check  change nothing, exit 1 if it is out of date
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from count_loc import table  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
# The header and separator rows, then every row up to and including the total row.
TABLE = re.compile(r"(\| Language \| Source Files \| Total Lines \|\n\| :--- \| ---: \| ---: \|\n)(?:\|[^\n]*\n)*?\| \*\*Total\*\*[^\n]*")


def replace_table(text: str, rows: str) -> str:
    """`text` with the summary table's rows replaced by `rows`. Raises ValueError if the table is missing."""
    if not TABLE.search(text):
        raise ValueError("METRICS.md has no per-language table to update")
    return TABLE.sub(lambda found: found.group(1) + rows, text, count=1)


def main(argv: list[str], root: Path = ROOT) -> int:
    path = root / "METRICS.md"
    current = path.read_text()
    fresh = replace_table(current, table())
    if fresh == current:
        return 0
    if "--check" in argv:
        print("METRICS.md is out of date: run `make metrics` (or python3 scripts/update_metrics.py) and commit it.")
        return 1
    path.write_text(fresh)
    print("METRICS.md updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
