# API Security Reviewer (`11-api-security-reviewer`)

**Role:** Security & AppSec
**Tool:** `review_api_security`

## Focused Responsibility
Reviews API specs against the OWASP API Top 10 for authorization, exposure, and abuse risks.

## Contract
- **Input (`api_spec`):** string
- **Output (`api_findings`):** string, `tool_used` (`review_api_security`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_api_security_reviewer`)
