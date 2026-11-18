# SOC2 Evidence Collector (`06-soc2-evidence-collector`)

**Role:** Security & AppSec  
**Tool:** `collect_control_proof`

## Focused Responsibility
Maps CC6/CC7 controls to CI logs, PR approvals, and backup proofs.

## Contract
- **Input (`control_id`):** string
- **Output (`evidence_bundle`):** string, `tool_used` (`collect_control_proof`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_soc2_evidence_collector`)
