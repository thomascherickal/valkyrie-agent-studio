# North Star Metric Designer (`14-north-star-designer`)

**Role:** Product Management
**Tool:** `define_north_star`

## Focused Responsibility
Chooses a north star metric and breaks it into input metrics teams can move.

## Contract
- **Input (`product_goals`):** string
- **Output (`metric_tree`):** string, `tool_used` (`define_north_star`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_14_north_star_designer`)
