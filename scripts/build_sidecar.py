"""Build the API into one executable (a Tauri sidecar) with PyInstaller.

Run from the repo root with the studio-core venv:  studio-core/.venv/bin/python scripts/build_sidecar.py
It writes studio-ui/src-tauri/binaries/valkyrie-api-<target-triple>, which `make package` hands to Tauri.
"""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "studio-ui" / "src-tauri" / "binaries"
# The API only reads these from agents/: the definition, the sample, and the docs. Rust crates and tests stay out.
SKIP_DIRS = {"rust", "__pycache__"}
SKIP_FILES = {"test_agent.py", "demo.svg"}


def keep(path: Path) -> bool:
    """True when a file under agents/ belongs in the bundle."""
    return not (SKIP_DIRS & set(path.parts)) and path.name not in SKIP_FILES


def target_triple(rustc_verbose: str) -> str:
    """The host target triple from `rustc -vV`, for example x86_64-unknown-linux-gnu."""
    found = re.search(r"^host: (\S+)$", rustc_verbose, re.MULTILINE)
    if not found:
        raise ValueError("rustc -vV did not report a host triple")
    return found.group(1)


def copy_agents(source: Path, target: Path) -> int:
    """Copy the files the API needs from `source` into `target`. Returns how many files."""
    count = 0
    for file in sorted(source.rglob("*")):
        if file.is_file() and keep(file.relative_to(source)):
            destination = target / file.relative_to(source)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, destination)
            count += 1
    return count


def build() -> Path:
    triple = target_triple(subprocess.run(["rustc", "-vV"], capture_output=True, text=True, check=True).stdout)
    suffix = ".exe" if sys.platform == "win32" else ""
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        files = copy_agents(ROOT / "agents", work / "agents")
        print(f"bundling {files} agent files")
        subprocess.run(
            [sys.executable, "-m", "PyInstaller", "--onefile", "--noconfirm", "--clean", "--name", "valkyrie-api",
             "--distpath", str(work / "dist"), "--workpath", str(work / "build"), "--specpath", str(work),
             "--paths", str(ROOT / "studio-core"), "--add-data", f"{work / 'agents'}{';' if sys.platform == 'win32' else ':'}agents",
             "--collect-submodules", "uvicorn", "--collect-submodules", "valkyrie",
             str(ROOT / "studio-core" / "valkyrie" / "serve.py")],
            check=True,
        )
        OUT.mkdir(parents=True, exist_ok=True)
        binary = OUT / f"valkyrie-api-{triple}{suffix}"
        shutil.copy2(work / "dist" / f"valkyrie-api{suffix}", binary)
    print(f"wrote {binary} ({binary.stat().st_size // 1_000_000} MB)")
    return binary


if __name__ == "__main__":
    build()
