# Rollback Verifier (`10-rollback-verifier`)

**Role:** DevOps & SRE  
**Tool:** `eval_canary_gate`

## Focused Responsibility
Evaluates canary error/latency deltas to trigger automated rollbacks.

## Contract
- **Input (`canary_stats`):** string
- **Output (`rollback_action`):** string, `tool_used` (`eval_canary_gate`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_10_rollback_verifier`)
