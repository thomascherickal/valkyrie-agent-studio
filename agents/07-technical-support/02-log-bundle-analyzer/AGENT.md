# Log Bundle Analyzer (`02-log-bundle-analyzer`)

**Role:** Technical Support  
**Tool:** `extract_root_exception`

## Focused Responsibility
Extracts root-cause exceptions and timestamps from diagnostic logs.

## Contract
- **Input (`log_excerpt`):** string
- **Output (`diagnostic_summary`):** string, `tool_used` (`extract_root_exception`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_log_bundle_analyzer`)
