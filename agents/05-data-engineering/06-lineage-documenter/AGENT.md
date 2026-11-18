# Lineage Documenter (`06-lineage-documenter`)

**Role:** Data Engineering  
**Tool:** `trace_column_lineage`

## Focused Responsibility
Traces column-level provenance from raw ingestion to BI metrics.

## Contract
- **Input (`sql_graph`):** string
- **Output (`lineage_map`):** string, `tool_used` (`trace_column_lineage`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_lineage_documenter`)
