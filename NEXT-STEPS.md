# Next Steps for Valkyrie AI Agent Studio

Keep this file current. Tick what is done, add what you find, then pick up the next open step that does not need the user (see "Autonomous Delivery" in `CLAUDE.md`).

## Verification Checklist (All Green)
- [x] `studio-core`: `pytest` (123 passed, 100.00% branch & statement coverage).
- [x] `command-centre`: `pytest` (1 passed, 100.00% branch & statement coverage).
- [x] `studio-ui`: `npm run desktop:build` (Vite + Tauri v2 Rust Shell) + `vitest run --coverage` (145 tests, 100% statements, branches, functions, lines).
- [x] `Cargo.toml` workspace: `cargo test --workspace` (242 crates: `rust-runtime-template`, `valkyrie-studio-tauri`, and 240 agent crates).
- [x] `valkyrie-studio-tauri`: end-to-end API start/stop, `cargo test -p valkyrie-studio-tauri -- --ignored` (needs `studio-core/.venv`).
- [x] `agents/`: 12 roles × 20 focused agents = 240 blueprints with `ROLE.md`, `AGENT.md`, `agent.ir.yaml`, `agent.py`, `test_agent.py`, `sample_data.json`, `demo.svg`, and `rust/`. All 240 also have a playbook and three generated Python versions, and all 720 are run in the sandbox by a test.

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
- [x] **Hybrid has a real model path:** the sandbox always has `model(prompt)`. The API answers it with your provider (Gemini by default, or `VALKYRIE_MODEL_PROVIDER` and `VALKYRIE_MODEL_ID`) and returns `None` when no key is set or the call fails, so the draft is used and the tests never touch the network. A slow model call does not use up the code's time limit.
- [x] **Free text fills blank fields:** a blank data field is read from the main input when it says `Label: value`, `label = value` or `| label | value |`. A value you supply always wins, and numbers are pulled out of the value ("2 person-months" gives 2).
- [x] **Run with my unsaved edits:** `POST /api/agents/run` accepts `code`; the Run tab offers a button when the editor has unsaved changes.
- [x] **Custom agents:** regenerating an agent drops its old edits, and `DELETE /api/agents/custom/{id}` (with a Delete agent button that asks once) removes it with its edits.
- [x] **Live traces:** `/ws/traces` streams the shared Command Centre list now and on every change; the panel shows it and falls back to the REST list when the socket is down.
- [x] **Keys without a restart:** each run re-reads `.env` (real environment variables still win; a key removed from the file is unset). The Advanced **Providers** tab shows which keys are set (never the key) and has a **Reload .env** button (`GET /api/providers`, `POST /api/providers/reload`).
- [x] **Health retry:** the GUI backs off (1.5 s up to 15 s), stops after 12 retries and shows **Retry connection**.
- [x] **Deploy to Rust is labelled:** the dialog says the crate is built from the agent's definition, not from edited Python.
- [x] **Modularity:** `explanation` moved to `agent_explanation.py`, storage paths to `storage.py`, the trace stream to `command_centre_routes.py`, and the CSS split in two, so every file is under 200 lines.

- [x] **20 agents per role:** ids 11 to 20 of every role (120 new agents) have the same files, playbook (data fields, five guidance sections, formulas with no hidden constants) and profile as the first ten. Playbooks and profiles now live in per-role packages (`playbooks/roleNN/core.py` and `extra.py`, `profiles/roleNN.py`), and a test keeps the UI catalog, `ROLE.md` and the `agents/` folders in step.

- [x] **Provider fallback:** a run asks Gemini first, then OpenCode free models (`big-pickle`, `deepseek-v4.1-flash-free`, `mimo-v2.6-flash-free`), then OpenRouter free models (`openrouter/free`, `google/gemma-4-31b-it:free`). Providers with no key are skipped, an empty or failed answer moves on, and all-failed returns 502 with each reason. The Hybrid `model()` helper uses the same chain. Override the lists with `VALKYRIE_OPENCODE_MODELS` and `VALKYRIE_OPENROUTER_MODELS`.
- [x] **Full step tracing:** every run and every action is recorded step by step (`tracing.py`), kept in memory, appended to `logs/trace.jsonl`, streamed over `/ws/trace` and shown in the Command Centre **Trace log** with run and status filters, expandable detail, copy and clear. Keys are redacted before anything is stored or sent.
- [x] **Live provider check (Gemini and OpenRouter):** verified with the saved keys. It found and fixed a real bug: the Gemini request carried `thinking_level` and `reasoning_effort` as top-level fields, which the API rejects (HTTP 400); the level now goes in `generationConfig.thinkingConfig`, and Gemini's key travels in a header instead of the URL. A Hybrid run now uses the real model and its review step passes.

