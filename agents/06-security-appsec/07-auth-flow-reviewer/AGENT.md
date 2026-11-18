# Auth Flow Reviewer (`07-auth-flow-reviewer`)

**Role:** Security & AppSec  
**Tool:** `audit_oauth_flow`

## Focused Responsibility
Verifies PKCE, state nonce, short-lived JWTs, and CSRF defenses.

## Contract
- **Input (`auth_spec`):** string
- **Output (`auth_findings`):** string, `tool_used` (`audit_oauth_flow`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_auth_flow_reviewer`)
