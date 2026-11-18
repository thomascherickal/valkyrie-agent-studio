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
    }
  ]
};
