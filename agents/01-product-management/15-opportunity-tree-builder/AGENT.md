# Opportunity Solution Tree Builder (`15-opportunity-tree-builder`)

**Role:** Product Management
**Tool:** `build_ost`

## Focused Responsibility
Builds an opportunity solution tree from an outcome, customer needs, and candidate solutions.

## Contract
- **Input (`desired_outcome`):** string
- **Output (`opportunity_tree`):** string, `tool_used` (`build_ost`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_opportunity_tree_builder`)
