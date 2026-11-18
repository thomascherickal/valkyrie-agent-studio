# Accessibility Auditor (`08-accessibility-auditor`)

**Role:** QA & Test Automation  
**Tool:** `audit_wcag_aa`

## Focused Responsibility
Audits DOM markup for landmarks, contrast, focus order, and ARIA.

## Contract
- **Input (`html_snippet`):** string
- **Output (`a11y_issues`):** string, `tool_used` (`audit_wcag_aa`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_accessibility_auditor`)
