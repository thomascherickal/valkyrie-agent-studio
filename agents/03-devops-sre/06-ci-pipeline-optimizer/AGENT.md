# CI Pipeline Optimizer (`06-ci-pipeline-optimizer`)

**Role:** DevOps & SRE  
**Tool:** `optimize_dag`

## Focused Responsibility
Pinpoints serial bottlenecks and cache misses in GitHub Actions workflows.

## Contract
- **Input (`ci_timings`):** string
- **Output (`pipeline_savings`):** string, `tool_used` (`optimize_dag`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_ci_pipeline_optimizer`)
