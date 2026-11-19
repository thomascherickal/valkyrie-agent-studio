.PHONY: test-all coverage run-gui deploy-rust sidecar package hooks metrics clean-worktrees

# Once per clone: turn on the git hooks in .githooks (METRICS.md refreshed on commit, checked on push).
hooks:
	chmod +x .githooks/*
	git config core.hooksPath .githooks

# Remove stale worktrees (folder gone) and local branches already merged into main. Add DRY=1 to only list them.
clean-worktrees:
	python3 scripts/clean_worktrees.py $(if $(DRY),--dry-run,)

# Rewrite the table in METRICS.md from the real counts.
metrics:
	python3 scripts/update_metrics.py

test-all:
	cd studio-core && .venv/bin/python -m pytest
	cd command-centre && PYTHONPATH=. ../studio-core/.venv/bin/python -m pytest
	cd studio-ui && npm test
	cargo test --workspace

coverage: test-all

run-gui:
	cd studio-core && .venv/bin/uvicorn valkyrie.api_server:app --reload --port 8000 &
	cd studio-ui && npm run desktop:start

deploy-rust:
	cargo build --release --workspace

# The API as one executable for installers (needs: studio-core/.venv/bin/pip install pyinstaller, and rustc).
sidecar:
	studio-core/.venv/bin/python scripts/build_sidecar.py

# An installer that carries the API (needs: cargo install tauri-cli). Pass BUNDLES=deb (or appimage, msi, dmg...) to pick one.
package: sidecar
	cd studio-ui && npm run build
	cd studio-ui/src-tauri && cargo tauri build --config tauri.sidecar.conf.json $(if $(BUNDLES),--bundles $(BUNDLES),)
