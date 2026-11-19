# Mutation Test Reviewer (`13-mutation-test-reviewer`)

**Role:** QA & Test Automation
**Tool:** `review_mutation_survivors`

## Focused Responsibility
Reviews mutation testing results and turns surviving mutants into targeted tests.

## Contract
- **Input (`mutation_report`):** string
- **Output (`survivor_actions`):** string, `tool_used` (`review_mutation_survivors`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_13_mutation_test_reviewer`)
