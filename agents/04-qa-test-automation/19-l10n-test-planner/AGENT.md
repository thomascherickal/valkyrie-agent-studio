# Localization Test Planner (`19-l10n-test-planner`)

**Role:** QA & Test Automation
**Tool:** `plan_locale_tests`

## Focused Responsibility
Plans localization and internationalization tests for locales, text expansion, and formats.

## Contract
- **Input (`locale_list`):** string
- **Output (`l10n_plan`):** string, `tool_used` (`plan_locale_tests`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_l10n_test_planner`)
