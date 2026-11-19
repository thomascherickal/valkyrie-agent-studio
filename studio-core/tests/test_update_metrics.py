"""Tests for scripts/update_metrics.py, which the git hooks run."""

import importlib.util
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("update_metrics", ROOT / "scripts" / "update_metrics.py")
assert spec and spec.loader
update_metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(update_metrics)

DOC = """# Metrics

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 1 | 10 |
| Rust | 2 | 5 |
| **Total** | **3** | **15** |

After the table.
"""
ROWS = "| Python | 9 | 90 |\n| **Total** | **9** | **90** |"


def test_replace_table_swaps_only_the_rows() -> None:
    out = update_metrics.replace_table(DOC, ROWS)
    assert "| Python | 9 | 90 |" in out and "| Rust |" not in out and out.endswith("\n\nAfter the table.\n")
    assert out.startswith("# Metrics\n\n| Language | Source Files | Total Lines |\n| :--- | ---: | ---: |\n")
    assert update_metrics.replace_table(out, ROWS) == out  # replacing again changes nothing
    with pytest.raises(ValueError, match="no per-language table"):
        update_metrics.replace_table("nothing here", ROWS)


def test_main_rewrites_checks_and_leaves_a_current_file_alone(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(update_metrics, "table", lambda: ROWS)
    (tmp_path / "METRICS.md").write_text(DOC)
    assert update_metrics.main(["--check"], tmp_path) == 1 and "out of date" in capsys.readouterr().out
    assert (tmp_path / "METRICS.md").read_text() == DOC  # --check never writes
    assert update_metrics.main([], tmp_path) == 0 and "updated" in capsys.readouterr().out
    assert "| Python | 9 | 90 |" in (tmp_path / "METRICS.md").read_text()
    assert update_metrics.main(["--check"], tmp_path) == 0 and update_metrics.main([], tmp_path) == 0
    assert capsys.readouterr().out == ""


def test_the_repo_metrics_file_has_a_table_the_script_can_update() -> None:
    assert update_metrics.TABLE.search((ROOT / "METRICS.md").read_text())


def test_count_loc_table_ends_with_a_total_row() -> None:
    import count_loc

    rows = count_loc.table("HEAD").splitlines()
    assert rows[-1].startswith("| **Total** |") and all(r.startswith("| ") for r in rows) and len(rows) > 3
