# Competitive Intel Analyst (`04-competitive-intel`)

**Role:** Product Management  
**Tool:** `diff_feature_matrix`

## Focused Responsibility
Builds feature parity and differentiation matrices against competitor release notes.

## Contract
- **Input (`competitor_notes`):** string
- **Output (`matrix_summary`):** string, `tool_used` (`diff_feature_matrix`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_competitive_intel`)
