# Incident Forensics Guide (`13-forensics-guide`)

**Role:** Security & AppSec
**Tool:** `plan_forensics`

## Focused Responsibility
Guides digital forensics collection with evidence order, preservation, and chain of custody.

## Contract
- **Input (`incident_summary`):** string
- **Output (`forensics_plan`):** string, `tool_used` (`plan_forensics`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_forensics_guide`)
