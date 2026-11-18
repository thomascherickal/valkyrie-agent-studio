# Next Steps for Valkyrie AI Agent Studio

Keep this file current. Tick what is done, add what you find, then pick up the next open step that does not need the user (see "Autonomous Delivery" in `CLAUDE.md`).

## Verification Checklist (All Green)
- [x] `studio-core`: `pytest` (29 passed, 100.00% branch & statement coverage).
- [x] `command-centre`: `pytest` (1 passed, 100.00% branch & statement coverage).
- [x] `studio-ui`: `npm run desktop:build` (Vite + Tauri v2 Rust Shell) + `vitest run --coverage` (40 tests, 100% statements, branches, functions, lines).
- [x] `Cargo.toml` workspace: `cargo test --workspace` (122 crates: `rust-runtime-template`, `valkyrie-studio-tauri`, and 120 agent crates; 131 tests).
- [x] `valkyrie-studio-tauri`: end-to-end API start/stop, `cargo test -p valkyrie-studio-tauri -- --ignored` (needs `studio-core/.venv`).
- [x] `agents/`: 12 roles × 10 focused agents = 120 blueprints with `ROLE.md`, `AGENT.md`, `agent.ir.yaml`, `agent.py`, `test_agent.py`, `sample_data.json`, `demo.svg`, and `rust/`.

## Done
- [x] **Tauri auto-start (was Phase 2):** the desktop app starts `uvicorn` with `studio-core/.venv` (or `VALKYRIE_PYTHON`), reuses an API already on `:8000`, and stops the one it started on exit. The GUI retries `/health` every 1.5 s until the API answers and reloads the Command Centre when it does.
- [x] **Docs:** `README.md` and `QUICK_START.md` describe the rewritten GUI, the API, and the model keys.
- [x] **`.gitignore` (was Phase 3):** `target/`, `.venv/`, `node_modules/`, `dist/` are ignored.
- [x] **Provider keys:** the backend reads `GEMINI_API_KEY`, `OPENROUTER_API_KEY` and `OPENCODE_API_KEY` from the environment. Without a key, runs are simulated.

## Recommended Next Steps
1. **Needs the user: live provider check.** Run once with a real `GEMINI_API_KEY`, and confirm the OpenCode endpoint (`https://opencode.ai/zen/v1`) and a free Model ID for OpenRouter and OpenCode. No live call has been made to any hosted provider.
2. **Persist custom agents.** Agents created under Create agent vanish on reload, because only `write_generated_agent` can save them and no route calls it. Add a save route and load saved agents into the "Custom Agents" role at startup.
3. **Stream traces.** `/ws/traces` exists but the Command Centre only polls the REST list. Use the WebSocket for live traces.
4. **Bundle the API for installers.** The auto-start finds the repo at compile time, so it works for `desktop:start` and dev builds only. A packaged installer needs the API shipped as a Tauri sidecar (for example a PyInstaller binary).
5. **Cap the health retry.** The GUI retries forever at a fixed interval. Add a cap or backoff if the offline noise matters.
6. **Test tooling.** `make test-all` uses `.venv/bin/pytest`, which can import another checkout's code when the venv is symlinked into a git worktree. Switch the Makefile to `.venv/bin/python -m pytest`.
