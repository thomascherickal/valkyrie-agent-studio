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
    }
  ]
};
