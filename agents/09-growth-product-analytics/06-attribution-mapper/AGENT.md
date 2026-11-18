# Attribution Mapper (`06-attribution-mapper`)

**Role:** Growth & Product Analytics  
**Tool:** `compute_channel_roi`

## Focused Responsibility
Compares first-touch vs linear multi-touch CAC across channels.

## Contract
- **Input (`channel_spend`):** string
- **Output (`attribution_table`):** string, `tool_used` (`compute_channel_roi`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_attribution_mapper`)
