"""Playbooks for the Management agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "11-management/01-sprint-capacity-planner": {
        "fields": ["engineers|Engineers on the team|number|6", "working_days|Working days in the sprint|number|10", "pto_days|Total PTO days in the sprint|number|4", "holiday_days|Public holidays in the sprint|number|0", "oncall|Engineers on call this sprint|number|1", "velocity|Average velocity (story points)|number|34"],
        "sections": [
            ["Team and calendar", "Roster: {input}", "{engineers} engineers, {working_days} working days, {pto_days} PTO days, {holiday_days} holidays, {oncall} on call."],
            ["Capacity formula", "Net person-days = engineers x days - PTO - holidays x engineers - on-call load. Count on-call engineers at about 40 percent availability (interrupt-driven work).", "Scale the average velocity by net person-days divided by full person-days to get this sprint's point target."],
            ["Commit rules", "Commit to the point target, not to the stretch. Use the average of the last 3 to 5 sprints, never the best one. Reserve 15 to 20 percent for bugs and unplanned work.", "New team members count at 50 percent for their first 2 sprints."],
            ["Risks to check", "Large stories above 8 points, unfinished carry-over, dependencies on other teams, a release in the sprint, and single points of knowledge when someone is out.", "If net capacity drops under 70 percent, cut scope early and tell stakeholders in planning, not at the review."],
            ["Hygiene", "Do not convert points to hours. Measure predictability (delivered divided by committed, target 80 to 100 percent) over time.", "Revisit the velocity baseline when the team changes by more than one person."],
        ],
        "metrics": ["Net person-days|engineers * working_days - pto_days - holiday_days * engineers - oncall * working_days * 0.4|{:.1f}", "Capacity versus full strength|(engineers * working_days - pto_days - holiday_days * engineers - oncall * working_days * 0.4) / (engineers * working_days)|{:.0%}", "Story point target|velocity * (engineers * working_days - pto_days - holiday_days * engineers - oncall * working_days * 0.4) / (engineers * working_days)|{:.0f}"],
    },
    "11-management/02-1on1-prep-assistant": {
        "fields": ["shipped|Recently shipped work|list|Rust workspace rollout, CI cache fix, Two design reviews", "blockers|Blockers|list|CI cache permissions, Waiting on security review", "growth|Growth goals|list|Lead a cross-team project, Improve written design docs", "last_topics|Topics from the last 1:1|list|Staff promotion path, On-call load", "mood|Energy or mood signal|text|Engaged but tired after the release crunch"],
        "sections": [
            ["Context", "Engineer context: {input}", "Signal: {mood}", "The 1:1 belongs to the report. Open with their topics, then yours."],
            ["Recent wins", "*{shipped}", "Name the impact on users or the team, not only the task. Recognition lands best when specific and timely."],
            ["Blockers and support", "*{blockers}", "For each: what you will do, by when. Remove one blocker before the next meeting; unresolved blockers are the top reason for 1:1s losing trust."],
            ["Growth", "*{growth}", "Ask: what skill do you want to build this quarter, what work excites you, what would you stop doing? Link goals to concrete projects and review progress monthly."],
            ["Follow-ups and questions", "Review commitments from last time:", "*{last_topics}", "Good questions: What is slowing you down? How is the workload? What feedback do you have for me? Close with two written action items with owners."],
        ],
        "metrics": [],
    },
    "11-management/03-okr-alignment-checker": {
        "fields": ["objectives|Quarterly objectives and key results|list|KR1: Cut p99 latency by 40%, KR2: Reach 99.95% uptime, KR3: Raise activation to 45%", "total_points|Total points planned this quarter|number|120", "aligned_points|Points mapped to a key result|number|78", "ktlo_pct|Allowance for keep-the-lights-on work (percent)|number|15"],
        "sections": [
            ["Mapping", "Epics versus OKRs: {input}", "Objectives in force:", "*{objectives}"],
            ["How to map", "Link each epic to exactly one key result it moves, and write the expected change in the metric. If you cannot name the metric movement, the epic is orphaned or the KR is badly written.", "A theme such as a custom dark theme normally fits no latency KR; either tie it to an adoption KR with evidence or defer it."],
            ["Orphan work", "Orphan work is not always bad: allow {ktlo_pct} percent for keep-the-lights-on (security patches, on-call, compliance). Above that, the roadmap is drifting.", "Orphan epics require a sponsor and a one-line justification to proceed."],
            ["Quality of the OKRs", "Objectives are qualitative and inspiring; key results are measurable outcomes with baseline and target, not tasks. Aim for 3 to 5 KRs per team; scoring 0.7 is a healthy stretch.", "Check for output KRs such as ship X: rewrite as the result of shipping X."],
            ["Actions", "Re-plan if aligned work is below 80 percent of capacity: stop or defer orphans, shift points to the KR furthest behind, and ask product whether a KR should change.", "Repeat the check at mid-quarter."],
        ],
        "metrics": ["Alignment (points mapped)|aligned_points / total_points|{:.0%}", "Unaligned points|total_points - aligned_points|{:,.0f}", "Orphan points beyond the allowance|max(0, total_points - aligned_points - total_points * ktlo_pct / 100)|{:,.0f}"],
    },
    "11-management/04-hiring-rubric-builder": {
        "fields": ["competencies|Competencies assessed|list|Architecture and system design, Rust and Python depth, Debugging, Communication", "competency_count|Number of competencies|number|4", "round_min|Interview length (minutes)|number|60", "hire_bar|Hiring bar|text|Strong hire needs 3 of 4 competencies at 4 and none below 3", "interviewers|Interviewers in the round|number|2"],
        "sections": [
            ["Role and round", "Role: {input}", "{interviewers} interviewers, {round_min} minutes. Bar: {hire_bar}"],
            ["Competencies", "*{competencies}", "Pick only competencies this round can observe. Each round covers 2 to 4, and no two rounds repeat the same one."],
            ["Signal anchors", "Score 1 to 4 against written examples. 1 No evidence or major concerns. 2 Partial; needs significant guidance. 3 Meets the bar for the level, works independently. 4 Exceeds; teaches others, handles ambiguity and trade-offs.", "For senior architecture: expects explicit requirements, trade-off analysis, failure modes, capacity numbers and migration plans."],
            ["Question design", "Use structured, job-related questions asked of every candidate in the same way, with probing follow-ups and a scoring guide. Prefer a work sample or design problem to trivia.", "Avoid questions on age, family, nationality or health, and avoid culture fit as a score; use values-based behaviours instead."],
            ["Debrief rules", "Interviewers write independent scores and notes before the debrief to avoid anchoring. Decide on evidence; one strong no on a core competency needs a discussion, not an average.", "Track pass rates, interviewer calibration and offer acceptance."],
        ],
        "metrics": ["Minutes per competency|round_min / competency_count|{:.0f}", "Competencies needed at score 4 (3 of 4 rule)|competency_count * 3 / 4|{:.1f}"],
    },
    "11-management/05-perf-review-synthesizer": {
        "fields": ["period|Review period|text|H2 2026", "strengths|Strengths with evidence|list|Led the Rust workspace migration across 6 repos, Mentored two junior engineers, Wrote the design doc for the plugin API", "growth_areas|Growth areas|list|Delegating code reviews earlier, Scoping projects with less rework", "level|Level and expectations|text|Senior engineer (IC4)", "impact|Measurable impact|longtext|Build time down 35 percent\nTwo launches delivered on time\nOn-call incident count down by a third"],
        "sections": [
            ["Context", "Feedback received: {input}", "Period {period}; level {level}."],
            ["Strengths", "*{strengths}", "Write each as behaviour, situation and effect. Back every claim with an artifact (PR, doc, metric)."],
            ["Impact", "*{impact}", "Judge impact against expectations of the level, not against peers' hours."],
            ["Growth areas", "*{growth_areas}", "Give one concrete next step per area and a way to measure it. Frame as a future behaviour: 'delegate the first review of each PR from next sprint'."],
            ["Calibration and bias", "Check for recency bias (weigh the whole period), halo and horns, and different language for different groups (for example 'abrasive' versus 'direct'). Replace adjectives with examples.", "Keep ratings and compensation conversations separate from the growth conversation where policy allows."],
        ],
        "metrics": [],
    },
    "11-management/06-cross-team-dependency": {
        "fields": ["provider|Providing team|text|Core platform team", "days_until_due|Days until the consumer needs it|number|4", "provider_eta_days|Provider estimated days to deliver|number|6", "buffer_days|Integration buffer needed (days)|number|2", "fallback|Fallback if late|text|Mock the /ws/traces endpoint with recorded data"],
        "sections": [
            ["Dependency", "Milestones: {input}", "Provider: {provider}. Needed in {days_until_due} days; provider estimates {provider_eta_days} days; buffer {buffer_days} days."],
            ["Critical path", "List handoffs in order with owner, date and what is handed over (an API contract, a build, data). The critical path is the chain with zero slack; any slip on it moves the release.", "Slack = days until due - provider ETA - integration buffer. Zero or negative slack is a risk now, not later."],
            ["Risk rating", "Green: slack above 3 days. Amber: slack 0 to 3 days. Red: negative slack or no committed date. Treat a verbal date as unconfirmed.", "Escalate red items to both team leads within one working day."],
            ["Mitigations", "Agree an interface contract first so both sides build in parallel. Fallback: {fallback}", "Cut scope, add people only if the work parallelises, or move the consumer's date; adding people late slows a project."],
            ["Cadence", "Review the dependency board twice a week, record slips with cause, and ask providers to give a date range with confidence.", "Close each dependency with a short integration test."],
        ],
        "metrics": ["Slack (days)|days_until_due - provider_eta_days - buffer_days|{:+.0f}", "Provider slip against the need (days)|provider_eta_days - days_until_due|{:+.0f}"],
    },
    "11-management/07-meeting-action-extractor": {
        "fields": ["attendees|Attendees|list|Alice, Bob, Carol", "decisions|Decisions made|list|Adopt the Cargo workspace layout, Make 100 percent coverage a merge gate", "total_actions|Action items found|number|6", "owned_actions|Action items with an owner and a due date|number|5", "default_due|Default due date if none was stated|text|End of the week"],
        "sections": [
            ["Source", "Notes: {input}", "Attendees: {attendees}"],
            ["Decisions", "*{decisions}", "Record each as a sentence with the decision, the owner and the reason. Distinguish decisions from discussions."],
            ["Action table", "Columns: action (verb first), owner (one name), due date (calendar date), status, link. Convert phrases such as by Friday to the actual date.", "Items with no owner or no date are not actions: flag them and assign by name in the meeting follow-up."],
            ["Completeness", "{owned_actions} of {total_actions} actions have both an owner and a due date. Default due date when none was stated: {default_due}.", "One owner per item, even if several people help."],
            ["Follow-through", "Send notes within 24 hours, with actions at the top. Review open actions at the start of the next meeting and carry over only with a new date and reason.", "Track actions in the team tracker, not in the notes alone."],
        ],
        "metrics": ["Actions fully specified|owned_actions / total_actions|{:.0%}", "Actions needing an owner or date|total_actions - owned_actions|{:.0f}"],
    },
    "11-management/08-tech-strategy-summarizer": {
        "fields": ["decision|Decision requested|text|Adopt the Universal Agent IR and the Rust transpiler across all 120 agents", "alternatives|Alternatives considered|list|Keep per-agent Python scripts, Adopt a third-party agent framework", "risks|Key risks|list|Transpiler gaps for dynamic features, Retraining the team in Rust", "weeks|Delivery time (weeks)|number|16", "engineers|Engineers assigned|number|6", "weekly_cost|Loaded cost per engineer-week (USD)|number|4000"],
        "sections": [
            ["Decision requested", "RFC: {input}", "Ask: {decision}", "Lead with the decision and the date it is needed, then the reason in two lines."],
            ["Options", "Alternatives considered:", "*{alternatives}", "Compare options on cost, risk, time to value and reversibility in a small table; say why the others lose."],
            ["Risks", "*{risks}", "Each risk gets a mitigation and a trigger for reversing the decision."],
            ["Cost and timeline", "{weeks} weeks with {engineers} engineers at {weekly_cost} USD per engineer-week.", "State the milestones, the first user-visible win in 4 to 6 weeks, and what stops while the team works on this."],
            ["Memo rules", "One page: context, decision, options, risks, cost, next step. Plain language, numbers instead of adjectives, an owner, and a link to the full RFC.", "End with the exact approval wanted and who has to give it."],
        ],
        "metrics": ["Person-weeks|weeks * engineers|{:,.0f}", "Estimated cost|weeks * engineers * weekly_cost|${:,.0f}", "Cost per month|engineers * weekly_cost * 4.33|${:,.0f}"],
    },
    "11-management/09-team-health-pulse": {
        "fields": ["deploys_per_week|Deployments per week|number|7", "lead_time_h|Lead time for changes (hours)|number|3", "cfr_pct|Change failure rate (percent)|number|2", "mttr_min|Time to restore (minutes)|number|18", "morale|Team morale (1 to 5 survey)|number|3.8"],
        "sections": [
            ["Snapshot", "DORA snapshot: {input}", "Deploys per week {deploys_per_week}; lead time {lead_time_h} h; failure rate {cfr_pct} percent; restore time {mttr_min} minutes; morale {morale} of 5."],
            ["DORA tiers", "Elite: deploy on demand (multiple per day), lead time under 1 day, change failure rate up to 5 percent, restore under 1 hour. High: daily to weekly, under 1 week, up to 10 percent, under 1 day. Medium: weekly to monthly, 1 week to 1 month. Low: slower.", "Place each metric in a tier separately; the team tier is its weakest of the four."],
            ["Read with care", "Metrics are for team improvement, not ranking or individual performance. Gaming is certain when they appear in reviews. Use medians and trends over 6 to 12 weeks.", "A very low failure rate with rare deploys can mean fear, not quality."],
            ["Morale indicators", "Pulse survey every two weeks with 5 questions: workload, clarity, autonomy, support, would recommend. Watch trends, turnover, after-hours work, PR wait times and on-call load.", "Below 3.5 or a drop of 0.5 triggers a retro and a manager follow-up within a week."],
            ["Actions", "Pick one metric to improve per quarter. Speed fixes: smaller batches, trunk-based development, faster CI. Stability fixes: tests, progressive delivery, runbooks.", "Share results openly with the team first."],
        ],
        "metrics": ["Lead time (days)|lead_time_h / 24|{:.2f}", "Failed deployments per week|deploys_per_week * cfr_pct / 100|{:.2f}", "Morale against a 4.0 target|morale / 4|{:.0%}"],
    },
    "11-management/10-quarterly-roadmap-brief": {
        "fields": ["milestones|Total milestones|number|10", "on_track|Milestones on track|number|9", "behind_weeks|Weeks the slipping item is behind|number|1", "budget_pct|Budget used (percent)|number|62", "elapsed_pct|Quarter elapsed (percent)|number|70"],
        "sections": [
            ["Quarter status", "Inputs: {input}", "{on_track} of {milestones} milestones on track; budget used {budget_pct} percent with {elapsed_pct} percent of the quarter gone."],
            ["Delivery confidence", "Rate each milestone: High (done or on track with no open risk), Medium (risk with a plan), Low (slipping or unplanned dependency). Give a date and an owner for every Medium or Low.", "A slipping item {behind_weeks} week(s) behind: say whether it moves the release and what recovery is planned."],
            ["Risks", "Top 3 risks with likelihood, impact, owner and mitigation. Include dependencies, hiring, and technical unknowns. Separate risks (might happen) from issues (happening).", "Do not hide amber items; boards trust teams who flag early."],
            ["Spend", "Compare budget burn to time elapsed. Burn faster than time without matching progress needs an explanation.", "Show forecast to completion, not only actuals."],
            ["Next quarter", "Propose the top 3 to 5 bets with expected outcomes, what will be dropped, and the decisions needed from the room.", "One slide per theme; ratings as colour plus words for accessibility."],
        ],
        "metrics": ["Milestones on track|on_track / milestones|{:.0%}", "Budget burn versus time elapsed|budget_pct / elapsed_pct|{:.2f}x", "Milestones at risk|milestones - on_track|{:.0f}"],
    },
}
