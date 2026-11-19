# Developer Webinar Planner (`17-webinar-planner`)

**Role:** Developer Relations & Docs
**Tool:** `plan_webinar`

## Focused Responsibility
Plans developer webinars with topic, run of show, demo safety, promotion, and follow-up.

## Contract
- **Input (`webinar_brief`):** string
- **Output (`webinar_plan`):** string, `tool_used` (`plan_webinar`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_webinar_planner`)
