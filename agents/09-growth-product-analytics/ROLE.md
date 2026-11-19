# Growth & Product Analytics

Growth & Product Analytics suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-funnel-dropoff-analyst` — **Funnel Dropoff Analyst**: Computes step-by-step conversion rates and biggest dropoff levers. (Tool: `calc_funnel_rates`)
- `02-cohort-retention-modeler` — **Cohort Retention Modeler**: Evaluates D1/D7/D30 retention curves across signup channels. (Tool: `analyze_cohort_curve`)
- `03-ab-test-interpreter` — **A/B Test Interpreter**: Checks p-values, confidence intervals, and sample ratio mismatch. (Tool: `evaluate_ab_stats`)
- `04-activation-metric-finder` — **Activation Metric Finder**: Identifies early actions strongly correlated with 90-day retention. (Tool: `rank_activation_signals`)
- `05-pricing-elasticity-analyst` — **Pricing Elasticity Analyst**: Models upgrade conversion and revenue impact of paywall shifts. (Tool: `simulate_paywall`)
- `06-attribution-mapper` — **Attribution Mapper**: Compares first-touch vs linear multi-touch CAC across channels. (Tool: `compute_channel_roi`)
- `07-seo-content-strategist` — **SEO Content Strategist**: Finds high-intent developer keywords with low documentation competition. (Tool: `score_keyword_gaps`)
- `08-churn-cohort-explainer` — **Churn Cohort Explainer**: Correlates seat contraction with unused features and latency spikes. (Tool: `explain_churn_drivers`)
- `09-plg-loop-designer` — **PLG Loop Designer**: Designs shareable agent blueprint links that drive organic signups. (Tool: `model_viral_k_factor`)
- `10-exec-kpi-narrator` — **Exec KPI Narrator**: Turns weekly product telemetry tables into crisp narrative memos. (Tool: `narrate_weekly_kpis`)
- `11-lifecycle-email-planner` — **Lifecycle Email Planner**: Plans lifecycle email programs by trigger, timing, goal, and measurement. (Tool: `plan_lifecycle_emails`)
- `12-ltv-cac-modeler` — **LTV to CAC Modeler**: Models customer lifetime value against acquisition cost with payback and sensitivity to churn. (Tool: `model_ltv_cac`)
- `13-experiment-backlog-ranker` — **Experiment Backlog Ranker**: Ranks growth experiments by impact, confidence, and effort with traffic and runtime checks. (Tool: `rank_experiments`)
- `14-referral-program-designer` — **Referral Program Designer**: Designs referral programs with rewards, triggers, fraud limits, and break-even math. (Tool: `design_referral`)
- `15-onboarding-funnel-auditor` — **Onboarding Funnel Auditor**: Audits onboarding steps for friction, time to value, and the biggest drop-off. (Tool: `audit_onboarding`)
- `16-segment-discovery-analyst` — **Segment Discovery Analyst**: Finds customer segments from usage patterns and tests which segments retain and pay best. (Tool: `find_segments`)
- `17-pricing-page-reviewer` — **Pricing Page Reviewer**: Reviews pricing pages for clarity, anchoring, plan fit, objections, and conversion risks. (Tool: `review_pricing_page`)
- `18-pipeline-forecaster` — **Pipeline Forecaster**: Forecasts bookings from pipeline stage, conversion history, and deal age with risk bands. (Tool: `forecast_pipeline`)
- `19-event-taxonomy-auditor` — **Event Taxonomy Auditor**: Audits analytics event names and properties for consistency, coverage, and tracking debt. (Tool: `audit_event_names`)
- `20-win-loss-analyst` — **Win Loss Analyst**: Analyzes win and loss interviews for decision drivers, competitor patterns, and sales fixes. (Tool: `analyze_win_loss`)
