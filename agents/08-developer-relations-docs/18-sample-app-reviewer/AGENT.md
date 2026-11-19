# Sample App Reviewer (`18-sample-app-reviewer`)

**Role:** Developer Relations & Docs
**Tool:** `review_sample_app`

## Focused Responsibility
Reviews sample applications for clarity, security, correctness, and ease of running.

## Contract
- **Input (`sample_readme`):** string
- **Output (`sample_review`):** string, `tool_used` (`review_sample_app`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_sample_app_reviewer`)
