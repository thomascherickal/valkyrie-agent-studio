# Spot Instance Advisor (`12-spot-instance-advisor`)

**Role:** FinOps & Cloud Cost
**Tool:** `assess_spot_fit`

## Focused Responsibility
Assesses which workloads can run on spot capacity and designs interruption handling.

## Contract
- **Input (`workload_profile`):** string
- **Output (`spot_plan`):** string, `tool_used` (`assess_spot_fit`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_spot_instance_advisor`)
