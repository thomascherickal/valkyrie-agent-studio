# Backfill Orchestrator (`08-backfill-orchestrator`)

**Role:** Data Engineering  
**Tool:** `chunk_date_windows`

## Focused Responsibility
Splits multi-year backfills into safe rate-limited date chunks.

## Contract
- **Input (`backfill_window`):** string
- **Output (`backfill_plan`):** string, `tool_used` (`chunk_date_windows`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_backfill_orchestrator`)
