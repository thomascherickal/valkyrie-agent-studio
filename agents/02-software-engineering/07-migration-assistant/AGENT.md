# Migration Assistant (`07-migration-assistant`)

**Role:** Software Engineering  
**Tool:** `gen_expand_contract`

## Focused Responsibility
Generates reversible expand-and-contract database migration scripts.

## Contract
- **Input (`schema_change`):** string
- **Output (`migration_sql`):** string, `tool_used` (`gen_expand_contract`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_migration_assistant`)
