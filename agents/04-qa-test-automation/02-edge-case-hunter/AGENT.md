# Edge Case Hunter (`02-edge-case-hunter`)

**Role:** QA & Test Automation  
**Tool:** `enumerate_boundaries`

## Focused Responsibility
Generates boundary, empty, unicode, and timezone DST test vectors.

## Contract
- **Input (`field_schema`):** string
- **Output (`edge_cases`):** string, `tool_used` (`enumerate_boundaries`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_edge_case_hunter`)
