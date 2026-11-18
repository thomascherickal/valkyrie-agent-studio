# Incident Commander (`01-incident-commander`)

**Role:** DevOps & SRE  
**Tool:** `build_ics_timeline`

## Focused Responsibility
Structures SEV-1/SEV-2 triage roles, timelines, and mitigation actions.

## Contract
- **Input (`alert_payload`):** string
- **Output (`command_plan`):** string, `tool_used` (`build_ics_timeline`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_incident_commander`)
