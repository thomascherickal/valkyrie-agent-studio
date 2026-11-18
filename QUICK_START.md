# Quick Start Guide (Beginners)

Welcome to **Valkyrie AI Agent Studio**! Follow these steps to build, test, and run the standalone desktop GUI and backend locally.

## 1. Prerequisites
- **Python 3.12+** (with virtual environment in `studio-core/.venv`)
- **Node.js 20+** (Node v24 recommended for modern tooling)
- **Rust & Cargo** (`rustc` + `cargo`)

## 2. Verify All Tests & Coverage (100%)
```bash
make test-all
cargo test --workspace
```
This runs:
1. `studio-core`: `pytest` with 100% branch and statement coverage.
2. `studio-ui`: `vitest run --coverage` with 100% lines, branches, functions, and statements.
3. `Cargo.toml` workspace: `rust-runtime-template` + all 120 agent Rust crates.

## 3. Build & Launch the Standalone Desktop GUI
```bash
cd studio-ui
npm run desktop:build   # Compiles TypeScript + Vite (dist/) and Tauri Rust shell (src-tauri/)
npm run desktop:start   # Launches the native Tauri Rust desktop window
```
The studio needs its Python API (FastAPI, `localhost:8000`) for everything: running agents, creating them, deploying, and the Command Centre.
- **Desktop app:** `desktop:start` starts the API for you with `studio-core/.venv`, reuses one that is already running on port 8000, and stops the one it started when you close the window. Set `VALKYRIE_PYTHON` to use a different Python.
- **Browser or manual start:** `make run-gui`, or `cd studio-core && .venv/bin/uvicorn valkyrie.api_server:app --port 8000`.
- The top bar shows **API offline** until the API answers, then the engine, `gemini-4-hydrogen · low thinking`. It keeps retrying, so a slow start is fine.

### Live model keys
Export a key before starting the API. Without one, runs are simulated and nothing is sent anywhere.
```bash
export GEMINI_API_KEY=...        # Gemini 4 Hydrogen, the default for every request
export OPENROUTER_API_KEY=...    # optional: OpenRouter (pick a Model ID under Design)
export OPENCODE_API_KEY=...      # optional: OpenCode (pick a Model ID under Design)
```
Local Ollama needs no key.

## 4. Explore the Desktop Studio
1. **Pick an agent:** Search the left sidebar across all 12 roles, or create your own under **Create agent**: describe it in plain English and it appears under **Custom Agents**. Created agents are saved to `custom-agents/` (set `VALKYRIE_CUSTOM_DIR` to move it) with their Python, YAML and Rust files, and they come back the next time you open the studio.
2. **Run:** Type a task and click **Run agent**. The result shows the engine, tokens, cost, and whether the eval gate passed.
3. **Experience level** (top bar) reveals more tabs:
   - **Beginner:** Run and Create agent.
   - **Intermediate:** adds **Design**: system prompt, provider (Gemini 4 Hydrogen, Ollama, OpenRouter, OpenCode), and thinking level.
   - **Advanced:** adds **Python**: run your own `run_agent(payload)` instead of the model.
4. **Command Centre** (right pane): start or stop the selected agent, or stop all, and watch their traces.
5. **Theme:** System, Light, or Dark in the top bar.
6. **Deploy to Rust:** Click **Deploy to Rust** for the generated crate and its benchmark.
