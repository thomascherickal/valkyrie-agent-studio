# Cache Strategy Advisor (`16-cache-strategy-advisor`)

**Role:** Software Engineering
**Tool:** `design_cache_strategy`

## Focused Responsibility
Designs cache layers, keys, expiry, and invalidation from the observed access pattern.

## Contract
- **Input (`access_pattern`):** string
- **Output (`cache_design`):** string, `tool_used` (`design_cache_strategy`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_cache_strategy_advisor`)
