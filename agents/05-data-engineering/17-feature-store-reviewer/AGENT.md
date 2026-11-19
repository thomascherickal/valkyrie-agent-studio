# Feature Store Reviewer (`17-feature-store-reviewer`)

**Role:** Data Engineering
**Tool:** `review_feature_store`

## Focused Responsibility
Reviews feature definitions for training and serving skew, leakage, freshness, and reuse.

## Contract
- **Input (`feature_specs`):** string
- **Output (`store_review`):** string, `tool_used` (`review_feature_store`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_feature_store_reviewer`)
