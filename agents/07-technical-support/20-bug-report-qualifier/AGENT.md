# Bug Report Qualifier (`20-bug-report-qualifier`)

**Role:** Technical Support
**Tool:** `qualify_bug_report`

## Focused Responsibility
Qualifies customer bug reports for reproducibility, severity, and engineering handoff.

## Contract
- **Input (`customer_report`):** string
- **Output (`qualified_bug`):** string, `tool_used` (`qualify_bug_report`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_bug_report_qualifier`)
