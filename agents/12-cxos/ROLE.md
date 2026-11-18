# C-Suite & Executives (CxOs)

C-Suite & Executives (CxOs) suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
