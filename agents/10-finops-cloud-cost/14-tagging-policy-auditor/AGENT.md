# Tagging Policy Auditor (`14-tagging-policy-auditor`)

**Role:** FinOps & Cloud Cost
**Tool:** `audit_tags`

## Focused Responsibility
Audits cloud resource tags for cost allocation coverage, consistency, and owner accuracy.

## Contract
- **Input (`resource_tags`):** string
- **Output (`tag_report`):** string, `tool_used` (`audit_tags`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_tagging_policy_auditor`)
