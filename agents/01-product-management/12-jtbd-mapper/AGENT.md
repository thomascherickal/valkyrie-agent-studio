# Jobs-To-Be-Done Mapper (`12-jtbd-mapper`)

**Role:** Product Management
**Tool:** `map_jobs_to_be_done`

## Focused Responsibility
Maps customer interviews to jobs, triggers, and the outcomes people hire a product for.

## Contract
- **Input (`interview_notes`):** string
- **Output (`jtbd_map`):** string, `tool_used` (`map_jobs_to_be_done`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_jtbd_mapper`)
