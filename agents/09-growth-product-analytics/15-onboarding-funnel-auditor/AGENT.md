# Onboarding Funnel Auditor (`15-onboarding-funnel-auditor`)

**Role:** Growth & Product Analytics
**Tool:** `audit_onboarding`

## Focused Responsibility
Audits onboarding steps for friction, time to value, and the biggest drop-off.

## Contract
- **Input (`onboarding_steps`):** string
- **Output (`onboarding_audit`):** string, `tool_used` (`audit_onboarding`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_onboarding_funnel_auditor`)
