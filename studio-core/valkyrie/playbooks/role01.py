"""Playbooks for the Product Management agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "01-product-management/01-prd-architect": {
        "fields": ["target_users|Target users|text|IT administrators at companies with 500+ employees", "success_metric|Success metric|text|Cut time-to-first-login from 20 to 5 minutes", "constraints|Constraints|longtext|Must support SAML 2.0 and Okta; no new database\nAudit log entry for every login", "launch_quarter|Target launch|text|Q3"],
        "sections": [
            ["Problem and opportunity", "Brief: {input}", "Who it is for: {target_users}", "A PRD starts from a problem a named user has today, not from a solution. Confirm the problem is evidenced (tickets, interviews, usage data) before committing roadmap space."],
            ["Goals", "Primary goal: {success_metric}", "Every goal needs a baseline, a target and a date. If any of the three is missing, treat the goal as a hypothesis."],
            ["Non-goals", "Anything not needed to reach: {success_metric}", "List at least three things this release will NOT do, so scope reviews have something to point at."],
            ["Requirements and constraints", "*{constraints}", "Write each requirement as a testable statement: a user, an action and an observable result."],
            ["Acceptance criteria", "Given {target_users} with the feature enabled, when they complete the main flow from the brief, then {success_metric} is measurable.", "Add one Given/When/Then per requirement, covering the failure path as well as the happy path."],
            ["Launch plan", "Target launch: {launch_quarter}", "Gate launch on: security review, docs, support training, rollback plan."],
        ],
        "metrics": [],
    },
    "01-product-management/02-roadmap-prioritizer": {
        "fields": ["reach|Reach (users per quarter)|number|5000", "impact|Impact (0.25, 0.5, 1, 2 or 3)|number|3", "confidence|Confidence (0 to 1)|number|0.8", "effort|Effort (person-months)|number|4"],
        "sections": [
            ["Scoring inputs", "Item: {input}", "Reach {reach} users per quarter, impact {impact}, confidence {confidence}, effort {effort} person-months."],
            ["How to read the score", "RICE = reach x impact x confidence / effort. Compare scores only within the same quarter and the same scale for reach and effort.", "Below 50% confidence the score is a guess: schedule discovery work before build."],
            ["Tiering", "Tier 1 (do now): score in the top third of the backlog. Tier 2 (next): middle third. Tier 3 (park): bottom third, or confidence below 0.5.", "Re-score every quarter: reach and effort estimates drift."],
            ["Sanity checks", "Impact scale: 3 massive, 2 high, 1 medium, 0.5 low, 0.25 minimal. Anything scored 3 needs a stated mechanism, not enthusiasm.", "Effort should include design, QA, docs and rollout, not only engineering. Round up to the nearest half person-month."],
        ],
        "metrics": ["RICE score|reach * impact * confidence / effort|{:,.1f}", "Impact per person-month|reach * impact / effort|{:,.0f}"],
    },
    "01-product-management/03-user-story-splitter": {
        "fields": ["persona|Primary persona|text|Workspace admin", "epic_points|Epic size (story points)|number|55", "velocity|Team velocity (points per sprint)|number|34", "dependencies|Known dependencies|list|Payments provider API, invoice PDF service", "done_criteria|Definition of done|longtext|Code reviewed and merged\nUnit and integration tests pass\nDocs and release note updated"],
        "sections": [
            ["Epic under review", "Epic: {input}", "Persona: {persona}", "Dependencies to resolve first: {dependencies}"],
            ["Splitting patterns", "Split by workflow step, by business rule variation, by data type, by interface, by happy path first then exceptions, or by CRUD operation. Avoid splitting by technical layer (front end story, back end story): it delivers no user value alone.", "Spike stories are allowed only when a risk blocks estimation; time-box them to 1 to 2 days."],
            ["INVEST check per story", "Independent: can be built in any order. Negotiable: describes the need, not the design. Valuable: a user sees a change. Estimable: the team can size it. Small: fits within one sprint, ideally 1 to 3 days. Testable: has Given/When/Then criteria.", "Any story above 8 points fails Small and must be split again."],
            ["Acceptance criteria template", "Given {persona} is signed in, when they perform the action in the epic, then the visible result is confirmed and an audit event is recorded.", "Write one failure criterion per story: invalid input, missing permission, downstream timeout."],
            ["Definition of done", "*{done_criteria}", "Stories are not done until they meet the shared definition, even if the demo works."],
            ["Delivery outlook", "Epic of {epic_points} points at a velocity of {velocity} points per sprint.", "Plan for at most 70 to 80 percent of velocity on one epic; the rest absorbs bugs and interrupts."],
        ],
        "metrics": ["Sprints to deliver at full velocity|epic_points / velocity|{:.1f}", "Sprints at 75% focus|epic_points / (velocity * 0.75)|{:.1f}", "Minimum story count (5 points max)|epic_points / 5|{:,.0f}"],
    },
    "01-product-management/04-competitive-intel": {
        "fields": ["our_product|Our product|text|Valkyrie Studio", "competitors|Competitors tracked|list|Competitor X, Competitor Y", "our_price|Our price (USD per seat per month)|number|29", "competitor_price|Competitor price (USD per seat per month)|number|35", "differentiators|Our claimed differentiators|list|Local-first execution, 120 ready agents, Rust export"],
        "sections": [
            ["Competitor moves", "Evidence: {input}", "Competitors in scope: {competitors}", "Log each move with date, source URL and confidence. A launch announcement is a claim; a pricing page or changelog is evidence."],
            ["Feature parity matrix", "Rows are customer jobs, columns are {our_product} and each competitor. Score each cell: none, partial, parity, ahead.", "Mark a gap as critical only if it appeared in at least three lost-deal notes in the last quarter."],
            ["Differentiation", "Claimed differentiators: {differentiators}", "A differentiator counts only if it is true, valuable to the buyer and hard to copy within two quarters. Strike the rest from the pitch."],
            ["Pricing position", "Our price {our_price} versus competitor {competitor_price} USD per seat per month.", "Do not match price cuts reflexively; first check whether the competitor changed packaging or limits."],
            ["Response plan", "Respond (roadmap change), neutralize (messaging and battlecard), or ignore. Choose ignore when the move does not touch your top two segments.", "Refresh the battlecard within 5 working days of any critical move."],
        ],
        "metrics": ["Price gap vs competitor|(our_price - competitor_price) / competitor_price|{:.1%}", "Annual price delta per 100 seats|(our_price - competitor_price) * 100 * 12|{:+,.0f} USD"],
    },
    "01-product-management/05-voice-of-customer": {
        "fields": ["top_theme|Top theme|text|CSV export timeouts", "theme_mentions|Mentions of top theme|number|180", "total_responses|Total responses analysed|number|1200", "affected_arr|ARR of accounts citing the theme (USD)|number|450000", "total_arr|Total ARR (USD)|number|4800000"],
        "sections": [
            ["Raw feedback", "Batch: {input}", "{total_responses} responses analysed; leading theme: {top_theme}."],
            ["Clustering method", "Tag each verbatim with one primary theme and at most one secondary. Merge themes only when the underlying job or failure is the same; keep bug, usability and missing feature separate.", "Re-read a random 10 percent sample of tags; if disagreement exceeds 15 percent, tighten the theme definitions."],
            ["Frequency versus churn risk", "Rank themes on two axes: share of responses and share of ARR. A theme with 5 percent of mentions but 30 percent of ARR outranks a loud, low-value one.", "Weight detractor (NPS 0 to 6) verbatims double when estimating churn risk."],
            ["Evidence for the top theme", "{top_theme}: {theme_mentions} mentions, {affected_arr} USD ARR affected.", "Attach three representative quotes and the account IDs behind them before sending to engineering."],
            ["Recommended actions", "Hot: bug or outage-class theme with ARR exposure above 10 percent. Plan: recurring request above 5 percent of mentions. Watch: everything else.", "Close the loop: tell customers who raised a theme what changed, within one release cycle."],
        ],
        "metrics": ["Theme share of responses|theme_mentions / total_responses|{:.1%}", "ARR exposure|affected_arr / total_arr|{:.1%}", "Average ARR per citing account mention|affected_arr / theme_mentions|${:,.0f}"],
    },
    "01-product-management/06-launch-readiness": {
        "fields": ["launch_date|Launch date|text|2026-12-02", "gates_total|Total gates|number|12", "gates_green|Gates signed off|number|9", "owners|Gate owners|list|Engineering: Priya, Docs: Marco, Legal: Ana, Support: Dev", "rollback_plan|Rollback plan|text|Feature flag off within 5 minutes, DB migration reversible"],
        "sections": [
            ["Gate status", "Reported state: {input}", "Gates signed off: {gates_green} of {gates_total}. Owners: {owners}."],
            ["Required gates", "Engineering: tests green, load test passed, on-call briefed. Security: pentest findings triaged, no open high. Docs: quickstart and API reference live. Legal: terms, privacy and licenses cleared. Support: macros, escalation path, status page copy ready. Billing: plans, invoices and tax verified.", "Every gate needs a named owner and a dated sign-off, not a verbal OK."],
            ["Go / no-go rules", "Go: all gates green, or amber with a written mitigation and an accountable owner. No-go: any red security, legal or billing gate.", "Decide at T minus 48 hours for {launch_date}; late surprises after that need an explicit exception."],
            ["Rollback and comms", "Rollback: {rollback_plan}", "Test the rollback in staging before launch day. A rollback nobody rehearsed is a hope."],
            ["Day-of checklist", "War room channel open, dashboards pinned, error budget alert armed, comms drafts approved, support on elevated staffing for 48 hours.", "Run a post-launch review within 10 working days comparing predicted and actual adoption."],
        ],
        "metrics": ["Readiness|gates_green / gates_total|{:.0%}", "Gates remaining|gates_total - gates_green|{:.0f}"],
    },
    "01-product-management/07-pricing-modeler": {
        "fields": ["price_per_seat|Price (USD per seat per month)|number|29", "seats|Seats per account|number|10", "tokens_included_k|Included tokens per seat (thousands)|number|100", "cogs_per_1k|Inference COGS (USD per 1k tokens)|number|0.002", "other_cogs|Other COGS per seat (USD per month)|number|3", "utilization|Share of included tokens used (percent)|number|80"],
        "sections": [
            ["Tier assumptions", "Tier: {input}", "{seats} seats at {price_per_seat} USD, {tokens_included_k}k tokens included per seat, {utilization} percent utilization."],
            ["Margin model", "Gross margin per seat = price - inference COGS - other COGS (support, hosting, payment fees). Inference COGS = included tokens x utilization x cost per 1k tokens.", "Healthy SaaS targets 75 to 80 percent gross margin; AI-heavy products often land at 60 to 70 percent. Below 55 percent the tier needs a usage cap or overage price."],
            ["Seat versus usage", "Seat pricing is predictable for buyers but exposes you to heavy users. Usage pricing aligns cost and revenue but makes budgets hard to forecast.", "A hybrid works well: a seat fee with an included pool and metered overage at 1.5 to 3 times cost."],
            ["Stress tests", "Rerun the model at 100 percent utilization, at 2x token price, and at 50 percent seat discounts for annual deals.", "Flag any scenario where gross margin per seat falls below zero: that is a loss-making segment."],
            ["Packaging guidance", "Three tiers is the default: entry, core, scale. Put the limit on the metric that tracks value (agents run, seats), not on features customers consider basic.", "Grandfather existing customers for one renewal cycle to protect retention."],
        ],
        "metrics": ["ARPA (monthly)|price_per_seat * seats|${:,.0f}", "Inference COGS per seat|tokens_included_k * cogs_per_1k * utilization / 100|${:,.2f}", "Gross margin per seat|price_per_seat - tokens_included_k * cogs_per_1k * utilization / 100 - other_cogs|${:,.2f}", "Gross margin|(price_per_seat - tokens_included_k * cogs_per_1k * utilization / 100 - other_cogs) / price_per_seat|{:.1%}"],
    },
    "01-product-management/08-experiment-designer": {
        "fields": ["baseline_pct|Baseline conversion (percent)|number|35", "mde_pp|Minimum detectable effect (percentage points)|number|3", "daily_users|Eligible users per day|number|800", "guardrails|Guardrail metrics|list|Support tickets per user, Activation D7, Error rate", "primary_metric|Primary metric|text|D1 activation rate"],
        "sections": [
            ["Hypothesis", "Hypothesis: {input}", "Primary metric: {primary_metric}", "Write it as: if we change X for segment Y, metric Z moves by at least MDE because of mechanism M."],
            ["Design", "Randomize at the user level, 50/50, with a stable hash on user id. Pre-register the primary metric, the MDE, the runtime and the analysis method before launch.", "Use alpha 0.05 two-sided and power 0.8. Reduce variance with CUPED only if a pre-period covariate correlates above 0.5."],
            ["Sample size", "Baseline {baseline_pct} percent, MDE {mde_pp} points, about {daily_users} eligible users per day.", "Rule of thumb for 80 percent power: n per arm = 16 x p x (1 - p) / delta squared. Halving the MDE quadruples the sample."],
            ["Guardrails", "*{guardrails}", "Stop the test early only for a guardrail breach set in advance, never for a promising p-value (peeking inflates false positives)."],
            ["Validity checks", "Sample ratio mismatch: chi-square on assignment counts, investigate if p is below 0.001. Run at least one full week to cover weekday cycles. Check novelty effects after day 7.", "Decision rule: ship if the primary metric is significant and no guardrail regresses beyond its limit; otherwise keep control."],
        ],
        "metrics": ["Sample size per arm|16 * (baseline_pct / 100) * (1 - baseline_pct / 100) / ((mde_pp / 100) * (mde_pp / 100))|{:,.0f}", "Runtime in days (both arms)|2 * 16 * (baseline_pct / 100) * (1 - baseline_pct / 100) / ((mde_pp / 100) * (mde_pp / 100)) / daily_users|{:.1f}", "Relative lift to detect|mde_pp / baseline_pct|{:.1%}"],
    },
    "01-product-management/09-release-notes-writer": {
        "fields": ["version|Version|text|v2.1.0", "release_date|Release date|text|2026-11-18", "audience|Audience|text|Developers and workspace admins", "breaking_changes|Breaking changes|list|Legacy /run-agent route removed, Token refresh now requires re-login", "upgrade_steps|Upgrade steps|longtext|Update the CLI to 2.1.0\nRe-authenticate with valkyrie login\nRun valkyrie doctor to verify"],
        "sections": [
            ["Release header", "Version {version}, released {release_date}, for {audience}.", "Lead with the single change a customer cares about most, in one sentence of benefit, not implementation."],
            ["What changed", "Source log: {input}", "Group entries as New, Improved, Fixed. Rewrite commit text from the user's point of view: 'You can now export invoices' not 'feat: add invoice export'."],
            ["Breaking changes", "*{breaking_changes}", "Put breaking changes at the top, state who is affected, what to do and by what date. Never bury them under Fixed."],
            ["Upgrade steps", "*{upgrade_steps}", "Every step must be copy-pasteable and verified on a clean machine."],
            ["Style rules", "One line per item, present tense, no internal ticket IDs or jargon. Link to docs for anything needing more than two sentences.", "Security fixes: describe the impact and affected versions, not the exploit; link to the advisory."],
        ],
        "metrics": [],
    },
    "01-product-management/10-stakeholder-brief": {
        "fields": ["period|Reporting period|text|Week 46", "milestones_planned|Milestones planned|number|10", "milestones_done|Milestones delivered|number|8", "risks|Top risks|list|SSO vendor delay, Hiring gap in platform team", "asks|Decisions or asks|list|Approve 2 contractors, Confirm Dec 2 launch date"],
        "sections": [
            ["Headline", "Period: {period}", "Updates received: {input}", "Open with one sentence that states overall status (green, amber or red) and why."],
            ["Delivery", "Delivered {milestones_done} of {milestones_planned} planned milestones.", "Report against the plan, not against last week. Amber means recovery plan in hand; red means help needed."],
            ["Risks", "*{risks}", "Each risk needs an owner, a likelihood, an impact and a next step with a date. Drop risks with no owner."],
            ["Asks and decisions", "*{asks}", "Phrase each as a decision with a deadline and a default: 'Approve by Friday or we proceed with option B'."],
            ["Format rules", "Keep the digest under 300 words. Put numbers with their trend and their target. Executives read the first three lines; make them sufficient.", "Send at the same time every week so the absence of a brief is itself a signal."],
        ],
        "metrics": ["Delivery rate|milestones_done / milestones_planned|{:.0%}", "Milestones behind plan|milestones_planned - milestones_done|{:.0f}"],
    },
}
