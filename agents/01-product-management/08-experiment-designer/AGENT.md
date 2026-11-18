# Experiment Designer (`08-experiment-designer`)

**Role:** Product Management  
**Tool:** `calc_ab_sample_size`

## Focused Responsibility
Formulates A/B test hypotheses, MDE sample sizes, and guardrail metrics.

## Contract
- **Input (`hypothesis`):** string
- **Output (`experiment_spec`):** string, `tool_used` (`calc_ab_sample_size`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_experiment_designer`)
