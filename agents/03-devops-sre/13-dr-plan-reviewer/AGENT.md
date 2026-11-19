# Disaster Recovery Reviewer (`13-dr-plan-reviewer`)

**Role:** DevOps & SRE
**Tool:** `review_dr_plan`

## Focused Responsibility
Reviews disaster recovery plans against RTO, RPO, backups, dependencies, and test evidence.

## Contract
- **Input (`dr_plan`):** string
- **Output (`dr_gaps`):** string, `tool_used` (`review_dr_plan`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_dr_plan_reviewer`)
