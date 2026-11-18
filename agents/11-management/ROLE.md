# Engineering & Product Management

Engineering & Product Management suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
