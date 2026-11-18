# Architecture Reviewer (`01-architecture-reviewer`)

**Role:** Software Engineering  
**Tool:** `check_failure_modes`

## Focused Responsibility
Audits RFCs for single points of failure, coupling, and backpressure gaps.

## Contract
- **Input (`rfc_summary`):** string
- **Output (`review_findings`):** string, `tool_used` (`check_failure_modes`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_architecture_reviewer`)
