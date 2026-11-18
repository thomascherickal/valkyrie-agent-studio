# Budget Alert Router (`09-budget-alert-router`)

**Role:** FinOps & Cloud Cost  
**Tool:** `route_budget_warning`

## Focused Responsibility
Routes forecasted monthly overruns to squad Slack/email owners.

## Contract
- **Input (`budget_status`):** string
- **Output (`alert_payload`):** string, `tool_used` (`route_budget_warning`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_09_budget_alert_router`)
