# Migration Guide Writer (`11-migration-guide-writer`)

**Role:** Developer Relations & Docs
**Tool:** `write_migration_guide`

## Focused Responsibility
Writes upgrade guides for breaking changes with before and after code and a safe order of steps.

## Contract
- **Input (`breaking_changes`):** string
- **Output (`migration_guide`):** string, `tool_used` (`write_migration_guide`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_migration_guide_writer`)
