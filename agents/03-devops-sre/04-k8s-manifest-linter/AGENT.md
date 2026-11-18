# Kubernetes Manifest Linter (`04-k8s-manifest-linter`)

**Role:** DevOps & SRE  
**Tool:** `lint_k8s_spec`

## Focused Responsibility
Checks deployments for missing probes, limits, and PodDisruptionBudgets.

## Contract
- **Input (`k8s_yaml`):** string
- **Output (`lint_findings`):** string, `tool_used` (`lint_k8s_spec`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_k8s_manifest_linter`)
