# Valkyrie AI Agent Studio

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Agents](https://img.shields.io/badge/agents-120-blue)
![Engine](https://img.shields.io/badge/default%20LLM-gemini--4--hydrogen%20(low)-purple)
![Rust](https://img.shields.io/badge/rust-tokio%20%2B%20serde-orange)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6-3178C6)
![React](https://img.shields.io/badge/React-18-61DAFB)
![Vite](https://img.shields.io/badge/Vite-5-646CFF)
![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![Antigravity](https://img.shields.io/badge/Antigravity-Ready-blueviolet)
![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-cc785c)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Free%20Tier-6366f1)
![OpenCode](https://img.shields.io/badge/OpenCode-Free%20Tier-10b981)
![Optimization](https://img.shields.io/badge/Optimization-pymoo%20GA-f59e0b)
![TDD](https://img.shields.io/badge/TDD-100%25%20Enforced-success)

**Valkyrie AI Agent Studio** is a standalone desktop platform (**Tauri Rust Shell + TypeScript + React + FastAPI + Cargo Workspace**) for designing, testing, optimizing, and compiling autonomous AI agents across **12 core tech company roles** (**10 focused agents per role, 120 agents total**).

## Key Capabilities
- **Standalone Tauri Rust Desktop GUI (`studio-ui/src-tauri/` + `studio-ui/src/`):** Native Rust Tauri v2 shell (`get_runtime_info`, `run_rust_agent` calling `valkyrie-rust-runtime`) paired with a modern CSS Grid + Container Query + `light-dark()` TypeScript UI supporting **System / Light / Dark** themes and **Beginner / Intermediate / Advanced** experience modes.
- **120 Focused Agents (`agents/` & `studio-ui/src/data/roles/`):** Every agent has a dedicated tool, typed input/output contract (`agent.ir.yaml`), deterministic Python handler (`agent.py`), `sample_data.json`, visual `demo.svg` preview, `AGENT.md`, `test_agent.py`, and standalone Rust crate (`rust/`).
- **Free-First LLM Routing (`studio-core/valkyrie/subscription_manager.py`):** Defaults to `gemini-4-hydrogen` (`thinking_level: "low"`), prioritizes free providers (`gemini_free`, `opencode_free`, `openrouter_free`, local `ollama` `qwen3.5:latest`), and falls back to subscriptions with explicit user notification on rate limits.
- **Local Metaheuristic Optimization (`studio-core/valkyrie/metaheuristic_optimizer.py`):** Runs a `pymoo` Genetic Algorithm (`GA`) locally every 3rd agent run to tune `temperature` and `max_tokens_scale`.
- **One-Click Rust Transpiler & 121-Crate Cargo Workspace:** Converts `agent.ir.yaml` into async `tokio` + `serde` Rust crates and validates the entire workspace via `cargo test --workspace`.

## Documentation
- [Quick Start (Beginners)](QUICK_START.md)
- [Architecture](docs/architecture.md)
- [API Reference](docs/api-reference.md)
- [Studio UI & Desktop Guide](docs/ui-guide.md)
- [Subscriptions & Free-Tier Routing](docs/subscriptions.md)
- [Metaheuristic Optimization (pymoo)](docs/metaheuristic.md)
- [Rust Deployment & Workspace](docs/rust-deployment.md)
- [Testing & 100% Coverage](docs/testing-and-coverage.md)
- [Project Plan & Gap Closure](PLAN.md)
- [Next Steps](NEXT-STEPS.md)
- [Software Metrics](METRICS.md)
- [Project Rules](GEMINI.md)

## Quick Commands
```bash
make test-all                     # Run 100% covered Python, TypeScript, and Rust tests
cd studio-ui && npm run desktop:build  # Build Vite + Electron standalone desktop bundle
cargo test --workspace            # Test runtime template + all 120 agent Rust crates
```
