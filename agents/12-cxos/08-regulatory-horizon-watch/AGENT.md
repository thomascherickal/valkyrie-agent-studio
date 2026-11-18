# Regulatory Horizon Watcher (`08-regulatory-horizon-watch`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `map_compliance_gaps`

## Focused Responsibility
Maps EU AI Act, SOC2, and GDPR updates to product roadmap controls.

## Contract
- **Input (`policy_scope`):** string
- **Output (`regulatory_brief`):** string, `tool_used` (`map_compliance_gaps`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_regulatory_horizon_watch`)
