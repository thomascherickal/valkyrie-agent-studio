"""The project icon lives in assets/. The web favicon and the Tauri app icon must be copies of it."""

import json
from pathlib import Path
import struct

REPO = Path(__file__).resolve().parents[2]
ICON = REPO / "assets" / "valkyrie-studio-icon.png"
COPIES = {
    "web favicon": REPO / "studio-ui" / "public" / "favicon.png",
    "Tauri app icon": REPO / "studio-ui" / "src-tauri" / "icons" / "icon.png",
}


def test_the_icon_is_a_square_png() -> None:
    data = ICON.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n"
    width, height = struct.unpack(">II", data[16:24])
    assert width == height and width >= 128


def test_the_favicon_and_app_icon_are_copies_of_the_asset() -> None:
    for name, copy in COPIES.items():
        assert copy.read_bytes() == ICON.read_bytes(), f"{name} differs from assets/{ICON.name}: copy it again"


def test_the_pages_and_config_point_at_the_icon() -> None:
    assert '<link rel="icon" type="image/png" href="/favicon.png"' in (REPO / "studio-ui" / "index.html").read_text()
    tauri = json.loads((REPO / "studio-ui" / "src-tauri" / "tauri.conf.json").read_text())
    assert tauri["bundle"]["icon"] == ["icons/icon.png"]
    assert "assets/valkyrie-studio-icon.png" in (REPO / "README.md").read_text()
