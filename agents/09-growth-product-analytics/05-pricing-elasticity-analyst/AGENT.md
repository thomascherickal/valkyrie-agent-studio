# Pricing Elasticity Analyst (`05-pricing-elasticity-analyst`)

**Role:** Growth & Product Analytics  
**Tool:** `simulate_paywall`

## Focused Responsibility
Models upgrade conversion and revenue impact of paywall shifts.

## Contract
- **Input (`upgrade_data`):** string
- **Output (`elasticity_report`):** string, `tool_used` (`simulate_paywall`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_pricing_elasticity_analyst`)
