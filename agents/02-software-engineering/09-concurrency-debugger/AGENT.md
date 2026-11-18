# Concurrency Debugger (`09-concurrency-debugger`)

**Role:** Software Engineering  
**Tool:** `analyze_lock_graph`

## Focused Responsibility
Identifies lock ordering inversions, unawaited futures, and race windows.

## Contract
- **Input (`async_trace`):** string
- **Output (`deadlock_report`):** string, `tool_used` (`analyze_lock_graph`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_concurrency_debugger`)
