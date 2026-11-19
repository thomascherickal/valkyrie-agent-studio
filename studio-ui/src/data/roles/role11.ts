import type { RoleCatalog } from "../types";

export const ROLE_11: RoleCatalog = {
  "id": "11-management",
  "name": "Engineering & Product Management",
  "agents": [
    {
      "id": "01-sprint-capacity-planner",
      "name": "Sprint Capacity Planner",
      "description": "Adjusts story-point targets for PTO, on-call rotation, and holidays.",
      "tool": "calc_net_capacity",
      "inputKey": "team_roster",
      "outputKey": "sprint_target",
      "sampleInput": "6 engineers, 4 PTO days, 1 on-call, avg velocity 34 pts"
    },
    {
      "id": "02-1on1-prep-assistant",
      "name": "1:1 Prep Assistant",
      "description": "Organizes shipped PRs, blockers, and career growth notes for 1:1s.",
      "tool": "structure_1on1_agenda",
      "inputKey": "engineer_context",
      "outputKey": "agenda_md",
      "sampleInput": "Led Rust workspace rollout; blocked on CI cache permissions"
    },
    {
      "id": "03-okr-alignment-checker",
      "name": "OKR Alignment Checker",
      "description": "Maps sprint epics against quarterly OKRs and flags orphan work.",
      "tool": "score_okr_fit",
      "inputKey": "epics_vs_okrs",
      "outputKey": "alignment_report",
      "sampleInput": "Epic: Custom dark theme; OKR1: Cut p99 latency by 40%"
    },
    {
      "id": "04-hiring-rubric-builder",
      "name": "Hiring Rubric Builder",
      "description": "Creates structured, signal-anchored interview rubrics for role levels.",
      "tool": "build_rubric_grid",
      "inputKey": "role_level",
      "outputKey": "rubric_md",
      "sampleInput": "Senior Rust/Python Systems Engineer \u2014 Architecture Round"
    },
    {
      "id": "05-perf-review-synthesizer",
      "name": "Perf Review Synthesizer",
      "description": "Synthesizes peer feedback and shipped artifacts into balanced reviews.",
      "tool": "synthesize_feedback",
      "inputKey": "feedback_notes",
      "outputKey": "review_draft",
      "sampleInput": "Strong systems design; can delegate code reviews earlier"
    },
    {
      "id": "06-cross-team-dependency",
      "name": "Cross-Team Dependency Tracker",
      "description": "Highlights critical-path handoffs and schedule slips across squads.",
      "tool": "map_critical_path",
      "inputKey": "squad_milestones",
      "outputKey": "dependency_risks",
      "sampleInput": "UI team needs /ws/traces from Core by Nov 20"
    },
    {
      "id": "07-meeting-action-extractor",
      "name": "Meeting Action Extractor",
      "description": "Extracts concrete owners, decisions, and due dates from transcripts.",
      "tool": "extract_action_items",
      "inputKey": "meeting_notes",
      "outputKey": "action_table",
      "sampleInput": "Alice to ship Cargo workspace by Fri; Bob to verify 100% cov"
    },
    {
      "id": "08-tech-strategy-summarizer",
      "name": "Tech Strategy Summarizer",
      "description": "Condenses 15-page architecture RFCs into 1-page decision memos.",
      "tool": "distill_decision_memo",
      "inputKey": "rfc_outline",
      "outputKey": "memo_md",
      "sampleInput": "Adopt Universal Agent IR + Rust transpiler across all 120 agents"
    },
    {
      "id": "09-team-health-pulse",
      "name": "Team Health Pulse",
      "description": "Tracks DORA metrics alongside qualitative team morale indicators.",
      "tool": "evaluate_dora_tier",
      "inputKey": "dora_snapshot",
      "outputKey": "health_report",
      "sampleInput": "Deploy freq: daily, Lead time: 3h, CFR: 2%, MTTR: 18m"
    },
    {
      "id": "10-quarterly-roadmap-brief",
      "name": "Quarterly Roadmap Brief",
      "description": "Prepares QBR slides with delivery confidence ratings and risks.",
      "tool": "format_qbr_brief",
      "inputKey": "qbr_inputs",
      "outputKey": "qbr_summary",
      "sampleInput": "Q4: 9/10 milestones on track; Rust CLI 1 week behind"
    },
    {
      "id": "11-delegation-coach",
      "name": "Delegation Coach",
      "description": "Coaches managers on what to delegate, to whom, and how much guidance and authority to give.",
      "tool": "plan_delegation",
      "inputKey": "task_list",
      "outputKey": "delegation_plan",
      "sampleInput": "My tasks: weekly metrics report, vendor negotiation, hiring screens, incident reviews, roadmap draft"
    },
    {
      "id": "12-promotion-packet-builder",
      "name": "Promotion Packet Builder",
      "description": "Builds promotion packets from impact evidence mapped to level expectations and peer signal.",
      "tool": "build_promo_packet",
      "inputKey": "impact_notes",
      "outputKey": "promo_packet",
      "sampleInput": "Led billing migration (zero downtime, 3 teams), mentored 2 engineers, cut invoice errors 70%, wrote the pricing RFC"
    },
    {
      "id": "13-conflict-mediation-guide",
      "name": "Conflict Mediation Guide",
      "description": "Guides managers through team conflicts with fact-finding, a mediation agenda, and agreements.",
      "tool": "plan_mediation",
      "inputKey": "conflict_summary",
      "outputKey": "mediation_plan",
      "sampleInput": "Two senior engineers disagree on ownership of the auth service; reviews have turned sharp; 3 teammates raised concerns"
    },
    {
      "id": "14-retro-facilitator",
      "name": "Retro Facilitator",
      "description": "Facilitates team retrospectives with a format, data, discussion, and tracked action items.",
      "tool": "facilitate_retro",
      "inputKey": "retro_notes",
      "outputKey": "retro_actions",
      "sampleInput": "Sprint 42: 3 incidents, review wait 2 days, good pairing, unclear priorities; last retro's 4 actions: 1 done"
    },
    {
      "id": "15-headcount-justifier",
      "name": "Headcount Justifier",
      "description": "Builds a headcount case from workload data, cost, risk, and the cost of not hiring.",
      "tool": "justify_headcount",
      "inputKey": "workload_data",
      "outputKey": "headcount_case",
      "sampleInput": "On-call load 1.8x target, 3 roadmap items slipped a quarter, team of 8, requesting 2 engineers"
    },
    {
      "id": "16-first-90-days-planner",
      "name": "30-60-90 Day Planner",
      "description": "Plans a new manager or hire's first 90 days with learning goals, relationships, and early wins.",
      "tool": "plan_first_quarter",
      "inputKey": "role_context",
      "outputKey": "onboarding_plan",
      "sampleInput": "New engineering manager for a 9-person platform team, two open incidents, roadmap behind, one low-morale report"
    },
    {
      "id": "17-tradeoff-advisor",
      "name": "Priority Tradeoff Advisor",
      "description": "Weighs competing requests by value, cost, deadline, and risk and explains the choice.",
      "tool": "weigh_tradeoffs",
      "inputKey": "competing_asks",
      "outputKey": "tradeoff_memo",
      "sampleInput": "Sales wants a custom export for a 300k deal; support wants fixes for 40 tickets; platform wants a 3-week upgrade"
    },
    {
      "id": "18-skip-level-prep-assistant",
      "name": "Skip Level Prep Assistant",
      "description": "Prepares skip-level meetings with questions, signals to listen for, and follow-up commitments.",
      "tool": "prep_skip_level",
      "inputKey": "team_signals",
      "outputKey": "skip_level_agenda",
      "sampleInput": "Team of 14 under 2 managers; engagement dip in the survey; reports mention unclear priorities and slow decisions"
    },
    {
      "id": "19-blameless-review-facilitator",
      "name": "Blameless Review Facilitator",
      "description": "Facilitates blameless incident reviews with a timeline, contributing factors, and actions.",
      "tool": "run_blameless_review",
      "inputKey": "incident_timeline",
      "outputKey": "review_agenda",
      "sampleInput": "Checkout down 47 minutes after a config push at 14:05; rollback delayed by missing runbook; alert fired 9 minutes late"
    },
    {
      "id": "20-feedback-writer",
      "name": "Feedback Writer",
      "description": "Writes specific, balanced feedback from observed behavior, impact, and a clear request.",
      "tool": "write_feedback",
      "inputKey": "observed_behavior",
      "outputKey": "feedback_draft",
      "sampleInput": "In Tuesday's design review you interrupted two juniors; they stopped presenting; the design missed two edge cases"
    }
  ]
};
