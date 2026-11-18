# User Story Splitter (`03-user-story-splitter`)

**Role:** Product Management  
**Tool:** `split_invest_stories`

## Focused Responsibility
Decomposes large epics into INVEST-compliant stories with Given/When/Then criteria.

## Contract
- **Input (`epic_text`):** string
- **Output (`stories`):** string, `tool_used` (`split_invest_stories`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_user_story_splitter`)
