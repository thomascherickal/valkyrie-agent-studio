# Container Hardener (`08-container-hardener`)

**Role:** Security & AppSec  
**Tool:** `lint_dockerfile`

## Focused Responsibility
Audits Dockerfiles for non-root USER, pinned digests, and multi-stage.

## Contract
- **Input (`dockerfile_text`):** string
- **Output (`hardened_diff`):** string, `tool_used` (`lint_dockerfile`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_08_container_hardener`)
