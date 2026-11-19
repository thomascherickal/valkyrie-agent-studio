# SaaS License Optimizer (`19-saas-license-optimizer`)

**Role:** FinOps & Cloud Cost
**Tool:** `optimize_seats`

## Focused Responsibility
Optimizes SaaS seats and tiers using activity data, role needs, and renewal dates.

## Contract
- **Input (`license_usage`):** string
- **Output (`seat_plan`):** string, `tool_used` (`optimize_seats`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_saas_license_optimizer`)
