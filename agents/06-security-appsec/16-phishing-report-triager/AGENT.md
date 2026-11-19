# Phishing Report Triager (`16-phishing-report-triager`)

**Role:** Security & AppSec
**Tool:** `triage_phishing`

## Focused Responsibility
Triages reported phishing emails by indicators, impact, and required response actions.

## Contract
- **Input (`reported_email`):** string
- **Output (`phishing_verdict`):** string, `tool_used` (`triage_phishing`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_phishing_report_triager`)
