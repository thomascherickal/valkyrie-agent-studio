# Helm Chart Reviewer (`14-helm-chart-reviewer`)

**Role:** DevOps & SRE
**Tool:** `review_helm_values`

## Focused Responsibility
Reviews Helm values and templates for safe defaults, resource limits, and upgrade risks.

## Contract
- **Input (`helm_values`):** string
- **Output (`chart_review`):** string, `tool_used` (`review_helm_values`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_helm_chart_reviewer`)
