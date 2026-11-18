# LLM Token Optimizer (`05-llm-token-optimizer`)

**Role:** FinOps & Cloud Cost  
**Tool:** `recommend_model_tier`

## Focused Responsibility
Routes simple tasks to gemini-4-hydrogen (low) and trims prompt bloat.

## Contract
- **Input (`llm_usage`):** string
- **Output (`token_savings`):** string, `tool_used` (`recommend_model_tier`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_llm_token_optimizer`)
