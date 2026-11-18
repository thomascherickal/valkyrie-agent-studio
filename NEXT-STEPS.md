# Next Steps for Valkyrie AI Agent Studio

## Verification Checklist (All Green)
- [x] `studio-core`: `pytest` (29 passed, 100.00% branch & statement coverage).
- [x] `command-centre`: `pytest` (1 passed, 100.00% branch & statement coverage).
- [x] `studio-ui`: `npm run desktop:build` (Vite + Tauri v2 Rust Shell) + `vitest run --coverage` (39 tests, 100% statements, branches, functions, lines).
- [x] `Cargo.toml` workspace: `cargo test --workspace` (122 crates: `rust-runtime-template`, `valkyrie-studio-tauri`, and 120 agent crates).
- [x] `agents/`: 12 roles × 10 focused agents = 120 blueprints with `ROLE.md`, `AGENT.md`, `agent.ir.yaml`, `agent.py`, `test_agent.py`, `sample_data.json`, `demo.svg`, and `rust/`.

## Recommended Next Phases
1. **Phase 1 — Live Provider Credentials:** `export GEMINI_API_KEY=...` (or `OPENROUTER_API_KEY` / `OPENCODE_API_KEY`) before `make run-gui`; the backend reads them from the environment. Confirm the OpenCode endpoint (`https://opencode.ai/zen/v1`) and pick a model ID under Design, since neither provider has a default model. Without a key, runs return a deterministic simulation. Or start local Ollama (`qwen3.5:latest`) and pick it under Design.
2. **Phase 2 — Tauri Native Sidecar:** Auto-spawn `uvicorn valkyrie.api_server:app` from `src-tauri/src/lib.rs` on desktop app launch.
3. **Phase 3 — `.gitignore` & Clean Git Tree:** Add `.gitignore` for `target/`, `.venv/`, `node_modules/`, and `dist/` and unstage generated artifacts.
