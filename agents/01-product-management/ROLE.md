# Product Management

Product Management suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-prd-architect` — **PRD Architect**: Converts feature briefs into structured PRDs with goals, non-goals, and acceptance criteria. (Tool: `extract_requirements`)
- `02-roadmap-prioritizer` — **Roadmap Prioritizer**: Scores backlog items using RICE (Reach, Impact, Confidence, Effort) and outputs ranked tiers. (Tool: `compute_rice_score`)
- `03-user-story-splitter` — **User Story Splitter**: Decomposes large epics into INVEST-compliant stories with Given/When/Then criteria. (Tool: `split_invest_stories`)
- `04-competitive-intel` — **Competitive Intel Analyst**: Builds feature parity and differentiation matrices against competitor release notes. (Tool: `diff_feature_matrix`)
- `05-voice-of-customer` — **Voice of Customer Synthesizer**: Clusters NPS verbatims and support themes by frequency and churn risk. (Tool: `cluster_verbatims`)
- `06-launch-readiness` — **Launch Readiness Coordinator**: Audits GTM gates across engineering, docs, legal, and support sign-offs. (Tool: `audit_launch_gates`)
- `07-pricing-modeler` — **Pricing & Packaging Modeler**: Models gross margin and ARPA across seat-based and usage-based pricing tiers. (Tool: `simulate_unit_margin`)
- `08-experiment-designer` — **Experiment Designer**: Formulates A/B test hypotheses, MDE sample sizes, and guardrail metrics. (Tool: `calc_ab_sample_size`)
- `09-release-notes-writer` — **Release Notes Writer**: Transforms git commit logs and PR summaries into customer-facing changelogs. (Tool: `format_changelog`)
- `10-stakeholder-brief` — **Stakeholder Brief Generator**: Distills sprint demos, risks, and KPIs into a concise executive digest. (Tool: `summarize_exec_digest`)
- `11-persona-builder` — **Persona Builder**: Turns interview and survey notes into evidence-backed persona cards. (Tool: `synthesize_personas`)
- `12-jtbd-mapper` — **Jobs-To-Be-Done Mapper**: Maps customer interviews to jobs, triggers, and the outcomes people hire a product for. (Tool: `map_jobs_to_be_done`)
- `13-kano-classifier` — **Kano Feature Classifier**: Classifies features as must-have, performance, or delighter from paired survey answers. (Tool: `classify_kano`)
- `14-north-star-designer` — **North Star Metric Designer**: Chooses a north star metric and breaks it into input metrics teams can move. (Tool: `define_north_star`)
- `15-opportunity-tree-builder` — **Opportunity Solution Tree Builder**: Builds an opportunity solution tree from an outcome, customer needs, and candidate solutions. (Tool: `build_ost`)
- `16-beta-program-manager` — **Beta Program Manager**: Plans beta programs with cohort size, entry criteria, feedback loops, and exit gates. (Tool: `plan_beta_program`)
- `17-sunset-planner` — **Feature Sunset Planner**: Plans feature retirement with usage evidence, customer notice, migration, and rollback gates. (Tool: `plan_sunset`)
- `18-pmf-survey-analyst` — **PMF Survey Analyst**: Scores the product-market fit survey and reads the segments that would miss the product most. (Tool: `score_pmf_survey`)
- `19-build-buy-evaluator` — **Build vs Buy Evaluator**: Compares build, buy, and partner options on cost, speed, risk, and strategic fit. (Tool: `compare_build_buy`)
- `20-product-ops-cadence-planner` — **Product Ops Cadence Planner**: Designs the weekly, monthly, and quarterly meeting and reporting rhythm for product teams. (Tool: `plan_product_ops_cadence`)
