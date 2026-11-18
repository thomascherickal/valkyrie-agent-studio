# PR Code Reviewer (`02-pr-code-reviewer`)

**Role:** Software Engineering  
**Tool:** `detect_antipatterns`

## Focused Responsibility
Inspects code diffs for boundary bugs, resource leaks, and missing tests.

## Contract
- **Input (`diff_snippet`):** string
- **Output (`review_comments`):** string, `tool_used` (`detect_antipatterns`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_pr_code_reviewer`)
