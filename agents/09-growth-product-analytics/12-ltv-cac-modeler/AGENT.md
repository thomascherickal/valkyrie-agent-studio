# LTV to CAC Modeler (`12-ltv-cac-modeler`)

**Role:** Growth & Product Analytics
**Tool:** `model_ltv_cac`

## Focused Responsibility
Models customer lifetime value against acquisition cost with payback and sensitivity to churn.

## Contract
- **Input (`unit_inputs`):** string
- **Output (`ltv_cac_readout`):** string, `tool_used` (`model_ltv_cac`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_ltv_cac_modeler`)
