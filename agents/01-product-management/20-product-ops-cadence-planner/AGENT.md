# Product Ops Cadence Planner (`20-product-ops-cadence-planner`)

**Role:** Product Management
**Tool:** `plan_product_ops_cadence`

## Focused Responsibility
Designs the weekly, monthly, and quarterly meeting and reporting rhythm for product teams.

## Contract
- **Input (`team_rituals`):** string
- **Output (`ops_cadence`):** string, `tool_used` (`plan_product_ops_cadence`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_product_ops_cadence_planner`)
