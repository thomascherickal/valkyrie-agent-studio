# Next Steps for Valkyrie AI Agent Studio

Keep this file current. Tick what is done, add what you find, then pick up the next open step that does not need the user (see "Autonomous Delivery" in `CLAUDE.md`).

## Verification Checklist (All Green)
- [x] `studio-core`: `pytest` (70 passed, 100.00% branch & statement coverage).
- [x] `command-centre`: `pytest` (1 passed, 100.00% branch & statement coverage).
- [x] `studio-ui`: `npm run desktop:build` (Vite + Tauri v2 Rust Shell) + `vitest run --coverage` (118 tests, 100% statements, branches, functions, lines).
- [x] `Cargo.toml` workspace: `cargo test --workspace` (122 crates: `rust-runtime-template`, `valkyrie-studio-tauri`, and 120 agent crates; 131 tests).
- [x] `valkyrie-studio-tauri`: end-to-end API start/stop, `cargo test -p valkyrie-studio-tauri -- --ignored` (needs `studio-core/.venv`).
- [x] `agents/`: 12 roles × 10 focused agents = 120 blueprints with `ROLE.md`, `AGENT.md`, `agent.ir.yaml`, `agent.py`, `test_agent.py`, `sample_data.json`, `demo.svg`, and `rust/`. All 120 also have a playbook and three generated Python versions, and all 360 are run in the sandbox by a test.

## Done
- [x] **Finished agents that only need data:** every agent has a playbook (`studio-core/valkyrie/playbooks/role01.py` to `role12.py`): the extra data fields it needs (label, kind, worked example), the sections of its deliverable (real domain guidance mixed with your data), and formulas for numeric agents (RICE, margins, burn rates and so on, evaluated by a small parser with no `eval`). A line that needs a blank field is left out, and the report ends with **Data still needed**. A test runs all 360 Python versions with only the example data and requires a complete report with nothing missing.
- [x] **Three Python versions of every agent:** **Rules** (fills the playbook), **Pipeline** (checked stages: validate, calculate, draft, coverage, review, compose) and **Hybrid** (adds a `call_model` hook you implement, plus a review step that catches a dropped section or a changed figure). They are rendered from templates in `impl_*.py` plus the agent's playbook, so the originals are always reproducible and nothing writes to them.
- [x] **Edit, check, save, revert, save as new:** `GET/PUT/DELETE /api/agents/{role}/{agent}/implementations/{impl}`, `POST .../implementations` (a new version next to the three built-in ones), and `POST .../check` (loads and runs the code once with the sample and returns the error and line). Edits live in `agent-edits/` (or `VALKYRIE_EDITS_DIR`); revert deletes the edit. Run executes the saved version chosen under **Run with** (`/api/agents/run` with `role_id`, `agent_id`, `impl`).
- [x] **Errors in the trace pane:** a **Problems** list in the Command Centre collects errors from check, save and run, newest first, with the line number.
- [x] **About this agent:** `GET .../explanation` serves a bulleted explanation (at least 250 words per agent in the tests): what it does, the data it needs, the figures it calculates, how each version works, and what to add. `GET .../fields` serves the data fields.
- [x] **Sandbox widened on purpose:** `typing`, `re`, `json` and `math` (public names only), the common pure builtins, exceptions and classes, a time limit that stops endless loops, and errors with line numbers. It is not a security boundary.
- [x] **Project icon:** `assets/valkyrie-studio-icon.png` is the web favicon, the Tauri app icon and the README logo. A test keeps the copies identical.
- [x] **Python tab from Intermediate:** it now appears at Intermediate and Advanced.
- [x] **Docs:** `README.md` and `QUICK_START.md` describe the GUI, the finished agents, the three Python versions, the code editor, the safety note, and the model keys.
- [x] **Tauri auto-start:** the desktop app starts `uvicorn` with `studio-core/.venv` (or `VALKYRIE_PYTHON`), reuses an API already on `:8000`, and stops the one it started on exit. The GUI retries `/health` until the API answers.
- [x] **Persisted custom agents:** created agents are saved to `custom-agents/` (or `VALKYRIE_CUSTOM_DIR`) and restored under Custom Agents. They get the same three Python versions and a general playbook (context, owner, deadline).
- [x] **Provider keys and `.env`:** the API reads `GEMINI_API_KEY`, `OPENROUTER_API_KEY` and `OPENCODE_API_KEY` from the environment or the repo's `.env`. Without a key, runs are simulated.
- [x] **`.gitignore`:** `target/`, `.venv/`, `node_modules/`, `dist/`, `.env*` (but not `.env.example`), `custom-agents/` and `agent-edits/` are ignored.
- [x] **Test tooling:** `make test-all` runs `python -m pytest`, so a venv symlinked into a git worktree cannot import another checkout's code.
- [x] **No hidden constants in formulas:** the IAM auditor has a `needed_count` field (was a fixed 2) and the Rust-port advisor a `week_cost` field (was a fixed 4,000 USD per engineer-week); the examples keep the old values.

## Recommended Next Steps
1. **Needs the user: live provider check.** Run once with a real `GEMINI_API_KEY`, and confirm the OpenCode endpoint (`https://opencode.ai/zen/v1`) and a free Model ID for OpenRouter and OpenCode. No live call has been made to any hosted provider.
2. **Give the Hybrid version a real model.** `call_model` is a stub because the sandbox has no network. Offer a safe, server-side helper (for example a `model(prompt)` function the sandbox can call that uses the configured provider and key) so Hybrid works without editing code.
3. **Review the playbooks with the people who own each domain.** They are expert-written starting points. Thresholds and wording should be adjusted to each team's standards (the About tab lists what to add).
4. **Interpret free text, not only fill templates.** The playbooks use the data you supply; they do not extract data from a pasted document. Add parsers (for example pull RICE numbers out of a backlog table) for the agents where it matters most.
5. **Deploy to Rust ignores the Python versions.** It transpiles the agent's IR only, so edited Python does not change the generated crate. Decide whether it should, or label it.
6. **Run uses the saved version.** Unsaved edits in the editor are not run (a hint says so). Offer "Run with my unsaved edits".
7. **Stale edits after regeneration.** Creating a custom agent with an id that already exists replaces its original but keeps its saved edits. Drop them on regenerate, or warn.
8. **Delete a custom agent.** Saved agents can be created and restored but not removed. Add `DELETE /api/agents/custom/{id}` and a Delete button.
9. **Stream traces.** `/ws/traces` exists but the Command Centre only polls the REST list. Use the WebSocket for live traces.
10. **Bundle the API for installers.** The auto-start finds the repo at compile time, so it works for `desktop:start` and dev builds only. A packaged installer needs the API shipped as a Tauri sidecar (for example a PyInstaller binary).
11. **Pick up key changes without a restart.** Keys are read once at startup, so editing `.env` needs an API restart.
12. **Cap the health retry.** The GUI retries forever at a fixed interval. Add a cap or backoff if the offline noise matters.
13. **Give Advanced its own tabs.** Advanced currently shows the same tabs as Intermediate.
