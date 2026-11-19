"""Tests for the pure parts of scripts/build_sidecar.py (what goes in the bundle, and the target name)."""

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("build_sidecar", ROOT / "scripts" / "build_sidecar.py")
assert spec and spec.loader
build_sidecar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_sidecar)


def test_only_what_the_api_reads_goes_in_the_bundle() -> None:
    keep = build_sidecar.keep
    assert keep(Path("01-product-management/01-prd-architect/agent.ir.yaml"))
    assert keep(Path("01-product-management/01-prd-architect/sample_data.json"))
    assert keep(Path("01-product-management/ROLE.md"))
    assert not keep(Path("01-product-management/01-prd-architect/rust/src/main.rs"))
    assert not keep(Path("01-product-management/01-prd-architect/test_agent.py"))
    assert not keep(Path("01-product-management/01-prd-architect/demo.svg"))
    assert not keep(Path("01-product-management/__pycache__/x.pyc"))


def test_copy_agents_copies_the_kept_files_and_counts_them(tmp_path: Path) -> None:
    source, target = tmp_path / "agents", tmp_path / "out"
    for name in ("r/a/agent.ir.yaml", "r/a/rust/Cargo.toml", "r/a/test_agent.py", "r/ROLE.md"):
        (source / name).parent.mkdir(parents=True, exist_ok=True)
        (source / name).write_text("x")
    assert build_sidecar.copy_agents(source, target) == 2
    assert sorted(p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file()) == ["r/ROLE.md", "r/a/agent.ir.yaml"]


def test_the_target_triple_comes_from_rustc() -> None:
    text = "rustc 1.90.0 (abc 2026-01-01)\nbinary: rustc\nhost: x86_64-unknown-linux-gnu\nrelease: 1.90.0\n"
    assert build_sidecar.target_triple(text) == "x86_64-unknown-linux-gnu"
    with pytest.raises(ValueError, match="host triple"):
        build_sidecar.target_triple("nothing useful")


def test_the_real_agents_folder_is_bundled_without_rust_or_tests() -> None:
    files = [p for p in (ROOT / "agents").rglob("*") if p.is_file() and build_sidecar.keep(p.relative_to(ROOT / "agents"))]
    assert len(files) > 900 and not any("rust" in p.parts or p.name == "test_agent.py" for p in files)
