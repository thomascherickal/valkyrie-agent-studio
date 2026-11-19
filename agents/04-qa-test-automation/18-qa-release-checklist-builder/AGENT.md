# QA Release Checklist Builder (`18-qa-release-checklist-builder`)

**Role:** QA & Test Automation
**Tool:** `build_release_checklist`

## Focused Responsibility
Builds release checklists from scope, risk, and past escapes with clear sign-off gates.

## Contract
- **Input (`release_scope`):** string
- **Output (`qa_checklist`):** string, `tool_used` (`build_release_checklist`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_18_qa_release_checklist_builder`)
