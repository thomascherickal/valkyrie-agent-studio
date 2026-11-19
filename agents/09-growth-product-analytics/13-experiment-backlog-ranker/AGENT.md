# Experiment Backlog Ranker (`13-experiment-backlog-ranker`)

**Role:** Growth & Product Analytics
**Tool:** `rank_experiments`

## Focused Responsibility
Ranks growth experiments by impact, confidence, and effort with traffic and runtime checks.

## Contract
- **Input (`experiment_ideas`):** string
- **Output (`ranked_backlog`):** string, `tool_used` (`rank_experiments`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_experiment_backlog_ranker`)
