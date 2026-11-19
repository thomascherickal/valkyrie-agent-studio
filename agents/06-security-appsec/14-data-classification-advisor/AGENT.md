# Data Classification Advisor (`14-data-classification-advisor`)

**Role:** Security & AppSec
**Tool:** `classify_data`

## Focused Responsibility
Classifies data stores by sensitivity and maps required controls for each class.

## Contract
- **Input (`data_inventory`):** string
- **Output (`classification_map`):** string, `tool_used` (`classify_data`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_data_classification_advisor`)
