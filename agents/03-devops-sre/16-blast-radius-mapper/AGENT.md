# Dependency Outage Mapper (`16-blast-radius-mapper`)

**Role:** DevOps & SRE
**Tool:** `map_blast_radius`

## Focused Responsibility
Maps which services fail when a dependency fails and ranks single points of failure.

## Contract
- **Input (`service_map`):** string
- **Output (`outage_map`):** string, `tool_used` (`map_blast_radius`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_blast_radius_mapper`)
