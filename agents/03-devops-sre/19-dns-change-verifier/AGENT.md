# DNS Change Verifier (`19-dns-change-verifier`)

**Role:** DevOps & SRE
**Tool:** `verify_dns_change`

## Focused Responsibility
Checks planned DNS changes for TTLs, propagation risk, records, and rollback readiness.

## Contract
- **Input (`dns_change`):** string
- **Output (`dns_checklist`):** string, `tool_used` (`verify_dns_change`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_19_dns_change_verifier`)
