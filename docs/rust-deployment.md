# Rust Deployment & Workspace Guide

## One-Click Transpilation (`valkyrie/rust_transpiler.py`)
`transpile_ir_to_rust(ir)` compiles any validated `AgentIR` into a standalone Rust crate (`valkyrie_<agent_id>`):
- **`Cargo.toml`:** Async `tokio` (`features = ["full"]`), `serde`, and `serde_json`.
- **`src/main.rs`:** `AgentConfig` defaulting to `gemini-4-hydrogen` (`thinking_level: "low"`), async `run_agent()`, and a deterministic `#[tokio::test]` harness.

## 121-Crate Cargo Workspace (`Cargo.toml`)
The root `Cargo.toml` unites `rust-runtime-template` and all 120 focused agent crates (`agents/*/*/rust`). Each agent crate defines its own domain tool function (e.g., `extract_requirements`, `estimate_rust_speedup`), `run_agent`, and `#[test] fn test_run()`.

```bash
cargo test --workspace
```
