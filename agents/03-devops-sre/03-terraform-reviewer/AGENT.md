# Terraform Reviewer (`03-terraform-reviewer`)

**Role:** DevOps & SRE  
**Tool:** `inspect_tf_blast`

## Focused Responsibility
Flags destructive resource replacements and wildcard IAM policies in plans.

## Contract
- **Input (`tf_plan_diff`):** string
- **Output (`tf_verdict`):** string, `tool_used` (`inspect_tf_blast`), `confidence` (float)

## Runtime
- Python module: `agent.py`
- Rust crate: `rust/Cargo.toml` (`valkyrie_03_terraform_reviewer`)
