# Community Q&A Helper (`05-community-qa-helper`)

**Role:** Developer Relations & Docs  
**Tool:** `compose_community_reply`

## Focused Responsibility
Drafts accurate, welcoming answers for GitHub Discussions and Discord.

## Contract
- **Input (`question_text`):** string
- **Output (`reply_md`):** string, `tool_used` (`compose_community_reply`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_05_community_qa_helper`)
