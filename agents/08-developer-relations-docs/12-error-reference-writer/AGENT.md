# Error Reference Writer (`12-error-reference-writer`)

**Role:** Developer Relations & Docs
**Tool:** `write_error_reference`

## Focused Responsibility
Writes error reference pages with cause, fix, example, and links for each error code.

## Contract
- **Input (`error_catalog`):** string
- **Output (`error_reference`):** string, `tool_used` (`write_error_reference`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_error_reference_writer`)
