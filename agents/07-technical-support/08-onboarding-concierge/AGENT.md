# Onboarding Concierge (`08-onboarding-concierge`)

**Role:** Technical Support  
**Tool:** `generate_setup_plan`

## Focused Responsibility
Builds tailored 7-day setup checklists for new enterprise teams.

## Contract
- **Input (`customer_profile`):** string
- **Output (`onboarding_plan`):** string, `tool_used` (`generate_setup_plan`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_onboarding_concierge`)
