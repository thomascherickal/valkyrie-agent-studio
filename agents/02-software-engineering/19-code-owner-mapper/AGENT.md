# Code Ownership Mapper (`19-code-owner-mapper`)

**Role:** Software Engineering
**Tool:** `map_code_owners`

## Focused Responsibility
Maps files to owners from commit history and flags orphaned or overloaded areas.

## Contract
- **Input (`commit_history`):** string
- **Output (`owners_map`):** string, `tool_used` (`map_code_owners`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_code_owner_mapper`)
