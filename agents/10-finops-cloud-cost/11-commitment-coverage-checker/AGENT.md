# Commitment Coverage Checker (`11-commitment-coverage-checker`)

**Role:** FinOps & Cloud Cost
**Tool:** `check_commitment_coverage`

## Focused Responsibility
Checks reserved capacity and savings plan coverage and utilization against steady usage.

## Contract
- **Input (`usage_summary`):** string
- **Output (`coverage_report`):** string, `tool_used` (`check_commitment_coverage`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_commitment_coverage_checker`)
