# CEO Weekly Brief (`10-ceo-weekly-brief`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `compile_ceo_brief`

## Focused Responsibility
Synthesizes GTM, Eng, Finance, and People signals into a 3-min read.

## Contract
- **Input (`exec_inputs`):** string
- **Output (`weekly_brief_md`):** string, `tool_used` (`compile_ceo_brief`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_ceo_weekly_brief`)
