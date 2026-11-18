# Growth & Product Analytics

Growth & Product Analytics suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
