# CSAT Feedback Analyst (`16-csat-feedback-analyst`)

**Role:** Technical Support
**Tool:** `analyze_csat`

## Focused Responsibility
Analyzes CSAT scores and comments for themes, drivers, and agent coaching signals.

## Contract
- **Input (`csat_comments`):** string
- **Output (`csat_insights`):** string, `tool_used` (`analyze_csat`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_csat_feedback_analyst`)
