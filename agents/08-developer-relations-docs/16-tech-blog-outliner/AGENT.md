# Technical Blog Outliner (`16-tech-blog-outliner`)

**Role:** Developer Relations & Docs
**Tool:** `outline_tech_post`

## Focused Responsibility
Outlines technical posts with a clear thesis, reader level, sections, and runnable proof.

## Contract
- **Input (`topic_brief`):** string
- **Output (`post_outline`):** string, `tool_used` (`outline_tech_post`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_16_tech_blog_outliner`)
