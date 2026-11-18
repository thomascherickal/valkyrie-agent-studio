# Dependency Auditor (`06-dependency-auditor`)

**Role:** Software Engineering  
**Tool:** `scan_licenses`

## Focused Responsibility
Checks lockfiles for unmaintained packages, license conflicts, and bloat.

## Contract
- **Input (`dependencies`):** string
- **Output (`audit_report`):** string, `tool_used` (`scan_licenses`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_dependency_auditor`)
