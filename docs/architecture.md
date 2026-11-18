# Valkyrie Architecture

Valkyrie AI Agent Studio is organized as a modular monorepo where every source and test file stays under 200 lines.

## Layers
1. **Standalone Tauri Rust Desktop Shell (`studio-ui/`):**
   - **Tauri v2 Rust Shell (`src-tauri/src/lib.rs`, `src-tauri/tauri.conf.json`):** Hosts the native OS WebView window (`1440×920`) and exposes native Rust commands (`get_runtime_info`, `run_rust_agent`) linked directly to `valkyrie-rust-runtime`.
   - **React + TypeScript Workspace (`src/`):** Uses `src/data/roles/role01.ts`–`role12.ts` aggregated in `src/data/agentCatalog.ts` so all 120 focused agents are immediately browsable, searchable, and testable offline.
   - **Modern CSS (`src/styles/studio.css`):** CSS Grid (`grid-template-areas`), named container queries (`@container workspace`), `light-dark()` tokens with `@media (prefers-color-scheme: dark)` + `@supports` fallbacks, `scrollbar-gutter: stable`, and native `<dialog>` top-layer modals.
2. **Python Core & Compiler (`studio-core/valkyrie/`):**
   - `ir_schema.py`: Pydantic v2 Universal Agent IR (`agent.ir.yaml`) defaulting to `gemini-4-hydrogen` (`thinking_level: "low"`).
   - `llm_router.py`: Unified router for Gemini 4 Hydrogen and local Ollama (`http://localhost:11434/v1`, `qwen3.5:latest`) with token/cost calculation.
   - `subscription_manager.py`: Free-tier-first routing (`gemini_free`, `opencode_free`, `openrouter_free`, `ollama`) with rate-limit detection and subscription fallback notification.
   - `metaheuristic_optimizer.py`: Lightweight `pymoo` GA optimizer triggered locally every 3rd agent run.
   - `python_runner.py` & `eval_gate.py`: Restricted-namespace Python sandbox and automated schema/latency/cost/guardrail gate.
   - `rust_transpiler.py`, `command_centre.py`, and `api_server.py`: One-click Rust crate generation, lifecycle/trace control, REST endpoints, and `/ws/traces` WebSocket stream.
3. **Rust Runtime & Workspace (`Cargo.toml`, `rust-runtime-template/`, `agents/*/*/rust/`):**
   - Shared `ValkyrieAgent` trait and deterministic `MockGeminiAgent` in `rust-runtime-template/` plus 120 standalone agent crates unified in the root Cargo workspace.
