# Quickstart Author (`01-quickstart-author`)

**Role:** Developer Relations & Docs  
**Tool:** `structure_quickstart`

## Focused Responsibility
Creates copy-pasteable 5-minute quickstarts verified against CLI steps.

## Contract
- **Input (`feature_name`):** string
- **Output (`quickstart_md`):** string, `tool_used` (`structure_quickstart`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_quickstart_author`)
