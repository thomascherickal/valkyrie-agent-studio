# Deploy Freeze Advisor (`17-deploy-freeze-advisor`)

**Role:** DevOps & SRE
**Tool:** `decide_freeze`

## Focused Responsibility
Decides whether to freeze deploys using change risk, error budget, and the event calendar.

## Contract
- **Input (`change_calendar`):** string
- **Output (`freeze_decision`):** string, `tool_used` (`decide_freeze`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_deploy_freeze_advisor`)
