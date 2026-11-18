# RI & Savings Plan Advisor (`04-ri-savings-planner`)

**Role:** FinOps & Cloud Cost  
**Tool:** `model_commitment_roi`

## Focused Responsibility
Models 1-year no-upfront Savings Plan coverage for steady baselines.

## Contract
- **Input (`compute_baseline`):** string
- **Output (`savings_plan`):** string, `tool_used` (`model_commitment_roi`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_ri_savings_planner`)
