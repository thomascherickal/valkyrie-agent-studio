# Storage Tiering Planner (`07-storage-tiering-planner`)

**Role:** FinOps & Cloud Cost  
**Tool:** `design_lifecycle_rule`

## Focused Responsibility
Recommends S3 Intelligent-Tiering and Glacier lifecycle rules.

## Contract
- **Input (`bucket_stats`):** string
- **Output (`storage_savings`):** string, `tool_used` (`design_lifecycle_rule`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_07_storage_tiering_planner`)
