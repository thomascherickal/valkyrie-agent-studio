# Feature Flag Cleaner (`13-feature-flag-cleaner`)

**Role:** Software Engineering
**Tool:** `find_stale_flags`

## Focused Responsibility
Finds stale feature flags and plans safe removal with owners, tests, and rollout checks.

## Contract
- **Input (`flag_inventory`):** string
- **Output (`cleanup_plan`):** string, `tool_used` (`find_stale_flags`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_feature_flag_cleaner`)
