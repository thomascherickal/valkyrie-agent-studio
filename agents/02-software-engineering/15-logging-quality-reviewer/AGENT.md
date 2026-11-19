# Logging Quality Reviewer (`15-logging-quality-reviewer`)

**Role:** Software Engineering
**Tool:** `review_log_statements`

## Focused Responsibility
Reviews log statements for structure, levels, sensitive data, noise, and missing context.

## Contract
- **Input (`log_samples`):** string
- **Output (`logging_review`):** string, `tool_used` (`review_log_statements`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_logging_quality_reviewer`)
