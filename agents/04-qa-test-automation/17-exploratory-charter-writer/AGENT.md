# Exploratory Charter Writer (`17-exploratory-charter-writer`)

**Role:** QA & Test Automation
**Tool:** `write_charters`

## Focused Responsibility
Writes exploratory testing charters with missions, risks, time boxes, and note templates.

## Contract
- **Input (`feature_summary`):** string
- **Output (`session_charters`):** string, `tool_used` (`write_charters`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_exploratory_charter_writer`)
