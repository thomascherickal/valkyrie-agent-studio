# Investor Update Writer (`06-investor-update-writer`)

**Role:** C-Suite & Executives (CxOs)  
**Tool:** `format_investor_email`

## Focused Responsibility
Drafts crisp monthly investor updates covering wins, metrics, and asks.

## Contract
- **Input (`monthly_highlights`):** string
- **Output (`investor_update`):** string, `tool_used` (`format_investor_email`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_investor_update_writer`)
