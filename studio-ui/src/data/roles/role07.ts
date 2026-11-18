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
    }
  ]
};
