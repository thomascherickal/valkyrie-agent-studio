# Vendor Security Reviewer (`15-vendor-security-reviewer`)

**Role:** Security & AppSec
**Tool:** `review_vendor_security`

## Focused Responsibility
Reviews vendor security questionnaires and evidence to rate third-party risk.

## Contract
- **Input (`vendor_answers`):** string
- **Output (`vendor_risk`):** string, `tool_used` (`review_vendor_security`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_vendor_security_reviewer`)
