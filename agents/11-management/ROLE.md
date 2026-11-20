# Engineering & Product Management

Engineering & Product Management suite of 20 focused autonomous agents in Valkyrie Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-sprint-capacity-planner` — **Sprint Capacity Planner**: Adjusts story-point targets for PTO, on-call rotation, and holidays. (Tool: `calc_net_capacity`)
- `02-1on1-prep-assistant` — **1:1 Prep Assistant**: Organizes shipped PRs, blockers, and career growth notes for 1:1s. (Tool: `structure_1on1_agenda`)
- `03-okr-alignment-checker` — **OKR Alignment Checker**: Maps sprint epics against quarterly OKRs and flags orphan work. (Tool: `score_okr_fit`)
- `04-hiring-rubric-builder` — **Hiring Rubric Builder**: Creates structured, signal-anchored interview rubrics for role levels. (Tool: `build_rubric_grid`)
- `05-perf-review-synthesizer` — **Perf Review Synthesizer**: Synthesizes peer feedback and shipped artifacts into balanced reviews. (Tool: `synthesize_feedback`)
- `06-cross-team-dependency` — **Cross-Team Dependency Tracker**: Highlights critical-path handoffs and schedule slips across squads. (Tool: `map_critical_path`)
- `07-meeting-action-extractor` — **Meeting Action Extractor**: Extracts concrete owners, decisions, and due dates from transcripts. (Tool: `extract_action_items`)
- `08-tech-strategy-summarizer` — **Tech Strategy Summarizer**: Condenses 15-page architecture RFCs into 1-page decision memos. (Tool: `distill_decision_memo`)
- `09-team-health-pulse` — **Team Health Pulse**: Tracks DORA metrics alongside qualitative team morale indicators. (Tool: `evaluate_dora_tier`)
- `10-quarterly-roadmap-brief` — **Quarterly Roadmap Brief**: Prepares QBR slides with delivery confidence ratings and risks. (Tool: `format_qbr_brief`)
- `11-delegation-coach` — **Delegation Coach**: Coaches managers on what to delegate, to whom, and how much guidance and authority to give. (Tool: `plan_delegation`)
- `12-promotion-packet-builder` — **Promotion Packet Builder**: Builds promotion packets from impact evidence mapped to level expectations and peer signal. (Tool: `build_promo_packet`)
- `13-conflict-mediation-guide` — **Conflict Mediation Guide**: Guides managers through team conflicts with fact-finding, a mediation agenda, and agreements. (Tool: `plan_mediation`)
- `14-retro-facilitator` — **Retro Facilitator**: Facilitates team retrospectives with a format, data, discussion, and tracked action items. (Tool: `facilitate_retro`)
- `15-headcount-justifier` — **Headcount Justifier**: Builds a headcount case from workload data, cost, risk, and the cost of not hiring. (Tool: `justify_headcount`)
- `16-first-90-days-planner` — **30-60-90 Day Planner**: Plans a new manager or hire's first 90 days with learning goals, relationships, and early wins. (Tool: `plan_first_quarter`)
- `17-tradeoff-advisor` — **Priority Tradeoff Advisor**: Weighs competing requests by value, cost, deadline, and risk and explains the choice. (Tool: `weigh_tradeoffs`)
- `18-skip-level-prep-assistant` — **Skip Level Prep Assistant**: Prepares skip-level meetings with questions, signals to listen for, and follow-up commitments. (Tool: `prep_skip_level`)
- `19-blameless-review-facilitator` — **Blameless Review Facilitator**: Facilitates blameless incident reviews with a timeline, contributing factors, and actions. (Tool: `run_blameless_review`)
- `20-feedback-writer` — **Feedback Writer**: Writes specific, balanced feedback from observed behavior, impact, and a clear request. (Tool: `write_feedback`)
