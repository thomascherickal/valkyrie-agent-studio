import type { RoleCatalog } from "../types";

export const ROLE_12: RoleCatalog = {
  "id": "12-cxos",
  "name": "C-Suite & Executives (CxOs)",
  "agents": [
    {
      "id": "01-board-deck-synthesizer",
      "name": "Board Deck Synthesizer",
      "description": "Compiles ARR, net burn, NRR, and key product milestones for board slides.",
      "tool": "build_board_narrative",
      "inputKey": "quarter_metrics",
      "outputKey": "board_slides_md",
      "sampleInput": "ARR $4.8M (+22% QoQ), NRR 118%, Runway 28 months"
    },
    {
      "id": "02-ma-diligence-reviewer",
      "name": "M&A Diligence Reviewer",
      "description": "Flags IP, OSS license, security, and customer-concentration risks.",
      "tool": "score_diligence_risks",
      "inputKey": "diligence_docs",
      "outputKey": "risk_memo",
      "sampleInput": "Top customer 28% ARR; 1 GPLv3 dependency in core worker"
    },
    {
      "id": "03-annual-operating-plan",
      "name": "Annual Operating Plan Modeler",
      "description": "Models hiring pace, cloud COGS, and ARR scenarios for FY27.",
      "tool": "project_aop_scenarios",
      "inputKey": "aop_drivers",
      "outputKey": "aop_table",
      "sampleInput": "Base: +12 hires, 78% gross margin, $9.5M ending ARR"
    },
    {
      "id": "04-crisis-comms-strategist",
      "name": "Crisis Comms Strategist",
      "description": "Coordinates customer, press, and internal messaging during incidents.",
      "tool": "draft_comms_matrix",
      "inputKey": "crisis_brief",
      "outputKey": "comms_playbook",
      "sampleInput": "Third-party auth outage affecting 12% of EU logins"
    },
    {
      "id": "05-ai-transformation-advisor",
      "name": "AI Transformation Advisor",
      "description": "Ranks internal workflows by automation ROI and compliance safety.",
      "tool": "rank_ai_roi",
      "inputKey": "workflow_catalog",
      "outputKey": "rollout_roadmap",
      "sampleInput": "L1 support triage (1,200 tickets/wk) vs legal contract redlines"
    },
    {
      "id": "06-investor-update-writer",
      "name": "Investor Update Writer",
      "description": "Drafts crisp monthly investor updates covering wins, metrics, and asks.",
      "tool": "format_investor_email",
      "inputKey": "monthly_highlights",
      "outputKey": "investor_update",
      "sampleInput": "Launched Valkyrie 120-agent studio; seeking 2 enterprise intros"
    },
    {
      "id": "07-enterprise-deal-desk",
      "name": "Enterprise Deal Desk",
      "description": "Evaluates custom SLA, indemnity, and multi-year discount requests.",
      "tool": "score_deal_margin",
      "inputKey": "deal_terms",
      "outputKey": "deal_approval",
      "sampleInput": "$250k/yr 3-yr deal requesting 99.99% SLA and 25% discount"
    },
    {
      "id": "08-regulatory-horizon-watch",
      "name": "Regulatory Horizon Watcher",
      "description": "Maps EU AI Act, SOC2, and GDPR updates to product roadmap controls.",
      "tool": "map_compliance_gaps",
      "inputKey": "policy_scope",
      "outputKey": "regulatory_brief",
      "sampleInput": "Autonomous agent audit trails & human-in-the-loop logging"
    },
    {
      "id": "09-org-design-modeler",
      "name": "Org Design Modeler",
      "description": "Evaluates manager span-of-control and platform vs stream-aligned pods.",
      "tool": "analyze_org_topology",
      "inputKey": "org_chart",
      "outputKey": "org_recommendations",
      "sampleInput": "42 engineers, 4 managers, 1 platform team, 5 product pods"
    },
    {
      "id": "10-ceo-weekly-brief",
      "name": "CEO Weekly Brief",
      "description": "Synthesizes GTM, Eng, Finance, and People signals into a 3-min read.",
      "tool": "compile_ceo_brief",
      "inputKey": "exec_inputs",
      "outputKey": "weekly_brief_md",
      "sampleInput": "Pipeline $1.4M, Uptime 99.98%, 2 senior offers accepted"
    },
    {
      "id": "11-cash-runway-analyst",
      "name": "Cash Runway Analyst",
      "description": "Projects cash runway under base, downside, and upside cases with clear decision triggers.",
      "tool": "project_runway",
      "inputKey": "cash_position",
      "outputKey": "runway_scenarios",
      "sampleInput": "Cash 14.2M, net burn 780k a month, 9% monthly growth in revenue, 2 enterprise deals pending, hiring plan adds 600k"
    },
    {
      "id": "12-fundraising-narrative-builder",
      "name": "Fundraising Narrative Builder",
      "description": "Builds investor narratives from traction, market, team, and use of funds with proof points.",
      "tool": "build_fundraise_story",
      "inputKey": "company_facts",
      "outputKey": "investor_narrative",
      "sampleInput": "B2B workflow SaaS, 4.1M ARR growing 160% a year, 118% net retention, raising 20M Series B, 24 months of runway wanted"
    },
    {
      "id": "13-board-risk-register-keeper",
      "name": "Board Risk Register Keeper",
      "description": "Maintains a board-level risk register with likelihood, impact, owners, and mitigations.",
      "tool": "rank_board_risks",
      "inputKey": "risk_list",
      "outputKey": "risk_register",
      "sampleInput": "Top risks: key customer concentration, regulatory change in EU, cloud outage, loss of CTO, pricing pressure"
    },
    {
      "id": "14-executive-pricing-strategist",
      "name": "Executive Pricing Strategist",
      "description": "Frames pricing strategy decisions with value, competition, margin, and customer impact.",
      "tool": "assess_pricing_strategy",
      "inputKey": "pricing_context",
      "outputKey": "pricing_brief",
      "sampleInput": "Considering a 12% price rise on the Team plan; competitors flat; 4% monthly churn risk if the rise lands badly"
    },
    {
      "id": "15-partnership-evaluator",
      "name": "Partnership Evaluator",
      "description": "Evaluates partnership proposals on strategic fit, economics, dependency, and exit terms.",
      "tool": "score_partnership",
      "inputKey": "partnership_terms",
      "outputKey": "partner_memo",
      "sampleInput": "Channel partner offers access to 800 mid-market accounts for 25% revenue share; exclusivity 2 years; co-marketing"
    },
    {
      "id": "16-exec-search-planner",
      "name": "Executive Hiring Planner",
      "description": "Plans executive searches with scorecard, sourcing, process, references, and offer strategy.",
      "tool": "plan_exec_search",
      "inputKey": "role_need",
      "outputKey": "search_plan",
      "sampleInput": "Need a VP Sales for a 6M to 25M ARR journey; enterprise motion new; current head of sales leaving in 3 months"
    },
    {
      "id": "17-earnings-call-prep-coach",
      "name": "Earnings Call Prep Coach",
      "description": "Prepares earnings calls with messages, tough questions, disclosure checks, and rehearsal plans.",
      "tool": "prep_earnings_call",
      "inputKey": "quarter_results",
      "outputKey": "qa_prep",
      "sampleInput": "Revenue +22% (guide +25%), gross margin down 1.8 points, guidance cut for next quarter, one-time charge"
    },
    {
      "id": "18-cyber-risk-briefer",
      "name": "Cyber Risk Briefer",
      "description": "Briefs executives on cyber risk in business terms with exposure, controls, and decisions.",
      "tool": "brief_cyber_risk",
      "inputKey": "security_summary",
      "outputKey": "exec_risk_brief",
      "sampleInput": "3 critical findings open, MFA on 91% of staff, last restore test 14 months ago, ransomware drill planned"
    },
    {
      "id": "19-esg-metrics-reporter",
      "name": "Sustainability Metrics Reporter",
      "description": "Compiles sustainability metrics with boundaries, methods, targets, and assurance readiness.",
      "tool": "compile_esg_metrics",
      "inputKey": "esg_inputs",
      "outputKey": "esg_summary",
      "sampleInput": "Cloud 1,900 MWh, offices 420 MWh, travel 310 tCO2e; 58% renewable power; target net zero by 2040"
    },
    {
      "id": "20-strategic-bet-reviewer",
      "name": "Strategic Bet Reviewer",
      "description": "Reviews strategic bets for assumptions, option value, staging, and kill criteria.",
      "tool": "review_strategic_bet",
      "inputKey": "bet_proposal",
      "outputKey": "bet_review",
      "sampleInput": "Enter the healthcare vertical: 4M investment over 18 months, new compliance burden, 3 design partners signed"
    }
  ]
};
