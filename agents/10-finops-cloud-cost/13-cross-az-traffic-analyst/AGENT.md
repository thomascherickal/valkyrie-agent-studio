# Cross-AZ Traffic Analyst (`13-cross-az-traffic-analyst`)

**Role:** FinOps & Cloud Cost
**Tool:** `analyze_az_traffic`

## Focused Responsibility
Analyzes cross-zone and cross-region data transfer and proposes locality fixes.

## Contract
- **Input (`traffic_matrix`):** string
- **Output (`az_plan`):** string, `tool_used` (`analyze_az_traffic`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_cross_az_traffic_analyst`)
