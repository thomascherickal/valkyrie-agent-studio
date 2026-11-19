# Cloud Posture Reviewer (`17-cloud-posture-reviewer`)

**Role:** Security & AppSec
**Tool:** `review_cloud_posture`

## Focused Responsibility
Reviews cloud configuration for public exposure, identity risks, logging gaps, and drift.

## Contract
- **Input (`cloud_config`):** string
- **Output (`posture_report`):** string, `tool_used` (`review_cloud_posture`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_17_cloud_posture_reviewer`)
