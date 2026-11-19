# Support Macro Curator (`15-macro-curator`)

**Role:** Technical Support
**Tool:** `curate_macros`

## Focused Responsibility
Curates support macros by usage, quality, and outcome, and retires stale ones.

## Contract
- **Input (`macro_usage`):** string
- **Output (`macro_plan`):** string, `tool_used` (`curate_macros`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_macro_curator`)
