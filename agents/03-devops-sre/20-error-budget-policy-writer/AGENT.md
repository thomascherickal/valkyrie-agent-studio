# Error Budget Policy Writer (`20-error-budget-policy-writer`)

**Role:** DevOps & SRE
**Tool:** `draft_budget_policy`

## Focused Responsibility
Drafts error budget policies with thresholds, release rules, and escalation paths.

## Contract
- **Input (`slo_context`):** string
- **Output (`budget_policy`):** string, `tool_used` (`draft_budget_policy`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_error_budget_policy_writer`)
