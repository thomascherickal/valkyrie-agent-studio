# Escalation Packager (`03-escalation-packager`)

**Role:** Technical Support  
**Tool:** `package_l3_handoff`

## Focused Responsibility
Assembles clean L3 engineering repro bundles with env & trace IDs.

## Contract
- **Input (`case_notes`):** string
- **Output (`escalation_card`):** string, `tool_used` (`package_l3_handoff`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_escalation_packager`)
