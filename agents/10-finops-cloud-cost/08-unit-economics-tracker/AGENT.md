# Unit Economics Tracker (`08-unit-economics-tracker`)

**Role:** FinOps & Cloud Cost  
**Tool:** `calc_unit_cogs`

## Focused Responsibility
Calculates COGS per active tenant and per 1,000 agent invocations.

## Contract
- **Input (`cogs_inputs`):** string
- **Output (`unit_economics`):** string, `tool_used` (`calc_unit_cogs`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_unit_economics_tracker`)
