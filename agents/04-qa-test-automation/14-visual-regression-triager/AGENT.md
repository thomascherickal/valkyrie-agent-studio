# Visual Regression Triager (`14-visual-regression-triager`)

**Role:** QA & Test Automation
**Tool:** `triage_visual_diffs`

## Focused Responsibility
Triages screenshot diffs into real regressions, intended changes, and flaky rendering.

## Contract
- **Input (`screenshot_diffs`):** string
- **Output (`visual_triage`):** string, `tool_used` (`triage_visual_diffs`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_visual_regression_triager`)
