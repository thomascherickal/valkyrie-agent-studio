# Enterprise Account Handler (`18-enterprise-response-planner`)

**Role:** Technical Support
**Tool:** `plan_enterprise_response`

## Focused Responsibility
Plans responses for enterprise accounts with escalation, executive contacts, and recovery steps.

## Contract
- **Input (`account_issue`):** string
- **Output (`escalation_path`):** string, `tool_used` (`plan_enterprise_response`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_enterprise_response_planner`)
