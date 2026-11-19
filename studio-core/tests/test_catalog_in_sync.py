"""The agents/ folders and the studio-ui catalog list the same agents, so a new agent cannot be left out of either."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PER_ROLE = 20


def test_the_ui_catalog_matches_the_agent_folders() -> None:
    role_dirs = sorted(p for p in (ROOT / "agents").iterdir() if p.is_dir())
    assert len(role_dirs) == 12
    for number, role_dir in enumerate(role_dirs, start=1):
        ts = (ROOT / "studio-ui" / "src" / "data" / "roles" / f"role{number:02d}.ts").read_text()
        ids = re.findall(r'^\s{6}"id": "([^"]+)"', ts, re.M)
        folders = sorted(p.name for p in role_dir.iterdir() if p.is_dir())
        assert ids == folders and len(ids) == PER_ROLE, role_dir.name
        assert re.search(rf'^  "id": "{re.escape(role_dir.name)}"', ts, re.M)
        role_md = (role_dir / "ROLE.md").read_text()
        assert f"suite of {PER_ROLE} focused" in role_md and all(f"`{i}`" in role_md for i in ids), role_dir.name
