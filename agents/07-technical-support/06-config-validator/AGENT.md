# Config Validator (`06-config-validator`)

**Role:** Technical Support  
**Tool:** `validate_customer_yaml`

## Focused Responsibility
Validates customer agent.ir.yaml snippets and pinpoints syntax errors.

## Contract
- **Input (`yaml_snippet`):** string
- **Output (`validation_hints`):** string, `tool_used` (`validate_customer_yaml`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_06_config_validator`)
