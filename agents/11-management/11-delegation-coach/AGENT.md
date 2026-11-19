# Delegation Coach (`11-delegation-coach`)

**Role:** Engineering & Product Management
**Tool:** `plan_delegation`

## Focused Responsibility
Coaches managers on what to delegate, to whom, and how much guidance and authority to give.

## Contract
- **Input (`task_list`):** string
- **Output (`delegation_plan`):** string, `tool_used` (`plan_delegation`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_11_delegation_coach`)
