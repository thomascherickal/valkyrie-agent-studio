"""Playbooks for the Growth & Product Analytics agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "09-growth-product-analytics/11-lifecycle-email-planner": {
        "fields": ["signups_month|New signups per month|number|9000", "setup_rate|Share who finish setup now (0 to 1)|number|0.38", "target_rate|Target share who finish setup (0 to 1)|number|0.5", "trial_days|Trial length (days)|number|14", "unsub_limit|Unsubscribe rate you will tolerate (0 to 1)|number|0.005"],
        "sections": [
            ["Goal", "Goals: {input}", "{signups_month} signups a month. Setup rate {setup_rate}, target {target_rate}. Trial: {trial_days} days.", "Lifecycle email helps a person do the next useful thing. It is not a broadcast of everything you have."],
            ["Triggers and timing", "Welcome at signup, a setup nudge at 24 hours if setup is not done, a teammate invite on day 3, a value recap on day 7 and a trial-ending sequence at the last 3 days.", "Trigger on behaviour (did or did not do something), and stop the sequence when the person does it."],
            ["Content", "One goal per email, one button, a clear subject and a plain first line. Show the specific next step and the benefit, and send from a real person.", "Personalise by what the person has done, not by their first name alone."],
            ["Frequency and care", "Cap messages per week, respect preferences and unsubscribes at once and suppress people in an open support conversation.", "Keep unsubscribes under {unsub_limit} per send and pause a sequence that goes over."],
            ["Measure", "Test each sequence against a holdout group that gets no email. Judge by setup completion and retention, not by opens.", "Review sequences quarterly and retire emails that do not move the goal."],
        ],
        "metrics": ["Extra people finishing setup each month|signups_month * (target_rate - setup_rate)|{:,.0f}", "People finishing setup each month now|signups_month * setup_rate|{:,.0f}"],
    },
    "09-growth-product-analytics/12-ltv-cac-modeler": {
        "fields": ["arpa|Average revenue per account per month (USD)|number|120", "margin|Gross margin (0 to 1)|number|0.78", "churn|Monthly churn (0 to 1)|number|0.025", "cac|Customer acquisition cost (USD)|number|1400", "payback_goal|Payback goal (months)|number|9"],
        "sections": [
            ["Inputs", "Inputs: {input}", "ARPA {arpa} USD, margin {margin}, churn {churn} a month, CAC {cac} USD.", "Lifetime value is the gross profit an average customer gives you over their life. Compare it with what it cost to win them."],
            ["Formulas", "Lifetime in months is 1 divided by monthly churn. LTV is ARPA x gross margin x lifetime. The LTV to CAC ratio is LTV divided by CAC. Payback months is CAC divided by monthly gross profit per account.", "Use gross margin, not revenue, or you overstate value."],
            ["Reading the ratio", "A ratio of 3 or more with payback inside 12 months is the usual healthy range. Below 1 you lose money on each customer. Far above 5 may mean you under-invest in growth.", "Compare payback with your goal of {payback_goal} months."],
            ["Sensitivity", "LTV is very sensitive to churn. Halving churn doubles lifetime. Check the result at churn plus and minus 1 point and by segment, since averages hide strong and weak groups.", "Use cohort retention, not a single blended rate, for the real curve."],
            ["Cautions", "Use blended and paid CAC side by side, include sales and onboarding costs, and cap lifetime at 5 years to avoid fantasy numbers for low-churn segments.", "Revisit the model quarterly with fresh cohort data."],
        ],
        "metrics": ["Customer lifetime (months)|1 / churn|{:.0f}", "Lifetime value (USD)|arpa * margin / churn|${:,.0f}", "LTV to CAC ratio|arpa * margin / churn / cac|{:.1f}", "Payback (months)|cac / (arpa * margin)|{:.1f}"],
    },
    "09-growth-product-analytics/13-experiment-backlog-ranker": {
        "fields": ["idea|Top idea|text|Shorter signup form", "impact|Impact (1 to 10)|number|7", "confidence|Confidence (0 to 1)|number|0.6", "effort_days|Effort (days)|number|3", "weekly_visitors|Weekly visitors to the page|number|40000"],
        "sections": [
            ["Backlog", "Ideas: {input}", "Top idea: {idea}. Impact {impact}, confidence {confidence}, effort {effort_days} days.", "A ranking system stops the loudest idea from winning. It makes the trade-off visible."],
            ["Score", "Use ICE or RICE: impact x confidence divided by effort. Score every idea the same way and re-score when evidence changes.", "Confidence comes from data and prior tests, not from enthusiasm."],
            ["Can it be tested", "Estimate the sample size needed for the lift you expect. With {weekly_visitors} visitors a week, check how many weeks it takes. Tests longer than 4 weeks need a bigger change or another metric.", "Prefer big, bold changes on low-traffic pages, and small ones on high-traffic pages."],
            ["Portfolio", "Mix quick wins, bigger bets and learning tests. Do not run overlapping tests on the same users and metric.", "Write the hypothesis, the primary metric and the decision rule before the test starts."],
            ["Review", "Record every result, including losses, in a searchable log and re-rank monthly. Count learning rate: decisions made per quarter.", "Retire ideas that keep losing similar tests."],
        ],
        "metrics": ["ICE-style score|impact * confidence / effort_days|{:.2f}", "Visitors per day|weekly_visitors / 7|{:,.0f}"],
    },
    "09-growth-product-analytics/14-referral-program-designer": {
        "fields": ["accounts|Active accounts|number|5000", "invite_rate|Share of accounts who invite someone (0 to 1)|number|0.08", "convert_rate|Share of invited accounts who become customers (0 to 1)|number|0.2", "reward_cost|Reward cost per converted referral, both sides (USD)|number|200", "cac|Current paid CAC (USD)|number|1200"],
        "sections": [
            ["Brief", "Brief: {input}", "{accounts} accounts. {invite_rate} invite and {convert_rate} of those convert.", "Referral works when customers already love the product and sharing is easy at the right moment."],
            ["Mechanics", "Reward both sides, tie the reward to a meaningful event such as a paid plan and ask at a happy moment, such as after a successful result. Give every customer a personal link.", "Make the invitee's first step trivial and show the benefit immediately."],
            ["Economics", "Compare the reward cost per converted referral with your paid CAC. Referral pays when its total cost per customer is clearly lower than {cac} USD.", "Include the cost of fraud, support and tool fees."],
            ["Fraud and fairness", "Block self-referrals by matching email domain, payment method and device, delay rewards until payment clears, cap rewards per account and review outliers.", "State the rules in plain words and apply them consistently."],
            ["Measure", "Track invite rate, conversion, referred-customer retention (often higher) and net cost per customer. Test the reward size and the placement of the prompt.", "Retire the program if the cost passes paid CAC."],
        ],
        "metrics": ["New customers from referral per period|accounts * invite_rate * convert_rate|{:,.0f}", "Cost per referred customer (USD)|reward_cost|${:,.0f}", "Saving against paid CAC per customer (USD)|cac - reward_cost|${:,.0f}"],
    },
    "09-growth-product-analytics/15-onboarding-funnel-auditor": {
        "fields": ["started|People who start onboarding|number|10000", "finished|People who reach first value|number|1900", "worst_step|Step with the biggest drop|text|Connect data", "worst_drop|Drop at that step (0 to 1)|number|0.61", "median_minutes|Median minutes to first value|number|38"],
        "sections": [
            ["Funnel", "Steps: {input}", "{started} start and {finished} reach first value. Worst step: {worst_step}, losing {worst_drop}. Median time to value: {median_minutes} minutes.", "Onboarding exists to get a new user to a first result fast. Every step that does not help costs people."],
            ["Biggest leak", "Fix {worst_step} first. Ask why: is it effort, trust, a permission, an error or confusion? Watch five recordings and read the support tickets from that step.", "Offer a shortcut such as sample data so people see value before the hard step."],
            ["Remove and reorder", "Delay anything not needed for first value: invitations, profile fields and verification where you can. Ask for permission when the person sees why you need it.", "Show progress and let people skip ahead."],
            ["Time to value", "Aim for first value inside the first session. Median time today is {median_minutes} minutes. Use templates and defaults to cut it.", "Segment by plan, device and acquisition source, since one flow rarely fits all."],
            ["Test and track", "Test one change at a time against a control, measure activation at day 7 and not only step completion and set an alert on funnel breaks.", "Review the funnel after every release that touches signup."],
        ],
        "metrics": ["Overall completion rate|finished / started|{:.1%}", "People lost before first value|started - finished|{:,.0f}"],
    },
    "09-growth-product-analytics/16-segment-discovery-analyst": {
        "fields": ["segments|Segments found|number|4", "top_share|Share of revenue from the best segment (0 to 1)|number|0.55", "top_users|Share of users in the best segment (0 to 1)|number|0.18", "top_retention|Retention of the best segment (0 to 1)|number|0.9", "low_retention|Retention of the weakest segment (0 to 1)|number|0.35"],
        "sections": [
            ["Segments", "Usage: {input}", "{segments} segments. The best holds {top_users} of users and {top_share} of revenue.", "A useful segment differs in behaviour, value and the right action. A segment you cannot act on is only a label."],
            ["How to find them", "Pick features that describe behaviour (frequency, depth, features used) and normalise them. Use clustering to propose groups, then name each in plain words and check each is stable across months.", "Validate with interviews, since a cluster is a hypothesis."],
            ["Value of each", "Compare retention, revenue per account, expansion and support cost. Retention of {top_retention} against {low_retention} shows how different the groups are.", "Check the segments are not just plan tiers in disguise."],
            ["Actions", "Tailor onboarding, messaging and pricing to each group, and aim acquisition at lookalikes of the best. For the weakest group, either find a path to value or stop spending on it.", "Give each segment an owner and a metric."],
            ["Keep it current", "Rebuild the segmentation twice a year, track movement between segments and check that segment names still match behaviour.", "Share the definitions so product, sales and marketing use the same ones."],
        ],
        "metrics": ["Revenue index of the best segment|top_share / top_users|{:.1f}", "Retention gap between best and weakest (points)|(top_retention - low_retention) * 100|{:.0f}"],
    },
    "09-growth-product-analytics/17-pricing-page-reviewer": {
        "fields": ["plans|Plans shown|number|3", "visitors|Monthly visitors to the page|number|30000", "cta_rate|Click-through to signup or contact (0 to 1)|number|0.07", "annual_share|Customers on annual plans (0 to 1)|number|0.12", "annual_discount|Annual discount (0 to 1)|number|0.2"],
        "sections": [
            ["Page", "Copy: {input}", "{plans} plans, {visitors} monthly visitors, {cta_rate} click through.", "A pricing page answers four questions: what does it cost, what do I get, which plan is mine and is it safe to try."],
            ["Clarity", "State what is included and the limits in plain view, not in tooltips. Name plans by who they are for, highlight one recommended plan and keep feature rows to those that differ between plans.", "Show the price metric clearly (per seat, per usage)."],
            ["Conversion elements", "One clear call to action per plan, a free trial or demo path, an annual toggle with the saving ({annual_discount} here) and a comparison for people who read in detail.", "Annual share today is {annual_share}. A visible toggle usually raises it."],
            ["Objections", "Add an FAQ on cancelling, refunds, security, data export and support. Add logos, a short testimonial and a link to talk to sales for large teams.", "Use the questions sales and support hear most."],
            ["Test", "Test one change at a time, such as plan names, the recommended plan or the toggle default. Measure paid conversion and revenue per visitor, not clicks only.", "Segment by traffic source, since intent differs."],
        ],
        "metrics": ["Clicks per month|visitors * cta_rate|{:,.0f}", "Customers on annual plans per 100|annual_share * 100|{:.0f}"],
    },
    "09-growth-product-analytics/18-pipeline-forecaster": {
        "fields": ["proposal_deals|Deals in proposal|number|24", "negotiation_deals|Deals in negotiation|number|9", "proposal_win|Historical win rate from proposal (0 to 1)|number|0.28", "negotiation_win|Historical win rate from negotiation (0 to 1)|number|0.62", "avg_deal|Average deal size (USD)|number|38000"],
        "sections": [
            ["Pipeline", "Snapshot: {input}", "{proposal_deals} deals in proposal and {negotiation_deals} in negotiation, average {avg_deal} USD.", "A forecast is a probability-weighted view of the pipeline, with a range and not a single promise."],
            ["Stage-weighted view", "Multiply deals in each stage by the historical win rate from that stage and by the average value. Use your own history: stage rates from another company mislead.", "Update win rates from the last four quarters."],
            ["Risk adjustments", "Lower the odds for old deals (past the normal cycle), deals with no executive contact, heavy discounts or a named competitor. Raise them only with evidence.", "Treat deals that slipped twice as new opportunities."],
            ["Range", "Report a low case (negotiation deals only), a likely case (stage-weighted) and a high case (add upside deals). Share what has to be true for each.", "Compare each forecast with the actual result to learn your bias."],
            ["Actions", "Focus on the largest deals with the largest gap between value and probability, and on creating more pipeline if even the high case misses the target.", "Review the forecast weekly with the same method."],
        ],
        "metrics": ["Expected bookings from proposal (USD)|proposal_deals * proposal_win * avg_deal|${:,.0f}", "Expected bookings from negotiation (USD)|negotiation_deals * negotiation_win * avg_deal|${:,.0f}", "Total stage-weighted forecast (USD)|(proposal_deals * proposal_win + negotiation_deals * negotiation_win) * avg_deal|${:,.0f}"],
    },
    "09-growth-product-analytics/19-event-taxonomy-auditor": {
        "fields": ["events|Event names in use|number|340", "unused|Events with no data in 90 days|number|60", "duplicates|Events that duplicate another|number|28", "no_owner|Events without an owner|number|110", "minutes_each|Minutes to fix one event name end to end|number|45"],
        "sections": [
            ["Inventory", "Events: {input}", "{events} events: {unused} unused, {duplicates} duplicates, {no_owner} without an owner.", "Messy event names make every analysis slower and less trusted. A tracking plan is the cure."],
            ["Naming rules", "Use one convention (object_action in snake_case, past tense: plan_upgraded). Do not put values in names, and keep the same name across web, mobile and server.", "Rename through a mapping so history stays joinable."],
            ["Properties", "Define standard properties for every event (user id, account id, plan, platform, timestamp) and specific properties per event with types and allowed values.", "Avoid free-text properties and ids in event names."],
            ["Clean up", "Retire the {unused} unused events, merge the {duplicates} duplicates and give an owner to each of the {no_owner} unowned ones.", "Check dashboards that use an event before removing it."],
            ["Governance", "Keep the tracking plan in version control, validate events against it in CI and review new events in a short weekly meeting. Alert on events that stop arriving.", "Document what each event means and when it fires."],
        ],
        "metrics": ["Share of events that need action|(unused + duplicates) / events|{:.0%}", "Hours to fix the duplicates|duplicates * minutes_each / 60|{:.1f}", "Unowned share|no_owner / events|{:.0%}"],
    },
    "09-growth-product-analytics/20-win-loss-analyst": {
        "fields": ["deals|Deals reviewed|number|30", "lost|Deals lost|number|14", "price_losses|Losses mainly about price|number|6", "feature_losses|Losses mainly about a missing feature|number|5", "process_losses|Losses mainly about process or speed|number|3"],
        "sections": [
            ["Sample", "Notes: {input}", "{lost} of {deals} deals lost: {price_losses} on price, {feature_losses} on a missing feature, {process_losses} on process.", "Win-loss tells you why buyers choose, from the buyer. Ask the buyer, not the salesperson, whenever possible."],
            ["Method", "Interview the decision maker and one user within 30 days of the decision, with someone outside sales. Ask open questions about the process, the alternatives, the deciding factor and what almost changed the result.", "Interview wins as well as losses, since wins show what to repeat."],
            ["Coding the reasons", "Tag each deal with a primary reason and up to two secondary ones. Separate stated reasons (price) from real ones (value not shown). Count themes and keep quotes.", "Check price losses for hidden causes: unclear value, wrong buyer or wrong plan."],
            ["Competitors", "Track which competitor appears, in which segment, and how often you win against each. Update battlecards with the buyers' words.", "Look for patterns by deal size, industry and source."],
            ["Actions", "Send missing-feature themes to product with deal counts and value, process themes to sales operations and price themes to pricing. Report what changed each quarter.", "Close the loop by showing the sales team which fixes came from their deals."],
        ],
        "metrics": ["Loss rate|lost / deals|{:.0%}", "Share of losses about price|price_losses / lost|{:.0%}", "Share of losses about a missing feature|feature_losses / lost|{:.0%}"],
    },
}
