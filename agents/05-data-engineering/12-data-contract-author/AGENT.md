# Data Contract Author (`12-data-contract-author`)

**Role:** Data Engineering
**Tool:** `draft_data_contract`

## Focused Responsibility
Drafts data contracts with schema, semantics, quality rules, ownership, and change process.

## Contract
- **Input (`dataset_spec`):** string
- **Output (`contract_doc`):** string, `tool_used` (`draft_data_contract`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_12_data_contract_author`)
