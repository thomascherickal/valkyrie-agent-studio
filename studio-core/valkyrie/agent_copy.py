"""Copy an agent (and your edits to its Python) under a new name, as a new Custom Agent."""

from __future__ import annotations

from pathlib import Path
import re
import shutil

from valkyrie.ir_schema import dump_ir_to_yaml, load_ir_from_yaml

TEXT = {".py", ".md", ".rs", ".toml", ".json", ".yaml", ".yml", ".svg", ".txt"}
NAME_MAX = 60
ID_MAX = 40


def slug(name: str) -> str:
    """A folder-safe id from a name: lowercase letters, digits and single hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:ID_MAX].strip("-")


def _rewrite(root: Path, old_id: str, new_id: str) -> None:
    """Replace the old id (and the crate-style id with underscores) in every text file under `root`."""
    for file in root.rglob("*"):
        if file.is_file() and file.suffix in TEXT:
            text = file.read_text(encoding="utf-8")
            file.write_text(text.replace(old_id, new_id).replace(old_id.replace("-", "_"), new_id.replace("-", "_")), encoding="utf-8")


def copy_agent(source: Path, dest: Path, old_id: str, new_id: str, new_name: str) -> None:
    """Copy an agent folder to `dest` with the new id and name in its definition, code, docs and Rust crate."""
    shutil.copytree(source, dest, ignore=shutil.ignore_patterns("__pycache__", "target"))
    _rewrite(dest, old_id, new_id)
    ir_file = dest / "agent.ir.yaml"
    ir = load_ir_from_yaml(ir_file.read_text(encoding="utf-8"))
    ir_file.write_text(dump_ir_to_yaml(ir.model_copy(update={"name": new_name, "system_prompt": ir.system_prompt.replace(ir.name, new_name)})), encoding="utf-8")


def copy_edits(source: Path, dest: Path, old_id: str, new_id: str) -> bool:
    """Copy the saved edits of the Python versions. False when there were none."""
    if not source.is_dir():
        return False
    shutil.copytree(source, dest)
    _rewrite(dest, old_id, new_id)
    return True
