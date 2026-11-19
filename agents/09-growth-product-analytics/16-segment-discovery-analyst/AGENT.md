# Segment Discovery Analyst (`16-segment-discovery-analyst`)

**Role:** Growth & Product Analytics
**Tool:** `find_segments`

## Focused Responsibility
Finds customer segments from usage patterns and tests which segments retain and pay best.

## Contract
- **Input (`usage_summary`):** string
- **Output (`segment_findings`):** string, `tool_used` (`find_segments`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_segment_discovery_analyst`)
