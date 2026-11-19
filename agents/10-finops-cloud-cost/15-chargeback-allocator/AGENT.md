# Chargeback Allocator (`15-chargeback-allocator`)

**Role:** FinOps & Cloud Cost
**Tool:** `allocate_shared_cost`

## Focused Responsibility
Allocates shared cloud and platform costs to teams with fair, explainable drivers.

## Contract
- **Input (`shared_costs`):** string
- **Output (`allocation_table`):** string, `tool_used` (`allocate_shared_cost`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_chargeback_allocator`)
