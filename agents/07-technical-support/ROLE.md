# Technical Support

Technical Support suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-ticket-triager` — **Ticket Triager**: Routes tickets by urgency, product module, and enterprise SLA tier. (Tool: `classify_ticket_sla`)
- `02-log-bundle-analyzer` — **Log Bundle Analyzer**: Extracts root-cause exceptions and timestamps from diagnostic logs. (Tool: `extract_root_exception`)
- `03-escalation-packager` — **Escalation Packager**: Assembles clean L3 engineering repro bundles with env & trace IDs. (Tool: `package_l3_handoff`)
- `04-kb-article-drafter` — **KB Article Drafter**: Converts resolved support threads into searchable troubleshooting guides. (Tool: `format_kb_markdown`)
- `05-sla-breach-predictor` — **SLA Breach Predictor**: Flags open tickets approaching first-response or resolution deadlines. (Tool: `score_sla_risk`)
- `06-config-validator` — **Config Validator**: Validates customer agent.ir.yaml snippets and pinpoints syntax errors. (Tool: `validate_customer_yaml`)
- `07-api-error-explainer` — **API Error Explainer**: Translates raw HTTP 4xx/5xx error payloads into plain-English fixes. (Tool: `explain_api_error`)
- `08-onboarding-concierge` — **Onboarding Concierge**: Builds tailored 7-day setup checklists for new enterprise teams. (Tool: `generate_setup_plan`)
- `09-churn-signal-spotter` — **Churn Signal Spotter**: Detects repeat escalations and sentiment drops across account history. (Tool: `compute_churn_risk`)
- `10-status-page-updater` — **Status Page Updater**: Writes clear, accurate incident updates without internal jargon. (Tool: `draft_status_update`)