- [x] **API bundled for installers:** `make sidecar` builds the API into one executable (PyInstaller, 89 MB, 972 agent files), `make package` ships it beside the app, and the shell uses it when installed (`plan::choose`). Verified: the binary serves all 240 agents, runs an agent, creates a custom agent and writes its data and trace log to the user folder; Tauri placed it next to the app executable; a real `.deb` built and contains `usr/bin/valkyrie-studio-tauri` and `usr/bin/valkyrie-api`. Packaged apps keep your data and `.env` in the user folder (`VALKYRIE_HOME` overrides).

- [x] **Branches merged:** every branch is in `main` (PRs #7 to #12), including the project skills under `.claude/skills/`. Some of those skill files are over 200 lines (for example `validate-findings.cjs`); they are tooling, not project source.
- [x] **OpenCode key checked:** the key in `.env` is valid (a wrong key gets 401, this one lists 41 models) but OpenCode answers HTTP 429 `FreeUsageLimitError` for every free model, and paid models answer 403 (model access disabled) or 402 (no balance). The chain falls through to OpenRouter, and the trace shows each attempt.

- [x] **Git hooks enforce the tracking rule:** `.githooks/pre-commit` rewrites the `METRICS.md` table (`scripts/update_metrics.py`) and refuses a commit that does not include `NEXT-STEPS.md`; `.githooks/pre-push` refuses a push while the table is stale. `make hooks` turns them on (once per clone), `make metrics` rewrites the table by hand, `SKIP_TRACKING=1` skips them once.

- [x] **Stale worktrees removed, and kept away:** seven stale worktrees (six with their folders gone, one locked by an ended session) and 14 merged local branches were removed; only the main checkout and the active session's worktree remain. `make clean-worktrees` (`scripts/clean_worktrees.py`, tested) repeats it safely: it only touches worktrees whose folder is gone and branches that `git branch -d` accepts. `CLAUDE.md` now has a strict rule to merge finished work automatically and clean up after every merge.

- [x] **Skills excluded from the line limit:** `.claude/skills/` is vendored tooling, so the 200-line rule in `CLAUDE.md` no longer applies to it.
- [x] **Intermediate mode removed:** only Beginner and Advanced remain; Advanced has Design, Python and Providers.
- [x] **Health retry cap is 3:** the GUI backs off (1.5 s, 3 s, 6 s), stops after three retries and shows Retry connection.

- [x] **Secrets tab:** the Providers tab became **Secrets** (Advanced). Gemini, OpenRouter and OpenCode each have a key field shown as its first 10 characters plus asterisks, a model drop down filled live from the provider's catalog (free first), Save, Remove key and **Test Key**, which sends one real request and shows a green Test Succeeded or a red Test Failed with the likely causes listed. Keys are optional (a banner warns that output is simulated). Choices are saved to `.env` and used first by the fallback chain and `model()`. Verified live: Gemini 50 models, OpenRouter 480 (17 free), OpenCode 92 (13 free); Gemini and OpenRouter keys pass, OpenCode fails with its 429 and the causes.
- [x] **Trace calls cannot collide:** the trace function's first three arguments are positional-only, so a detail field may have any name.

- [x] **Deploy to Rust verifies first:** the Deploy button opens a verification box that compiles every Python version of the agent and runs it on six inputs (sample, no data, blank, very long, unicode, text for numbers). Problems block and are listed by version, input and line; a pass shows the warning that the Rust crate is built from the agent's definition and offers **Continue and deploy** or **Save verified agent…** (a name box; the server verifies again and saves a copy with its edits under Custom Agents). All 240 built-in agents pass.

## Recommended Next Steps
1. **Needs the user: OpenCode free quota or credits.** The key works, but OpenCode's free quota is used up (HTTP 429) and the account has no credits. Wait for the free quota to reset, or top up credits and enable model access in the OpenCode console, then confirm that a forced Gemini failure is answered by an OpenCode free model.
2. **Review the playbooks with the people who own each domain.** They are expert-written starting points. Thresholds and wording should be adjusted to each team's standards (the About tab lists what to add).
3. **Run the installer on a desktop.** The `.deb` was built and its contents checked, but not launched (no display here). Install it, open the app and confirm the status bar reads `gemini-4-hydrogen` and the Providers tab shows the user-folder `.env`. The macOS (`dmg`) and Windows (`msi`) bundles need to be built on those systems with `make package BUNDLES=...`.
