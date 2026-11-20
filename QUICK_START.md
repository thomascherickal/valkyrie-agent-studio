# Quick Start Guide (Beginners)

Welcome to **Valkyrie Agent Studio**! Follow these steps to build, test, and run the standalone desktop GUI and backend locally.

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
3. `Cargo.toml` workspace: `rust-runtime-template` + all 240 agent Rust crates.

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
Without a key, runs are simulated and nothing is sent anywhere. Give the API a key either way:

**1. A `.env` file (easiest).** Copy the template and fill it in. The API reads it when it starts, including when the desktop app starts the API for you. `.env` is gitignored, so your keys are not committed.
```bash
cp .env.example .env     # then edit .env
```
```
GEMINI_API_KEY=...        # Gemini 4 Hydrogen, the default for every request
OPENCODE_API_KEY=...      # fallback 1: OpenCode free models (they need a key)
OPENROUTER_API_KEY=...    # fallback 2: OpenRouter free models
```
**If Gemini fails, the next provider answers.** A run tries Gemini, then OpenCode free models (`big-pickle`, `deepseek-v4.1-flash-free`, `mimo-v2.6-flash-free`), then OpenRouter free models (`openrouter/free`). A provider with no key is skipped. The **Secrets** tab (Advanced) is where you manage all of this.

**2. Environment variables.** Export them before starting the API. A variable you export wins over the same name in `.env`.
```bash
export GEMINI_API_KEY=...
```

You do not need to restart the API after changing a key: every run re-reads `.env`, and **Reload .env** in the Secrets tab does it on demand. Local Ollama needs no key.

### The Secrets tab (Advanced)
One card each for **Gemini**, **OpenRouter** and **OpenCode**, plus a **Default provider** drop down:
- **API key:** shown as its first 10 characters followed by asterisks (a key you type is hidden entirely). Keys are optional: with none set, a banner says output is simulated. Save writes it to `.env` (owner-only access); **Remove key** clears it.
- **Model:** a drop down filled live from the provider's own catalog, free models first and marked (free). If a catalog cannot be reached, the built-in free models are shown and the note says why. **Effort** (low, medium, high) is Gemini's thinking level.
- **Test Key:** sends one real request with the key you typed (or the saved one). A green **Test Succeeded**, or a red **Test Failed** with the provider's message and the likely causes listed underneath: an invalid or revoked key, no credits, model access disabled, the model slug not found, a rate or free-usage limit, an outage, or no network.
- Your model and effort choices are used first by the fallback chain and by the Hybrid `model()` helper.

### Deploy to Rust, with a check first
Click **Deploy to Rust** and the studio first verifies the agent: every Python version must compile, avoid blocked code and run without errors on six kinds of input (the sample, no data, blank fields, very long text, unicode, and text where numbers belong). Any problem blocks the deploy and is listed with the version, the input and the line. If everything passes you see a warning (the Rust crate is built from the agent's definition, not from your Python) and can continue, or choose **Save verified agent…** to keep a verified copy, with your edits, under Custom Agents.

### See every step
The right-hand **Command Centre** has a **Trace log**: every step of every run, live (the request, the key check, the prompt, each provider attempt and its error, the code that ran, each stage, the checks). Click a step to open its full detail. The same steps are written to `logs/trace.jsonl`. Keys are never recorded.

### Install it as an app (carries its own API)
```bash
studio-core/.venv/bin/pip install pyinstaller    # once
cargo install tauri-cli                          # once
make package BUNDLES=deb                         # or appimage, msi, dmg (on that system)
```
`make sidecar` builds the API into one executable (`studio-ui/src-tauri/binaries/`), and `make package` has Tauri ship it beside the app. An installed app starts that API itself and keeps what you create (custom agents, edits, logs and your `.env`) in your user folder, for example `~/.local/share/valkyrie-studio/` on Linux. The Secrets tab shows the exact path of the `.env`. Set `VALKYRIE_HOME` to use another folder.

## 4. Explore the Desktop Studio
1. **Pick an agent:** Search the left sidebar across all 12 roles, or create your own under **Create agent**: describe it in plain English and it appears under **Custom Agents**. Created agents are saved to `custom-agents/` (set `VALKYRIE_CUSTOM_DIR` to move it) with their Python, YAML and Rust files, and they come back the next time you open the studio.
2. **Run an agent:** Every agent is a finished product that only needs your data. The **Run** tab shows a box for its main input (for example **Feature brief**) and one box for each extra piece of data it needs (for example **Target users**, **Success metric**). They start with a worked example, so the agent runs straight away. Replace the examples with your real data. Click **Add field** for any extra data of your own: it is sent under the name you give it.
   - **Run with** chooses how it runs: the Gemini 4 Hydrogen model, or one of the agent's three Python versions: **Rules** (fills the agent's playbook with your data), **Pipeline** (the same, in checked stages, with input coverage and review notes) and **Hybrid** (adds a model hook that you implement, with a review step).
   - The result is a complete deliverable for that agent: its sections, the figures it calculated, and a **Data still needed** list for any field you left blank. A line that depends on a blank field is left out instead of guessed.
3. **About this agent:** the **About this agent** tab explains in bullets what the agent does, the data it needs, the figures it calculates, how each Python version works, and what you still have to add (your systems, thresholds and rules).
4. **Experience level** (top bar) reveals more tabs:
   - **Beginner:** Run, About this agent and Create agent.
   - **Advanced:** adds **Design** (system prompt, provider, thinking level), **Python** and **Secrets**. There are two modes: Beginner and Advanced.
5. **Python tab:** pick one of the three versions, or one you saved, and edit it. **Check for errors** loads and runs it once and reports problems with the line number. **Save changes** stores your edit (and checks it). **Revert to original** puts a built-in version back. **Save as new implementation** keeps your code as an extra version next to the three built-in ones. The originals are never changed: they are rebuilt from the project files, your edits are saved separately in `agent-edits/` (set `VALKYRIE_EDITS_DIR` to move them), and the original stays visible under the editor. Run uses the **saved** version you pick under **Run with**. Your code may import `typing`, `re`, `json` and `math`.
6. **Command Centre** (right pane): start or stop the selected agent, or stop all, and watch their traces. Errors from checking, saving and running an agent appear under **Problems**, newest first.
7. **Theme:** System, Light, or Dark in the top bar.
8. **Deploy to Rust:** Click **Deploy to Rust** for the generated crate and its benchmark.

**Safety:** your Python runs inside the API on your machine with your permissions. The sandbox blocks obvious mistakes (such as importing `os`, calling `open`, or an endless loop), but it is not a security wall. Read code you did not write before running it, and do not expose port 8000 beyond your own machine.
