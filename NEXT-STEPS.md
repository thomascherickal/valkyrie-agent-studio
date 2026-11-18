# Next Steps for Valkyrie AI Agent Studio

Keep this file current. Tick what is done, add what you find, then pick up the next open step that does not need the user (see "Autonomous Delivery" in `CLAUDE.md`).

## Verification Checklist (All Green)
- [x] `studio-core`: `pytest` (45 passed, 100.00% branch & statement coverage).
- [x] `command-centre`: `pytest` (1 passed, 100.00% branch & statement coverage).
- [x] `studio-ui`: `npm run desktop:build` (Vite + Tauri v2 Rust Shell) + `vitest run --coverage` (60 tests, 100% statements, branches, functions, lines).
- [x] `Cargo.toml` workspace: `cargo test --workspace` (122 crates: `rust-runtime-template`, `valkyrie-studio-tauri`, and 120 agent crates; 131 tests).
- [x] `valkyrie-studio-tauri`: end-to-end API start/stop, `cargo test -p valkyrie-studio-tauri -- --ignored` (needs `studio-core/.venv`).
- [x] `agents/`: 12 roles × 10 focused agents = 120 blueprints with `ROLE.md`, `AGENT.md`, `agent.ir.yaml`, `agent.py`, `test_agent.py`, `sample_data.json`, `demo.svg`, and `rust/`.

## Done
- [x] **Tauri auto-start:** the desktop app starts `uvicorn` with `studio-core/.venv` (or `VALKYRIE_PYTHON`), reuses an API already on `:8000`, and stops the one it started on exit. The GUI retries `/health` every 1.5 s until the API answers and reloads the Command Centre when it does.
- [x] **Persisted custom agents:** `POST /api/agents/create-from-prompt` saves the generated files to `custom-agents/` (or `VALKYRIE_CUSTOM_DIR`), `GET /api/agents/custom` lists them, and the GUI restores them under Custom Agents once the API is online.
- [x] **View, edit, save and revert each agent's Python:** the Python tab shows an agent's own `agent.py` (all 120 plus custom agents), saves edits to `agent-edits/` (or `VALKYRIE_EDITS_DIR`) through `GET/PUT/DELETE /api/agents/{role}/{agent}/code`, and **Revert to original** deletes the edit. The original is never written and stays visible in the editor. Unsaved edits survive tab switches. Agents are looked up by role and id, so a custom agent can never shadow a catalog one.
- [x] **Data boxes for every agent:** the Run tab shows a labelled box for the agent's own input field (from its schema), plus **Add field** for extra named boxes. The run payload is keyed by those names, which is what each agent's `run_agent(payload)` reads. A guard stops a run when the Python override is on but its code has not loaded.
- [x] **Sandbox runs the real agents:** the Python sandbox allows `import typing` (a namespace of its public names only). A test runs all 120 original `agent.py` files with their own sample data. The sandbox is not a security boundary; it catches mistakes in your own code.
- [x] **Docs:** `README.md` and `QUICK_START.md` describe the rewritten GUI, the API, the saved agents, the code editor, and the model keys.
- [x] **`.gitignore`:** `target/`, `.venv/`, `node_modules/`, `dist/`, `.env*`, `custom-agents/` and `agent-edits/` are ignored.
- [x] **Provider keys:** the backend reads `GEMINI_API_KEY`, `OPENROUTER_API_KEY` and `OPENCODE_API_KEY` from the environment. Without a key, runs are simulated.
- [x] **`.env` loading:** the API reads the repo's `.env` (or `VALKYRIE_ENV_FILE`) at startup, including when the desktop app starts it. A variable already set in the shell wins, empty values are skipped, and values are never logged. `.env.example` is the committed template. Tests point the loader at nothing, so a real `.env` never leaks into them.
- [x] **Test tooling:** `make test-all` runs `python -m pytest`, so a venv symlinked into a git worktree cannot import another checkout's code.

## Recommended Next Steps
1. **Needs the user: live provider check.** Run once with a real `GEMINI_API_KEY`, and confirm the OpenCode endpoint (`https://opencode.ai/zen/v1`) and a free Model ID for OpenRouter and OpenCode. No live call has been made to any hosted provider.
2. **Warn about the Python sandbox in the user docs.** Your own Python runs inside the API with your machine's permissions, and the sandbox is a safety net, not a wall. Say so in `QUICK_START.md`, tell people to read shared code before running it, and not to expose port 8000 beyond their machine.
3. **Delete a custom agent.** Saved agents can be created and restored but not removed. Add `DELETE /api/agents/custom/{id}` and a Delete button.
4. **Stream traces.** `/ws/traces` exists but the Command Centre only polls the REST list. Use the WebSocket for live traces.
5. **Bundle the API for installers.** The auto-start finds the repo at compile time, so it works for `desktop:start` and dev builds only. A packaged installer needs the API shipped as a Tauri sidecar (for example a PyInstaller binary).
6. **Cap the health retry.** The GUI retries forever at a fixed interval. Add a cap or backoff if the offline noise matters.
7. **Edited Python reaches Rust.** Deploy to Rust transpiles the agent's IR only, so edited Python does not change the generated crate. Decide whether it should, or label it.
8. **Widen the sandbox on purpose.** User code cannot use classes, `range`, `isinstance` or `round`, because the restricted builtins omit them. Add the ones people hit, one at a time, with tests.
9. **Stale edits after regeneration.** Creating a custom agent with an id that already exists replaces its original but keeps its saved edit. Drop the edit on regenerate, or warn.
10. **Python tab discoverability.** It only appears at the Advanced experience level. Consider showing it from Intermediate.
11. **Pick up key changes without a restart.** Keys are read once at startup, so editing `.env` needs an API restart. Add a reload endpoint or re-read the file on each run.
