# Data Catalog Documenter (`20-catalog-documenter`)

**Role:** Data Engineering
**Tool:** `document_dataset`

## Focused Responsibility
Writes data catalog entries with definitions, lineage, quality status, and access guidance.

## Contract
- **Input (`table_metadata`):** string
- **Output (`catalog_entry`):** string, `tool_used` (`document_dataset`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_catalog_documenter`)
