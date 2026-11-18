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
If you also want the FastAPI backend running for live REST/WebSocket calls:
```bash
cd studio-core && .venv/bin/uvicorn valkyrie.api_server:app --reload --port 8000
```

## 4. Explore the Desktop Studio
1. **Search 120 Agents:** Use the left sidebar to filter across all 12 tech company roles (`01-product-management` through `12-cxos`).
2. **Theme Mode:** Switch between **System**, **Light**, and **Dark** in the top bar (persisted cleanly without flash-of-unthemed-content).
3. **Experience Modes:**
   - **Beginner Mode:** Visual Agent Builder, focused tool/schema preview, Subscription Switcher, and Sandbox Console.
   - **Intermediate Mode:** Unlocks the Custom Python Override editor (`agent.py`).
   - **Advanced Mode:** Unlocks the **Command Centre** to start, stop, admin-stop-all, and inspect visual agent traces.
4. **Deploy to Rust:** Click **Deploy to Rust** to inspect the native `<dialog>` deployment summary and crate target.
