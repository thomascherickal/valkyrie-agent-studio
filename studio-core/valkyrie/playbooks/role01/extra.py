"""Playbooks for the Product Management agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "01-product-management/11-persona-builder": {
        "fields": ["segment|Segment name|text|IT administrators at mid-size companies", "interviews|Interviews analysed|number|12", "supporting|Interviews that show the main behaviour|number|9", "goals|Top goals|list|Onboard staff in one day; pass the licence audit; stop chasing approvals", "pains|Top frustrations|list|Spreadsheet tracking; slow approvals; no audit trail"],
        "sections": [
            ["Persona summary", "Research: {input}", "Segment: {segment}, based on {interviews} interviews.", "A persona is a summary of a pattern seen in research, not a person you invented. Give it a role-based name, not a stock-photo name and age."],
            ["Goals", "*{goals}", "Write goals as outcomes the person wants (for example, pass the audit), not as features they might use."],
            ["Frustrations", "*{pains}", "Keep the person's own words in quotes next to each frustration. Quotes are the evidence a reader can check."],
            ["Evidence strength", "{supporting} of {interviews} interviews showed the main behaviour.", "Fewer than 3 interviews is an anecdote. Between 3 and 5 is a hypothesis. Above half of a sample of 8 or more is a pattern."],
            ["How to use it", "Use the persona to test each roadmap item with one question: does this help {segment} reach a goal or remove a frustration?", "Retire or rewrite a persona when new research contradicts it, and note the date of the last review."],
        ],
        "metrics": ["Share of interviews that support the pattern|supporting / interviews|{:.0%}"],
    },
    "01-product-management/12-jtbd-mapper": {
        "fields": ["customer|Customer type|text|Compliance lead at a 300-person software company", "trigger|Triggering event|text|A failed access-review audit", "alternative|What they used before|text|Shared spreadsheet and email reminders", "outcomes|Outcomes they measure|list|Time to produce audit evidence; number of overdue reviews; auditor findings", "switch_cost|Switching effort (hours)|number|40"],
        "sections": [
            ["Job statement", "Interview: {input}", "When {trigger}, a {customer} wants to get the review done so they can pass the audit without a scramble.", "Use the format: When [situation], I want to [motivation], so I can [outcome]. It describes progress, not a product."],
            ["Forces of progress", "Push: the old way ({alternative}) failed at {trigger}.", "Pull: the new way promises the outcomes listed below.", "Anxiety (cost of change, about {switch_cost} hours here) and habit pull the other way. Name both, because they explain why people do not switch."],
            ["Outcomes to measure", "*{outcomes}", "Write each outcome as a direction, a metric and a context: minimise the time to produce audit evidence."],
            ["Competing alternatives", "Current alternative: {alternative}.", "Include non-products such as doing nothing, hiring someone or building it in-house. These compete for the same job."],
            ["Product implications", "Prioritise work that lowers the anxiety or the {switch_cost} hours of effort before adding features.", "Check each idea against the job: does it help the customer make progress, or only look impressive in a demo?"],
        ],
        "metrics": ["Switching effort in working days|switch_cost / 8|{:.1f}"],
    },
    "01-product-management/13-kano-classifier": {
        "fields": ["feature|Feature being rated|text|Single sign-on", "respondents|Respondents|number|180", "happy_with|Percent happy if it exists|number|72", "unhappy_without|Percent unhappy if it is missing|number|55", "segment|Respondent segment|text|Existing customers with 200+ seats"],
        "sections": [
            ["Survey readout", "Results: {input}", "Feature: {feature}. Segment: {segment}. Respondents: {respondents}.", "Ask every feature as a pair: how would you feel if it were present, and how would you feel if it were absent."],
            ["Classification rules", "Must-have: unhappy when absent, only neutral when present. Performance: happier as it improves. Delighter: happy when present, no complaint when absent. Indifferent: neither answer moves.", "Reverse features (people dislike having them) and questionable answers must be reported, not forced into a bucket."],
            ["Reading this feature", "{feature}: {happy_with} percent are happy with it and {unhappy_without} percent are unhappy without it.", "A high number on both sides points to a must-have. A high happy share with a low unhappy share points to a delighter."],
            ["Sample quality", "With {respondents} respondents each answer moves a category by about 0.5 percent. Fewer than 30 per segment makes the buckets unreliable.", "Compare segments before merging them: a must-have for enterprise can be a delighter for small teams."],
            ["Roadmap use", "Ship must-haves first, balance performance features against cost, and use delighters for differentiation once the basics are in place.", "Re-survey every 12 months: today's delighter becomes tomorrow's must-have."],
        ],
        "metrics": ["Gap between wanting it and missing it (points)|unhappy_without - happy_with|{:+.0f}", "Weight of one respondent (percent)|100 / respondents|{:.2f}"],
    },
    "01-product-management/14-north-star-designer": {
        "fields": ["metric|Candidate north star|text|Weekly releases reviewed and shipped by a team", "current|Current value per week|number|1400", "target|Target value per week|number|2100", "weeks|Weeks to reach the target|number|26", "guardrail|Guardrail metric|text|Rollbacks per hundred releases"],
        "sections": [
            ["Candidate north star", "Goals: {input}", "Candidate: {metric}. Guardrail: {guardrail}.", "A good north star measures delivered customer value, moves with revenue over time and can be influenced by every team."],
            ["Tests it must pass", "Does it reflect value received, not effort or money? Is it a count or rate you can compute weekly? Can a team move it within a quarter?", "Reject vanity totals such as registered users and revenue taken alone: they hide whether customers got value."],
            ["Metric tree", "Break the north star into four inputs: breadth (how many teams), depth (releases per team), frequency (how often) and efficiency (time from review to ship).", "Give each input to one owning team and one target for the quarter, so the tree has owners."],
            ["Growth path", "From {current} to {target} per week in {weeks} weeks is the plan.", "Check that the target is reachable through the inputs and not only through new customers."],
            ["Guardrails", "Pair the metric with {guardrail} so the team cannot improve it by cutting quality.", "Review the metric every quarter and retire it if it stops predicting retention."],
        ],
        "metrics": ["Growth required|target / current - 1|{:.0%}", "Growth needed per week|(target - current) / weeks|{:,.1f}"],
    },
    "01-product-management/15-opportunity-tree-builder": {
        "fields": ["outcome|Desired outcome|text|Raise week-4 retention from 31 to 40 percent", "opportunities|Customer opportunities|list|Setup takes too long; Reports are hard to share; No guidance after first week", "solutions|Candidate solutions|list|Guided setup checklist; One-click report sharing; Weekly progress email", "baseline|Baseline retention (percent)|number|31", "goal|Target retention (percent)|number|40"],
        "sections": [
            ["Outcome", "Brief: {input}", "Outcome: {outcome}.", "An outcome is a change in customer behaviour you can measure, not a feature or a launch date."],
            ["Opportunities", "*{opportunities}", "Phrase each opportunity as a customer need, pain or desire, from research. Group duplicates and split any that are too big."],
            ["Solutions", "*{solutions}", "Generate at least three solutions per opportunity you pursue, so you compare options and do not fall for the first idea."],
            ["Assumption tests", "For each solution, list the riskiest assumption (desirability, usability, feasibility, viability) and a test that takes days, not weeks.", "Prototype tests and one-question surveys are enough to cut weak ideas before engineering time is spent."],
            ["Target", "Move retention from {baseline} to {goal} percent.", "Pick one opportunity at a time, compare it with its siblings and finish the test before starting the next."],
        ],
        "metrics": ["Points of retention to gain|goal - baseline|{:.0f}", "Relative improvement needed|goal / baseline - 1|{:.0%}"],
    },
    "01-product-management/16-beta-program-manager": {
        "fields": ["feature|Feature in beta|text|Reporting module", "invited|Accounts invited|number|40", "active|Accounts that used it in week 2|number|26", "weeks|Beta length (weeks)|number|6", "exit_criteria|Exit criteria|list|Crash-free sessions above 99.5 percent; Weekly use by 60 percent of cohort; No open severity-1 bugs"],
        "sections": [
            ["Beta scope", "Plan: {input}", "Feature: {feature}. {invited} accounts, {weeks} weeks.", "State what is in and out of the beta, and what customers may expect from you: support hours, data safety and the end date."],
            ["Choosing the cohort", "Choose accounts that cover your segments, include some heavy users and some sceptics, and have a champion who will respond.", "Avoid only friendly accounts. They hide the problems that new customers will hit."],
            ["Feedback loop", "Collect usage data, a short weekly survey and two calls per account.", "Triage feedback twice a week and reply to every report, so people keep taking part."],
            ["Exit gate", "*{exit_criteria}", "Agree the gate before the beta starts. Decide in advance what a no-go means: extend, fix or stop."],
            ["Engagement check", "{active} of {invited} accounts were active in week 2.", "Below 50 percent activity, fix onboarding before collecting any more opinions."],
        ],
        "metrics": ["Week-2 activation of the cohort|active / invited|{:.0%}", "Accounts still to activate|invited - active|{:,.0f}"],
    },
    "01-product-management/17-sunset-planner": {
        "fields": ["feature|Feature to retire|text|Legacy CSV exporter", "accounts_using|Accounts still using it|number|96", "total_accounts|Total accounts|number|3200", "hours_month|Maintenance hours per month|number|30", "notice_days|Notice you will give (days)|number|120"],
        "sections": [
            ["Sunset case", "Usage: {input}", "Feature: {feature}. {accounts_using} of {total_accounts} accounts still use it.", "Retire a feature when its upkeep cost is larger than the value it delivers to the customers who still use it."],
            ["Customer impact", "Group the remaining accounts by plan and revenue. Contact the highest-value ones personally.", "List what each group can no longer do and what replaces it. Missing a migration path is the usual cause of a sunset backlash."],
            ["Timeline", "Give {notice_days} days of notice with reminders at 90, 30 and 7 days before the date.", "Announce in product, by email and in the changelog on the same day, and keep a page that answers common questions."],
            ["Migration help", "Offer a migration guide, a script where possible and a support contact for the named accounts.", "Track how many accounts migrate each week and extend the date for strategic customers if needed."],
            ["Go and rollback gates", "Switch the feature off for a small group first, watch support volume and keep a flag to restore it for a week after the shutdown.", "Delete the code only after the restore window has passed."],
        ],
        "metrics": ["Share of accounts affected|accounts_using / total_accounts|{:.1%}", "Maintenance hours saved per year|hours_month * 12|{:,.0f}"],
    },
    "01-product-management/18-pmf-survey-analyst": {
        "fields": ["very|Very disappointed responses|number|54", "somewhat|Somewhat disappointed responses|number|63", "not|Not disappointed responses|number|33", "best_segment|Segment with the strongest score|text|Digital agencies", "main_benefit|Benefit people name most|text|One place to approve client work"],
        "sections": [
            ["Survey readout", "Results: {input}", "Strongest segment: {best_segment}. Most named benefit: {main_benefit}.", "The question is: how would you feel if you could no longer use this product? Report the share who answer very disappointed."],
            ["Reading the score", "Around 40 percent very disappointed is the usual threshold for product-market fit. Below 25 percent the product has not found its market.", "A score from fewer than 40 respondents is noise. Re-run the survey with active users only."],
            ["Segment analysis", "Split by role, company size and use case. The best segment shows where to focus.", "Sell and build for {best_segment} first. Do not average a strong segment away with weak ones."],
            ["What to build next", "Read the somewhat disappointed group: what stops them from becoming very disappointed?", "Ignore the not disappointed group for roadmap purposes. Use their answers to avoid targeting the wrong customers."],
            ["Follow up", "Interview five very disappointed users to learn the benefit in their words, and reuse that wording in your messaging.", "Repeat the survey each quarter to see whether the score is moving."],
        ],
        "metrics": ["Total responses|very + somewhat + not|{:,.0f}", "Very disappointed share|very / (very + somewhat + not)|{:.0%}"],
    },
    "01-product-management/19-build-buy-evaluator": {
        "fields": ["capability|Capability needed|text|In-app e-signature", "vendor_year|Vendor cost per year (USD)|number|45000", "build_months|Build effort (engineer-months)|number|5", "engineer_month|Cost of one engineer-month (USD)|number|16000", "maintain_year|Yearly upkeep if built (USD)|number|20000"],
        "sections": [
            ["Decision brief", "Request: {input}", "Capability: {capability}.", "Ask first whether this capability is core to what customers pay for. Build what differentiates you and buy what everyone has."],
            ["Cost over three years", "Buy: three years of vendor fees. Build: the one-time effort plus upkeep for each year.", "Include integration time, security review and training on the buy side, and on-call and bug fixing on the build side."],
            ["Speed to value", "Buying is usually faster to first release, building is faster to fit. Compare the months to a usable version, not to a perfect one.", "A vendor that needs six months of integration is not a quick option."],
            ["Risks", "Vendor: lock-in, price rises, outages and data location. Build: scope growth, key-person risk and compliance work you would own.", "Ask the vendor for an exit plan: data export, contract term and what happens if they are acquired."],
            ["Recommendation rule", "Buy when the capability is standard, the vendor passes security review and three-year cost is lower. Build when it is core or the vendor cannot meet a hard requirement.", "Record the decision, the assumptions and a review date."],
        ],
        "metrics": ["Build cost over 3 years (USD)|build_months * engineer_month + maintain_year * 3|${:,.0f}", "Buy cost over 3 years (USD)|vendor_year * 3|${:,.0f}", "Years until building pays back|build_months * engineer_month / (vendor_year - maintain_year)|{:.1f}"],
    },
    "01-product-management/20-product-ops-cadence-planner": {
        "fields": ["teams|Number of product teams|number|6", "meeting_hours|Hours per week each person spends in product meetings|number|9", "people|People involved|number|48", "pain|Biggest coordination problem|text|Roadmap changes surprise sales and support", "audiences|Groups to keep informed|list|Sales; Support; Marketing; Leadership"],
        "sections": [
            ["Current rhythm", "Description: {input}", "Biggest problem: {pain}.", "Meetings exist to make decisions or share information. Move information sharing to written updates and keep meetings for decisions."],
            ["Weekly", "A short written update from each team, and one 30-minute review focused on decisions, blockers and metric changes.", "Publish the agenda in advance and end with named owners and dates."],
            ["Monthly and quarterly", "Monthly: metric review and roadmap change log. Quarterly: planning, retrospective and a customer review.", "Freeze the next quarter's roadmap two weeks before it starts so dependent teams can plan."],
            ["Keeping others informed", "*{audiences}", "Send each group a short change digest on a fixed day. Surprises come from irregular updates, not from the changes themselves."],
            ["Cost of the rhythm", "{people} people spend {meeting_hours} hours a week in meetings.", "Review the rhythm every quarter and remove any meeting that did not produce a decision."],
        ],
        "metrics": ["Meeting hours per week across the group|people * meeting_hours|{:,.0f}", "Meeting hours per team per week|people * meeting_hours / teams|{:,.0f}"],
    },
}
