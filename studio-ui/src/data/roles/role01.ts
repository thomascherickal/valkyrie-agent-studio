import type { RoleCatalog } from "../types";

export const ROLE_01: RoleCatalog = {
  "id": "01-product-management",
  "name": "Product Management",
  "agents": [
    {
      "id": "01-prd-architect",
      "name": "PRD Architect",
      "description": "Converts feature briefs into structured PRDs with goals, non-goals, and acceptance criteria.",
      "tool": "extract_requirements",
      "inputKey": "feature_brief",
      "outputKey": "prd_markdown",
      "sampleInput": "Add SSO login with SAML 2.0 for enterprise workspaces"
    },
    {
      "id": "02-roadmap-prioritizer",
      "name": "Roadmap Prioritizer",
      "description": "Scores backlog items using RICE (Reach, Impact, Confidence, Effort) and outputs ranked tiers.",
      "tool": "compute_rice_score",
      "inputKey": "initiatives",
      "outputKey": "ranked_roadmap",
      "sampleInput": "Mobile Offline Sync (R:5000, I:3, C:0.8, E:4)"
    },
    {
      "id": "03-user-story-splitter",
      "name": "User Story Splitter",
      "description": "Decomposes large epics into INVEST-compliant stories with Given/When/Then criteria.",
      "tool": "split_invest_stories",
      "inputKey": "epic_text",
      "outputKey": "stories",
      "sampleInput": "As an admin, manage billing seats and export invoices"
    },
    {
      "id": "04-competitive-intel",
      "name": "Competitive Intel Analyst",
      "description": "Builds feature parity and differentiation matrices against competitor release notes.",
      "tool": "diff_feature_matrix",
      "inputKey": "competitor_notes",
      "outputKey": "matrix_summary",
      "sampleInput": "Competitor X launched usage-based metering and SOC2 Type II"
    },
    {
      "id": "05-voice-of-customer",
      "name": "Voice of Customer Synthesizer",
      "description": "Clusters NPS verbatims and support themes by frequency and churn risk.",
      "tool": "cluster_verbatims",
      "inputKey": "feedback_batch",
      "outputKey": "top_themes",
      "sampleInput": "Export CSV times out on >50k rows; dark mode requested"
    },
    {
      "id": "06-launch-readiness",
      "name": "Launch Readiness Coordinator",
      "description": "Audits GTM gates across engineering, docs, legal, and support sign-offs.",
      "tool": "audit_launch_gates",
      "inputKey": "checklist_state",
      "outputKey": "readiness_status",
      "sampleInput": "Docs: ready, Security: pending pentest, Billing: ready"
    },
    {
      "id": "07-pricing-modeler",
      "name": "Pricing & Packaging Modeler",
      "description": "Models gross margin and ARPA across seat-based and usage-based pricing tiers.",
      "tool": "simulate_unit_margin",
      "inputKey": "tier_assumptions",
      "outputKey": "margin_report",
      "sampleInput": "Pro: $29/seat, 100k tokens included, COGS $0.002/1k"
    },
    {
      "id": "08-experiment-designer",
      "name": "Experiment Designer",
      "description": "Formulates A/B test hypotheses, MDE sample sizes, and guardrail metrics.",
      "tool": "calc_ab_sample_size",
      "inputKey": "hypothesis",
      "outputKey": "experiment_spec",
      "sampleInput": "Shortening onboarding from 5 steps to 2 lifts D1 activation"
    },
    {
      "id": "09-release-notes-writer",
      "name": "Release Notes Writer",
      "description": "Transforms git commit logs and PR summaries into customer-facing changelogs.",
      "tool": "format_changelog",
      "inputKey": "pr_log",
      "outputKey": "release_notes",
      "sampleInput": "feat: add Rust transpiler; fix: OAuth token refresh race"
    },
    {
      "id": "10-stakeholder-brief",
      "name": "Stakeholder Brief Generator",
      "description": "Distills sprint demos, risks, and KPIs into a concise executive digest.",
      "tool": "summarize_exec_digest",
      "inputKey": "weekly_updates",
      "outputKey": "brief_text",
      "sampleInput": "Shipped v2.1 API; p99 latency down 38%; 2 blockers on SSO"
    }
  ]
};
