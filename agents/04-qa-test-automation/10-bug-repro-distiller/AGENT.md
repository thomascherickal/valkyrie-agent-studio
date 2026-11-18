# Bug Repro Distiller (`10-bug-repro-distiller`)

**Role:** QA & Test Automation  
**Tool:** `distill_min_repro`

## Focused Responsibility
Condenses verbose customer bug threads into minimal deterministic repros.

## Contract
- **Input (`bug_thread`):** string
- **Output (`repro_steps`):** string, `tool_used` (`distill_min_repro`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_bug_repro_distiller`)
