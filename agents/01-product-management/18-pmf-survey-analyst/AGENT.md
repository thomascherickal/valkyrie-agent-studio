# PMF Survey Analyst (`18-pmf-survey-analyst`)

**Role:** Product Management
**Tool:** `score_pmf_survey`

## Focused Responsibility
Scores the product-market fit survey and reads the segments that would miss the product most.

## Contract
- **Input (`survey_counts`):** string
- **Output (`pmf_readout`):** string, `tool_used` (`score_pmf_survey`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_pmf_survey_analyst`)
