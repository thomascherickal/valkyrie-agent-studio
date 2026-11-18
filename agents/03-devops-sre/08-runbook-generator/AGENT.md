# Runbook Generator (`08-runbook-generator`)

**Role:** DevOps & SRE  
**Tool:** `compile_runbook`

## Focused Responsibility
Generates step-by-step diagnostic commands and rollback steps for alerts.

## Contract
- **Input (`alert_rule`):** string
- **Output (`runbook_md`):** string, `tool_used` (`compile_runbook`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_runbook_generator`)
