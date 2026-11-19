# Known Issue Matcher (`17-known-issue-matcher`)

**Role:** Technical Support
**Tool:** `match_known_issues`

## Focused Responsibility
Matches a customer symptom report to known issues, workarounds, and fix status.

## Contract
- **Input (`symptom_report`):** string
- **Output (`issue_match`):** string, `tool_used` (`match_known_issues`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_known_issue_matcher`)
