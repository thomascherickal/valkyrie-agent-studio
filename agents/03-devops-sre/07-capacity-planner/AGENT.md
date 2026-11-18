# Capacity Planner (`07-capacity-planner`)

**Role:** DevOps & SRE  
**Tool:** `model_headroom`

## Focused Responsibility
Projects compute and memory headroom from peak QPS growth curves.

## Contract
- **Input (`traffic_forecast`):** string
- **Output (`scaling_plan`):** string, `tool_used` (`model_headroom`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_capacity_planner`)
