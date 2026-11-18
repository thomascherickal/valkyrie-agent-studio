# A/B Test Interpreter (`03-ab-test-interpreter`)

**Role:** Growth & Product Analytics  
**Tool:** `evaluate_ab_stats`

## Focused Responsibility
Checks p-values, confidence intervals, and sample ratio mismatch.

## Contract
- **Input (`ab_results`):** string
- **Output (`experiment_verdict`):** string, `tool_used` (`evaluate_ab_stats`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_ab_test_interpreter`)
