# Refactor Planner (`03-refactor-planner`)

**Role:** Software Engineering  
**Tool:** `plan_strangler_steps`

## Focused Responsibility
Plans incremental strangler-fig extractions without breaking public callers.

## Contract
- **Input (`module_metrics`):** string
- **Output (`refactor_plan`):** string, `tool_used` (`plan_strangler_steps`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_refactor_planner`)
