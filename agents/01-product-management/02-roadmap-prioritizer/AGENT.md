# Roadmap Prioritizer (`02-roadmap-prioritizer`)

**Role:** Product Management  
**Tool:** `compute_rice_score`

## Focused Responsibility
Scores backlog items using RICE (Reach, Impact, Confidence, Effort) and outputs ranked tiers.

## Contract
- **Input (`initiatives`):** string
- **Output (`ranked_roadmap`):** string, `tool_used` (`compute_rice_score`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_02_roadmap_prioritizer`)
