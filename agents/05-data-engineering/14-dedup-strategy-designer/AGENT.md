# Deduplication Strategy Designer (`14-dedup-strategy-designer`)

**Role:** Data Engineering
**Tool:** `design_dedup`

## Focused Responsibility
Designs deduplication rules for events and records with keys, windows, and survivorship.

## Contract
- **Input (`duplicate_report`):** string
- **Output (`dedup_plan`):** string, `tool_used` (`design_dedup`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_dedup_strategy_designer`)
