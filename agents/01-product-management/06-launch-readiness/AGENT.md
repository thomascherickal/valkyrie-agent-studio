# Launch Readiness Coordinator (`06-launch-readiness`)

**Role:** Product Management  
**Tool:** `audit_launch_gates`

## Focused Responsibility
Audits GTM gates across engineering, docs, legal, and support sign-offs.

## Contract
- **Input (`checklist_state`):** string
- **Output (`readiness_status`):** string, `tool_used` (`audit_launch_gates`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_launch_readiness`)
