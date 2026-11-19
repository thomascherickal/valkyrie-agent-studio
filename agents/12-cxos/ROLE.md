# C-Suite & Executives (CxOs)

C-Suite & Executives (CxOs) suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-board-deck-synthesizer` — **Board Deck Synthesizer**: Compiles ARR, net burn, NRR, and key product milestones for board slides. (Tool: `build_board_narrative`)
- `02-ma-diligence-reviewer` — **M&A Diligence Reviewer**: Flags IP, OSS license, security, and customer-concentration risks. (Tool: `score_diligence_risks`)
- `03-annual-operating-plan` — **Annual Operating Plan Modeler**: Models hiring pace, cloud COGS, and ARR scenarios for FY27. (Tool: `project_aop_scenarios`)
- `04-crisis-comms-strategist` — **Crisis Comms Strategist**: Coordinates customer, press, and internal messaging during incidents. (Tool: `draft_comms_matrix`)
- `05-ai-transformation-advisor` — **AI Transformation Advisor**: Ranks internal workflows by automation ROI and compliance safety. (Tool: `rank_ai_roi`)
- `06-investor-update-writer` — **Investor Update Writer**: Drafts crisp monthly investor updates covering wins, metrics, and asks. (Tool: `format_investor_email`)
- `07-enterprise-deal-desk` — **Enterprise Deal Desk**: Evaluates custom SLA, indemnity, and multi-year discount requests. (Tool: `score_deal_margin`)
- `08-regulatory-horizon-watch` — **Regulatory Horizon Watcher**: Maps EU AI Act, SOC2, and GDPR updates to product roadmap controls. (Tool: `map_compliance_gaps`)
- `09-org-design-modeler` — **Org Design Modeler**: Evaluates manager span-of-control and platform vs stream-aligned pods. (Tool: `analyze_org_topology`)
- `10-ceo-weekly-brief` — **CEO Weekly Brief**: Synthesizes GTM, Eng, Finance, and People signals into a 3-min read. (Tool: `compile_ceo_brief`)
- `11-cash-runway-analyst` — **Cash Runway Analyst**: Projects cash runway under base, downside, and upside cases with clear decision triggers. (Tool: `project_runway`)
- `12-fundraising-narrative-builder` — **Fundraising Narrative Builder**: Builds investor narratives from traction, market, team, and use of funds with proof points. (Tool: `build_fundraise_story`)
- `13-board-risk-register-keeper` — **Board Risk Register Keeper**: Maintains a board-level risk register with likelihood, impact, owners, and mitigations. (Tool: `rank_board_risks`)
- `14-executive-pricing-strategist` — **Executive Pricing Strategist**: Frames pricing strategy decisions with value, competition, margin, and customer impact. (Tool: `assess_pricing_strategy`)
- `15-partnership-evaluator` — **Partnership Evaluator**: Evaluates partnership proposals on strategic fit, economics, dependency, and exit terms. (Tool: `score_partnership`)
- `16-exec-search-planner` — **Executive Hiring Planner**: Plans executive searches with scorecard, sourcing, process, references, and offer strategy. (Tool: `plan_exec_search`)
- `17-earnings-call-prep-coach` — **Earnings Call Prep Coach**: Prepares earnings calls with messages, tough questions, disclosure checks, and rehearsal plans. (Tool: `prep_earnings_call`)
- `18-cyber-risk-briefer` — **Cyber Risk Briefer**: Briefs executives on cyber risk in business terms with exposure, controls, and decisions. (Tool: `brief_cyber_risk`)
- `19-esg-metrics-reporter` — **Sustainability Metrics Reporter**: Compiles sustainability metrics with boundaries, methods, targets, and assurance readiness. (Tool: `compile_esg_metrics`)
- `20-strategic-bet-reviewer` — **Strategic Bet Reviewer**: Reviews strategic bets for assumptions, option value, staging, and kill criteria. (Tool: `review_strategic_bet`)
