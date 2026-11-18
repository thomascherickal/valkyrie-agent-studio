# Idle Resource Reaper (`03-idle-resource-reaper`)

**Role:** FinOps & Cloud Cost  
**Tool:** `flag_idle_assets`

## Focused Responsibility
Lists unattached EBS volumes, idle load balancers, and zombie VMs.

## Contract
- **Input (`infra_inventory`):** string
- **Output (`reap_candidates`):** string, `tool_used` (`flag_idle_assets`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_idle_resource_reaper`)
