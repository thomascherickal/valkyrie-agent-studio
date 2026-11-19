# Codebase Onboarding Guide (`20-codebase-onboarding-guide`)

**Role:** Software Engineering
**Tool:** `write_onboarding_guide`

## Focused Responsibility
Writes a first-week onboarding guide for a repository with setup, code map, first task, and norms.

## Contract
- **Input (`repo_overview`):** string
- **Output (`onboarding_guide`):** string, `tool_used` (`write_onboarding_guide`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_20_codebase_onboarding_guide`)
