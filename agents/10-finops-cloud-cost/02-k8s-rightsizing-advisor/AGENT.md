# K8s Rightsizing Advisor (`02-k8s-rightsizing-advisor`)

**Role:** FinOps & Cloud Cost  
**Tool:** `compute_rightsize`

## Focused Responsibility
Compares requested vs p95 actual CPU/RAM to trim cluster waste.

## Contract
- **Input (`pod_metrics`):** string
- **Output (`rightsize_patch`):** string, `tool_used` (`compute_rightsize`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_k8s_rightsizing_advisor`)
