# API Contract Designer (`04-api-contract-designer`)

**Role:** Software Engineering  
**Tool:** `validate_openapi_diff`

## Focused Responsibility
Designs versioned REST/OpenAPI schemas and detects breaking field changes.

## Contract
- **Input (`endpoint_spec`):** string
- **Output (`contract_yaml`):** string, `tool_used` (`validate_openapi_diff`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_04_api_contract_designer`)
