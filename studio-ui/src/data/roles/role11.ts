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
    }
  ]
};
