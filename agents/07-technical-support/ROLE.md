# Technical Support

Technical Support suite of 20 focused autonomous agents in Valkyrie Agent Studio.

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
- `11-refund-policy-checker` — **Refund Policy Checker**: Checks refund requests against policy windows, usage, and exceptions with a clear decision. (Tool: `check_refund_policy`)
- `12-support-reply-drafter` — **Customer Reply Drafter**: Drafts clear, empathetic support replies with the answer, next steps, and expectations set. (Tool: `draft_support_reply`)
- `13-duplicate-ticket-merger` — **Duplicate Ticket Merger**: Finds duplicate and related tickets and proposes safe merges with one owner. (Tool: `find_duplicate_tickets`)
- `14-outage-comms-writer` — **Outage Customer Comms Writer**: Writes timely customer updates during an outage with impact, workaround, and the next update time. (Tool: `write_outage_comms`)
- `15-macro-curator` — **Support Macro Curator**: Curates support macros by usage, quality, and outcome, and retires stale ones. (Tool: `curate_macros`)
- `16-csat-feedback-analyst` — **CSAT Feedback Analyst**: Analyzes CSAT scores and comments for themes, drivers, and agent coaching signals. (Tool: `analyze_csat`)
- `17-known-issue-matcher` — **Known Issue Matcher**: Matches a customer symptom report to known issues, workarounds, and fix status. (Tool: `match_known_issues`)
- `18-enterprise-response-planner` — **Enterprise Account Handler**: Plans responses for enterprise accounts with escalation, executive contacts, and recovery steps. (Tool: `plan_enterprise_response`)
- `19-support-capacity-planner` — **Support Capacity Planner**: Plans support staffing from ticket volume, handle time, shrinkage, and service targets. (Tool: `plan_support_staffing`)
- `20-bug-report-qualifier` — **Bug Report Qualifier**: Qualifies customer bug reports for reproducibility, severity, and engineering handoff. (Tool: `qualify_bug_report`)
