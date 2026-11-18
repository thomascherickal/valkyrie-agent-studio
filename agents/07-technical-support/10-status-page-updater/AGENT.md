# Status Page Updater (`10-status-page-updater`)

**Role:** Technical Support  
**Tool:** `draft_status_update`

## Focused Responsibility
Writes clear, accurate incident updates without internal jargon.

## Contract
- **Input (`incident_state`):** string
- **Output (`status_message`):** string, `tool_used` (`draft_status_update`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_status_page_updater`)
