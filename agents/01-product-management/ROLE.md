# Product Management

Product Management suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
