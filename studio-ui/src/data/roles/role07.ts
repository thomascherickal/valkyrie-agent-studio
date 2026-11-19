import type { RoleCatalog } from "../types";

export const ROLE_07: RoleCatalog = {
  "id": "07-technical-support",
  "name": "Technical Support",
  "agents": [
    {
      "id": "01-ticket-triager",
      "name": "Ticket Triager",
      "description": "Routes tickets by urgency, product module, and enterprise SLA tier.",
      "tool": "classify_ticket_sla",
      "inputKey": "ticket_text",
      "outputKey": "routing_decision",
      "sampleInput": "Enterprise prod down: SAML assertion signature mismatch"
    },
    {
      "id": "02-log-bundle-analyzer",
      "name": "Log Bundle Analyzer",
      "description": "Extracts root-cause exceptions and timestamps from diagnostic logs.",
      "tool": "extract_root_exception",
      "inputKey": "log_excerpt",
      "outputKey": "diagnostic_summary",
      "sampleInput": "2026-11-18T10:12Z ERROR ConnectionResetError upstream 502"
    },
    {
      "id": "03-escalation-packager",
      "name": "Escalation Packager",
      "description": "Assembles clean L3 engineering repro bundles with env & trace IDs.",
      "tool": "package_l3_handoff",
      "inputKey": "case_notes",
      "outputKey": "escalation_card",
      "sampleInput": "Customer v2.4.1 on Ubuntu 24.04; trace_id=tr_991a"
    },
    {
      "id": "04-kb-article-drafter",
      "name": "KB Article Drafter",
      "description": "Converts resolved support threads into searchable troubleshooting guides.",
      "tool": "format_kb_markdown",
      "inputKey": "resolution_notes",
      "outputKey": "kb_article",
      "sampleInput": "Fixed Ollama CORS by setting OLLAMA_ORIGINS=http://localhost:5173"
    },
    {
      "id": "05-sla-breach-predictor",
      "name": "SLA Breach Predictor",
      "description": "Flags open tickets approaching first-response or resolution deadlines.",
      "tool": "score_sla_risk",
      "inputKey": "queue_snapshot",
      "outputKey": "escalation_alerts",
      "sampleInput": "Ticket #8821: Enterprise P1, unassigned for 22m (SLA: 30m)"
    },
    {
      "id": "06-config-validator",
      "name": "Config Validator",
      "description": "Validates customer agent.ir.yaml snippets and pinpoints syntax errors.",
      "tool": "validate_customer_yaml",
      "inputKey": "yaml_snippet",
      "outputKey": "validation_hints",
      "sampleInput": "thinking_level: ultra # invalid enum"
    },
    {
      "id": "07-api-error-explainer",
      "name": "API Error Explainer",
      "description": "Translates raw HTTP 4xx/5xx error payloads into plain-English fixes.",
      "tool": "explain_api_error",
      "inputKey": "error_payload",
      "outputKey": "fix_guidance",
      "sampleInput": "429 RESOURCE_EXHAUSTED on gemini-4-hydrogen free tier"
    },
    {
      "id": "08-onboarding-concierge",
      "name": "Onboarding Concierge",
      "description": "Builds tailored 7-day setup checklists for new enterprise teams.",
      "tool": "generate_setup_plan",
      "inputKey": "customer_profile",
      "outputKey": "onboarding_plan",
      "sampleInput": "50-person eng org using GitHub, Okta, and Rust microservices"
    },
    {
      "id": "09-churn-signal-spotter",
      "name": "Churn Signal Spotter",
      "description": "Detects repeat escalations and sentiment drops across account history.",
      "tool": "compute_churn_risk",
      "inputKey": "thread_history",
      "outputKey": "csm_alert",
      "sampleInput": "3rd escalation this month on rate-limit errors; renewal in 21d"
    },
    {
      "id": "10-status-page-updater",
      "name": "Status Page Updater",
      "description": "Writes clear, accurate incident updates without internal jargon.",
      "tool": "draft_status_update",
      "inputKey": "incident_state",
      "outputKey": "status_message",
      "sampleInput": "Investigating elevated latency on US-West inference router"
    },
    {
      "id": "11-refund-policy-checker",
      "name": "Refund Policy Checker",
      "description": "Checks refund requests against policy windows, usage, and exceptions with a clear decision.",
      "tool": "check_refund_policy",
      "inputKey": "refund_request",
      "outputKey": "refund_decision",
      "sampleInput": "Annual plan bought 41 days ago, 3 logins, customer says the integration never worked; asks for full refund"
    },
    {
      "id": "12-support-reply-drafter",
      "name": "Customer Reply Drafter",
      "description": "Drafts clear, empathetic support replies with the answer, next steps, and expectations set.",
      "tool": "draft_support_reply",
      "inputKey": "ticket_thread",
      "outputKey": "reply_draft",
      "sampleInput": "Customer: webhooks stopped arriving since Tuesday, production orders are stuck. Second message, no reply for 6 hours"
    },
    {
      "id": "13-duplicate-ticket-merger",
      "name": "Duplicate Ticket Merger",
      "description": "Finds duplicate and related tickets and proposes safe merges with one owner.",
      "tool": "find_duplicate_tickets",
      "inputKey": "ticket_list",
      "outputKey": "merge_plan",
      "sampleInput": "9 tickets about login loops on iOS 17.4 since the 2.8 release; 4 from the same company; 2 mention the same error code"
    },
    {
      "id": "14-outage-comms-writer",
      "name": "Outage Customer Comms Writer",
      "description": "Writes timely customer updates during an outage with impact, workaround, and the next update time.",
      "tool": "write_outage_comms",
      "inputKey": "outage_facts",
      "outputKey": "customer_comms",
      "sampleInput": "Payments API errors for 22% of requests since 14:05 UTC; cause under investigation; card checkout affected"
    },
    {
      "id": "15-macro-curator",
      "name": "Support Macro Curator",
      "description": "Curates support macros by usage, quality, and outcome, and retires stale ones.",
      "tool": "curate_macros",
      "inputKey": "macro_usage",
      "outputKey": "macro_plan",
      "sampleInput": "312 macros; 40 used 80% of the time; 120 not used in a year; CSAT 3 points lower when macro 'Reset steps' is used"
    },
    {
      "id": "16-csat-feedback-analyst",
      "name": "CSAT Feedback Analyst",
      "description": "Analyzes CSAT scores and comments for themes, drivers, and agent coaching signals.",
      "tool": "analyze_csat",
      "inputKey": "csat_comments",
      "outputKey": "csat_insights",
      "sampleInput": "Responses 620, score 4.1; low scores cite slow replies and repeated questions; praise for clear steps"
    },
    {
      "id": "17-known-issue-matcher",
      "name": "Known Issue Matcher",
      "description": "Matches a customer symptom report to known issues, workarounds, and fix status.",
      "tool": "match_known_issues",
      "inputKey": "symptom_report",
      "outputKey": "issue_match",
      "sampleInput": "Export to PDF hangs at 95% for reports over 5,000 rows on Safari; started after the 3.2 release"
    },
    {
      "id": "18-enterprise-response-planner",
      "name": "Enterprise Account Handler",
      "description": "Plans responses for enterprise accounts with escalation, executive contacts, and recovery steps.",
      "tool": "plan_enterprise_response",
      "inputKey": "account_issue",
      "outputKey": "escalation_path",
      "sampleInput": "Acme (ARR 480k, renewal in 60 days): 3 severity-2 tickets in 2 weeks; exec sponsor emailed the CEO"
    },
    {
      "id": "19-support-capacity-planner",
      "name": "Support Capacity Planner",
      "description": "Plans support staffing from ticket volume, handle time, shrinkage, and service targets.",
      "tool": "plan_support_staffing",
      "inputKey": "ticket_volume",
      "outputKey": "staffing_plan",
      "sampleInput": "2,400 tickets a week, 14 min average handling, 30% shrinkage, volume growing 6% a month"
    },
    {
      "id": "20-bug-report-qualifier",
      "name": "Bug Report Qualifier",
      "description": "Qualifies customer bug reports for reproducibility, severity, and engineering handoff.",
      "tool": "qualify_bug_report",
      "inputKey": "customer_report",
      "outputKey": "qualified_bug",
      "sampleInput": "Invoice PDF shows wrong tax for Canadian customers since March; two accounts affected; screenshot attached"
    }
  ]
};
