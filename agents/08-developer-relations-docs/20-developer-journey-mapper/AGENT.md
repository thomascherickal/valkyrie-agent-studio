# Developer Journey Mapper (`20-developer-journey-mapper`)

**Role:** Developer Relations & Docs
**Tool:** `map_developer_journey`

## Focused Responsibility
Maps the developer journey from discovery to production with friction, drop-off, and fixes.

## Contract
- **Input (`journey_notes`):** string
- **Output (`journey_map`):** string, `tool_used` (`map_developer_journey`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_developer_journey_mapper`)
