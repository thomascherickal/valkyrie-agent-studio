# Security Advisory Writer (`10-security-advisory-writer`)

**Role:** Security & AppSec  
**Tool:** `format_advisory_md`

## Focused Responsibility
Drafts transparent CVE advisories with affected versions and mitigations.

## Contract
- **Input (`advisory_input`):** string
- **Output (`advisory_doc`):** string, `tool_used` (`format_advisory_md`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_security_advisory_writer`)
