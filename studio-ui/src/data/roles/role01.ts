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
    },
    {
      "id": "11-persona-builder",
      "name": "Persona Builder",
      "description": "Turns interview and survey notes into evidence-backed persona cards.",
      "tool": "synthesize_personas",
      "inputKey": "research_notes",
      "outputKey": "persona_cards",
      "sampleInput": "12 interviews: admins spend Mondays on access requests; 9 of 12 use spreadsheets to track licences"
    },
    {
      "id": "12-jtbd-mapper",
      "name": "Jobs-To-Be-Done Mapper",
      "description": "Maps customer interviews to jobs, triggers, and the outcomes people hire a product for.",
      "tool": "map_jobs_to_be_done",
      "inputKey": "interview_notes",
      "outputKey": "jtbd_map",
      "sampleInput": "Switched from spreadsheets after the audit failed; needs proof of access reviews in under an hour"
    },
    {
      "id": "13-kano-classifier",
      "name": "Kano Feature Classifier",
      "description": "Classifies features as must-have, performance, or delighter from paired survey answers.",
      "tool": "classify_kano",
      "inputKey": "survey_results",
      "outputKey": "kano_matrix",
      "sampleInput": "SSO: 72% would be happy with it, 55% unhappy without it; dark mode: 40% happy, 6% unhappy without"
    },
    {
      "id": "14-north-star-designer",
      "name": "North Star Metric Designer",
      "description": "Chooses a north star metric and breaks it into input metrics teams can move.",
      "tool": "define_north_star",
      "inputKey": "product_goals",
      "outputKey": "metric_tree",
      "sampleInput": "Goal: help teams ship reviewed releases faster; users create pull requests, reviewers approve"
    },
    {
      "id": "15-opportunity-tree-builder",
      "name": "Opportunity Solution Tree Builder",
      "description": "Builds an opportunity solution tree from an outcome, customer needs, and candidate solutions.",
      "tool": "build_ost",
      "inputKey": "desired_outcome",
      "outputKey": "opportunity_tree",
      "sampleInput": "Outcome: raise week-4 retention from 31% to 40%; customers say setup is long and reports are hard to share"
    },
    {
      "id": "16-beta-program-manager",
      "name": "Beta Program Manager",
      "description": "Plans beta programs with cohort size, entry criteria, feedback loops, and exit gates.",
      "tool": "plan_beta_program",
      "inputKey": "beta_plan_brief",
      "outputKey": "beta_playbook",
      "sampleInput": "Beta of the new reporting module for 40 accounts over 6 weeks; need a go or no-go by the end"
    },
    {
      "id": "17-sunset-planner",
      "name": "Feature Sunset Planner",
      "description": "Plans feature retirement with usage evidence, customer notice, migration, and rollback gates.",
      "tool": "plan_sunset",
      "inputKey": "feature_usage",
      "outputKey": "sunset_plan",
      "sampleInput": "Legacy CSV exporter: 3% of accounts, 180 weekly runs, replaced by the scheduled-reports API"
    },
    {
      "id": "18-pmf-survey-analyst",
      "name": "PMF Survey Analyst",
      "description": "Scores the product-market fit survey and reads the segments that would miss the product most.",
      "tool": "score_pmf_survey",
      "inputKey": "survey_counts",
      "outputKey": "pmf_readout",
      "sampleInput": "150 responses: 54 very disappointed, 63 somewhat, 33 not disappointed; strongest in agencies"
    },
    {
      "id": "19-build-buy-evaluator",
      "name": "Build vs Buy Evaluator",
      "description": "Compares build, buy, and partner options on cost, speed, risk, and strategic fit.",
      "tool": "compare_build_buy",
      "inputKey": "capability_request",
      "outputKey": "decision_memo",
      "sampleInput": "Need in-app e-signature within 2 quarters; vendor quotes 45k per year, in-house estimate 5 engineer-months"
    },
    {
      "id": "20-product-ops-cadence-planner",
      "name": "Product Ops Cadence Planner",
      "description": "Designs the weekly, monthly, and quarterly meeting and reporting rhythm for product teams.",
      "tool": "plan_product_ops_cadence",
      "inputKey": "team_rituals",
      "outputKey": "ops_cadence",
      "sampleInput": "6 squads, weekly product reviews run long, roadmap changes surprise sales, metrics reviewed ad hoc"
    }
  ]
};
