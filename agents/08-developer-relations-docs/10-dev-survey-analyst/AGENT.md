# Dev Survey Analyst (`10-dev-survey-analyst`)

**Role:** Developer Relations & Docs  
**Tool:** `summarize_dx_metrics`

## Focused Responsibility
Quantifies DX friction points across onboarding, docs, and SDKs.

## Contract
- **Input (`survey_responses`):** string
- **Output (`dx_report`):** string, `tool_used` (`summarize_dx_metrics`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_dev_survey_analyst`)
