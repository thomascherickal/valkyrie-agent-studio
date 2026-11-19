# GPU Utilization Analyst (`20-gpu-utilization-analyst`)

**Role:** FinOps & Cloud Cost
**Tool:** `analyze_gpu_use`

## Focused Responsibility
Analyzes GPU utilization and queueing to cut idle accelerator spend and fix scheduling.

## Contract
- **Input (`gpu_metrics`):** string
- **Output (`gpu_plan`):** string, `tool_used` (`analyze_gpu_use`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_gpu_utilization_analyst`)
