import type { RoleCatalog } from "../types";

export const ROLE_09: RoleCatalog = {
  "id": "09-growth-product-analytics",
  "name": "Growth & Product Analytics",
  "agents": [
    {
      "id": "01-funnel-dropoff-analyst",
      "name": "Funnel Dropoff Analyst",
      "description": "Computes step-by-step conversion rates and biggest dropoff levers.",
      "tool": "calc_funnel_rates",
      "inputKey": "funnel_counts",
      "outputKey": "dropoff_analysis",
      "sampleInput": "Visited:1000 -> Installed:420 -> FirstRun:190 -> Deployed:95"
    },
    {
      "id": "02-cohort-retention-modeler",
      "name": "Cohort Retention Modeler",
      "description": "Evaluates D1/D7/D30 retention curves across signup channels.",
      "tool": "analyze_cohort_curve",
      "inputKey": "cohort_data",
      "outputKey": "retention_summary",
      "sampleInput": "Oct cohort: D1 62%, D7 38%, D30 29%"
    },
    {
      "id": "03-ab-test-interpreter",
      "name": "A/B Test Interpreter",
      "description": "Checks p-values, confidence intervals, and sample ratio mismatch.",
      "tool": "evaluate_ab_stats",
      "inputKey": "ab_results",
      "outputKey": "experiment_verdict",
      "sampleInput": "Control: 12.1% (n=5000), Variant: 14.4% (n=5020), p=0.008"
    },
    {
      "id": "04-activation-metric-finder",
      "name": "Activation Metric Finder",
      "description": "Identifies early actions strongly correlated with 90-day retention.",
      "tool": "rank_activation_signals",
      "inputKey": "behavior_events",
      "outputKey": "aha_moment",
      "sampleInput": "Users who run >=3 sandbox tests in 48h retain 3.1x higher"
    },
    {
      "id": "05-pricing-elasticity-analyst",
      "name": "Pricing Elasticity Analyst",
      "description": "Models upgrade conversion and revenue impact of paywall shifts.",
      "tool": "simulate_paywall",
      "inputKey": "upgrade_data",
      "outputKey": "elasticity_report",
      "sampleInput": "Moving Custom Python to Pro vs keeping free up to 5 agents"
    },
    {
      "id": "06-attribution-mapper",
      "name": "Attribution Mapper",
      "description": "Compares first-touch vs linear multi-touch CAC across channels.",
      "tool": "compute_channel_roi",
      "inputKey": "channel_spend",
      "outputKey": "attribution_table",
      "sampleInput": "GitHub OSS: $0 CAC, 42% signups; Search Ads: $180 CAC"
    },
    {
      "id": "07-seo-content-strategist",
      "name": "SEO Content Strategist",
      "description": "Finds high-intent developer keywords with low documentation competition.",
      "tool": "score_keyword_gaps",
      "inputKey": "topic_cluster",
      "outputKey": "content_roadmap",
      "sampleInput": "rust ai agent runtime, local llm ollama agent builder"
    },
    {
      "id": "08-churn-cohort-explainer",
      "name": "Churn Cohort Explainer",
      "description": "Correlates seat contraction with unused features and latency spikes.",
      "tool": "explain_churn_drivers",
      "inputKey": "churned_accounts",
      "outputKey": "retention_actions",
      "sampleInput": "72% of churned teams never deployed a Rust agent"
    },
    {
      "id": "09-plg-loop-designer",
      "name": "PLG Loop Designer",
      "description": "Designs shareable agent blueprint links that drive organic signups.",
      "tool": "model_viral_k_factor",
      "inputKey": "product_surface",
      "outputKey": "loop_spec",
      "sampleInput": "Shareable agent.ir.yaml + demo.svg preview cards"
    },
    {
      "id": "10-exec-kpi-narrator",
      "name": "Exec KPI Narrator",
      "description": "Turns weekly product telemetry tables into crisp narrative memos.",
      "tool": "narrate_weekly_kpis",
      "inputKey": "kpi_table",
      "outputKey": "kpi_memo",
      "sampleInput": "WAU +14% WoW, Free-to-Paid 4.8%, Median Time-to-First-Deploy 6m"
    },
    {
      "id": "11-lifecycle-email-planner",
      "name": "Lifecycle Email Planner",
      "description": "Plans lifecycle email programs by trigger, timing, goal, and measurement.",
      "tool": "plan_lifecycle_emails",
      "inputKey": "lifecycle_goals",
      "outputKey": "email_plan",
      "sampleInput": "Goal: lift week-1 activation; 38% finish setup; users who invite a teammate retain 2x; trial lasts 14 days"
    },
    {
      "id": "12-ltv-cac-modeler",
      "name": "LTV to CAC Modeler",
      "description": "Models customer lifetime value against acquisition cost with payback and sensitivity to churn.",
      "tool": "model_ltv_cac",
      "inputKey": "unit_inputs",
      "outputKey": "ltv_cac_readout",
      "sampleInput": "ARPA 120 per month, gross margin 78%, monthly churn 2.5%, CAC 1,400 blended, 9 months payback goal"
    },
    {
      "id": "13-experiment-backlog-ranker",
      "name": "Experiment Backlog Ranker",
      "description": "Ranks growth experiments by impact, confidence, and effort with traffic and runtime checks.",
      "tool": "rank_experiments",
      "inputKey": "experiment_ideas",
      "outputKey": "ranked_backlog",
      "sampleInput": "Ideas: shorter signup form, annual plan banner, onboarding checklist, referral prompt; 40k visitors a week"
    },
    {
      "id": "14-referral-program-designer",
      "name": "Referral Program Designer",
      "description": "Designs referral programs with rewards, triggers, fraud limits, and break-even math.",
      "tool": "design_referral",
      "inputKey": "referral_brief",
      "outputKey": "referral_design",
      "sampleInput": "B2B SaaS, 5k active accounts, wants teams to refer peers; CAC 1,200; considering a 100 credit on both sides"
    },
    {
      "id": "15-onboarding-funnel-auditor",
      "name": "Onboarding Funnel Auditor",
      "description": "Audits onboarding steps for friction, time to value, and the biggest drop-off.",
      "tool": "audit_onboarding",
      "inputKey": "onboarding_steps",
      "outputKey": "onboarding_audit",
      "sampleInput": "Signup, verify email, create workspace, invite team, connect data, first report; 61% drop at connect data"
    },
    {
      "id": "16-segment-discovery-analyst",
      "name": "Segment Discovery Analyst",
      "description": "Finds customer segments from usage patterns and tests which segments retain and pay best.",
      "tool": "find_segments",
      "inputKey": "usage_summary",
      "outputKey": "segment_findings",
      "sampleInput": "4 clusters by usage: heavy API users, dashboard-only viewers, occasional exporters, trial tourists"
    },
    {
      "id": "17-pricing-page-reviewer",
      "name": "Pricing Page Reviewer",
      "description": "Reviews pricing pages for clarity, anchoring, plan fit, objections, and conversion risks.",
      "tool": "review_pricing_page",
      "inputKey": "page_copy",
      "outputKey": "pricing_review",
      "sampleInput": "3 plans (Starter 19, Team 59, Business 199), usage limits hidden behind a tooltip, no annual toggle, no FAQ"
    },
    {
      "id": "18-pipeline-forecaster",
      "name": "Pipeline Forecaster",
      "description": "Forecasts bookings from pipeline stage, conversion history, and deal age with risk bands.",
      "tool": "forecast_pipeline",
      "inputKey": "pipeline_snapshot",
      "outputKey": "forecast",
      "sampleInput": "Q4 pipeline: 80 deals, 24 in proposal, 9 in negotiation; average deal 38k; 3 deals older than 120 days"
    },
    {
      "id": "19-event-taxonomy-auditor",
      "name": "Event Taxonomy Auditor",
      "description": "Audits analytics event names and properties for consistency, coverage, and tracking debt.",
      "tool": "audit_event_names",
      "inputKey": "event_list",
      "outputKey": "taxonomy_audit",
      "sampleInput": "signup, Sign_Up, user_signed_up, click_btn, ButtonClicked, plan_upgraded, upgrade; 340 events, 60 unused"
    },
    {
      "id": "20-win-loss-analyst",
      "name": "Win Loss Analyst",
      "description": "Analyzes win and loss interviews for decision drivers, competitor patterns, and sales fixes.",
      "tool": "analyze_win_loss",
      "inputKey": "deal_notes",
      "outputKey": "win_loss_themes",
      "sampleInput": "Lost 14 of 30 mid-market deals; reasons: price vs incumbent 6, missing SSO 5, slow security review 3"
    }
  ]
};
