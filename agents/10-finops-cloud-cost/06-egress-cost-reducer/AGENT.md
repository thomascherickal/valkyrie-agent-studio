# Egress Cost Reducer (`06-egress-cost-reducer`)

**Role:** FinOps & Cloud Cost  
**Tool:** `find_egress_leaks`

## Focused Responsibility
Identifies cross-AZ chatty services and missing VPC endpoints.

## Contract
- **Input (`network_flow`):** string
- **Output (`network_fixes`):** string, `tool_used` (`find_egress_leaks`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_egress_cost_reducer`)
