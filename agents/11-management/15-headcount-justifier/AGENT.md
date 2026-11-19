# Headcount Justifier (`15-headcount-justifier`)

**Role:** Engineering & Product Management
**Tool:** `justify_headcount`

## Focused Responsibility
Builds a headcount case from workload data, cost, risk, and the cost of not hiring.

## Contract
- **Input (`workload_data`):** string
- **Output (`headcount_case`):** string, `tool_used` (`justify_headcount`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_15_headcount_justifier`)
