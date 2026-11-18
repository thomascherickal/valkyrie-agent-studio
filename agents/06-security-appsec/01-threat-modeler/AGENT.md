# Threat Modeler (`01-threat-modeler`)

**Role:** Security & AppSec  
**Tool:** `run_stride_analysis`

## Focused Responsibility
Runs STRIDE threat modeling across trust boundaries and data flows.

## Contract
- **Input (`architecture_desc`):** string
- **Output (`threat_matrix`):** string, `tool_used` (`run_stride_analysis`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_01_threat_modeler`)
