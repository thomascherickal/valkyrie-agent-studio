# Coverage Gap Finder (`06-coverage-gap-finder`)

**Role:** QA & Test Automation  
**Tool:** `propose_branch_tests`

## Focused Responsibility
Parses uncovered branch lines and drafts targeted unit tests.

## Contract
- **Input (`coverage_report`):** string
- **Output (`missing_tests`):** string, `tool_used` (`propose_branch_tests`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_coverage_gap_finder`)
