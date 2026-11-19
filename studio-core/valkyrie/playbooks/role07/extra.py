"""Playbooks for the Technical Support agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "07-technical-support/11-refund-policy-checker": {
        "fields": ["plan_price|Amount paid (USD)|number|1200", "days_since|Days since purchase|number|41", "window_days|Refund window in the policy (days)|number|30", "usage_share|Share of the licence used (0 to 1)|number|0.05", "exception|Exception to consider|text|Documented product defect that blocked setup"],
        "sections": [
            ["Request", "Request: {input}", "Paid {plan_price} USD, {days_since} days ago. Policy window: {window_days} days. Exception: {exception}.", "A refund policy exists to be fair and predictable. Apply it the same way to everyone, and record the reason when you make an exception."],
            ["Policy check", "Within the window the customer is entitled to a refund. Outside it, refunds are discretionary. Check the window, the plan type and any contract terms first.", "Look for double charges and unauthorised charges: these are refunded regardless of the window."],
            ["Usage and cause", "Low usage and a documented defect that blocked setup support an exception. Heavy use over many weeks does not. Check the product logs and the support history before deciding.", "If the product failed, offer a fix or credit as well as a refund."],
            ["Options", "Full refund, partial refund for the unused period, credit or extension with a fix. State the amount, how long it takes to arrive and what happens to access.", "Prorate monthly. For annual plans, refund the unused full months."],
            ["Record and approval", "Record the decision, the reason and who approved it. Refunds over your approval limit go to a manager.", "Track refund rate and reasons monthly. A rising reason is a product signal."],
        ],
        "metrics": ["Days past the window|days_since - window_days|{:+.0f}", "Prorated refund for the unused part of a year (USD)|plan_price * (365 - days_since) / 365|${:,.0f}", "Value of licence not used (USD)|plan_price * (1 - usage_share)|${:,.0f}"],
    },
    "07-technical-support/12-support-reply-drafter": {
        "fields": ["customer|Customer name|text|Priya", "hours_waiting|Hours the customer has waited|number|6", "sla_hours|First-reply target (hours)|number|4", "cause|What you know about the cause|text|Our delivery service retried and paused after repeated timeouts", "next_update|When the next update is due|text|Within 2 hours"],
        "sections": [
            ["Ticket", "Thread: {input}", "Customer: {customer}. Waiting {hours_waiting} hours against a target of {sla_hours}.", "Write the reply the customer wants to receive: acknowledgement, what you know, what happens next and when."],
            ["Opening", "Greet by name, acknowledge the impact in one sentence and apologise once, specifically, for the delay and the disruption. Avoid stock phrases such as 'we value your business'.", "Do not blame the customer or promise what you cannot guarantee."],
            ["What we know", "Cause so far: {cause}. Say what is confirmed, what is still being checked and what you need from the customer, such as an endpoint URL or a timestamp.", "If you do not know, say so and say when you will."],
            ["What happens next", "Name the owner, the next step and the time: next update {next_update}. Offer a workaround to unblock them now if there is one.", "Link to the status page if the problem affects others."],
            ["Close the loop", "End with one clear request or confirmation, and follow up after the fix to check the problem is gone.", "Add a note to the ticket for the next agent: what was promised and when."],
        ],
        "metrics": ["Hours past the reply target|hours_waiting - sla_hours|{:+.1f}"],
    },
    "07-technical-support/13-duplicate-ticket-merger": {
        "fields": ["tickets|Tickets in the cluster|number|9", "companies|Companies affected|number|6", "minutes_each|Minutes agents spend per duplicate ticket|number|12", "root_ticket|Ticket to keep as the parent|text|SUP-4821", "engineering_link|Engineering issue|text|ENG-1177"],
        "sections": [
            ["Cluster", "Tickets: {input}", "{tickets} tickets from {companies} companies. Parent: {root_ticket}. Engineering issue: {engineering_link}.", "Merge when tickets describe the same problem. Link, but do not merge, when the cause is unclear or the customers need separate answers."],
            ["Match signals", "Same error code or message, same version or platform, same time window, same feature and similar reproduction steps. Compare all of these, not just the title.", "Search the title and body of recent tickets before opening a new one."],
            ["Merge carefully", "Keep the oldest or the best-documented ticket as the parent. Copy details and attachments into it, keep each customer's own history and tell each customer what you did.", "Never merge tickets from different customers into one public thread."],
            ["One owner", "Attach all tickets to {engineering_link}. Give one person the job of updating customers, so every customer gets the same facts.", "Add a macro that explains the known issue and how to get updates."],
            ["Prevention", "Show similar tickets while agents write a reply, publish known issues in the help centre and close the loop on every linked ticket when the fix ships.", "Track duplicates per week as a signal that a fix or article is missing."],
        ],
        "metrics": ["Duplicate tickets to merge|tickets - 1|{:,.0f}", "Agent hours saved by one shared answer|(tickets - 1) * minutes_each / 60|{:.1f}"],
    },
    "07-technical-support/14-outage-comms-writer": {
        "fields": ["service|Affected service|text|Payments API", "started|Start time (UTC)|text|14:05", "affected_share|Share of requests failing (0 to 1)|number|0.22", "status|Current status|text|Investigating", "update_minutes|Minutes until the next update|number|30", "outage_hours|Hours the outage may last|number|4"],
        "sections": [
            ["Facts", "Facts: {input}", "Service: {service}. Started {started} UTC. Status: {status}.", "In an outage, customers need to know three things: are you aware, what does it affect and when will you tell me more."],
            ["First update", "Post within 15 minutes: what is affected, who is affected ({affected_share} of requests are failing), the start time and that you are investigating. Do not guess at the cause.", "Use plain words and avoid internal names."],
            ["Follow-up updates", "Post every {update_minutes} minutes even if there is nothing new, and say so. A missed update is read as a loss of control.", "Use the same four headings each time: status, impact, what we are doing, next update."],
            ["Workaround and support", "Offer any safe workaround, such as retrying with backoff or paying another way. Tell customers how to get help and whether to open a ticket.", "Pin the status page link in support replies."],
            ["Resolution and review", "Announce the fix, confirm the end time and promise a written review within a set number of days. Include what you will change, not only what happened.", "Credits or service-level remedies are announced after the facts are confirmed."],
        ],
        "metrics": ["Failing requests per 1,000|affected_share * 1000|{:,.0f}", "Updates you will post over the outage|outage_hours * 60 / update_minutes|{:.0f}"],
    },
    "07-technical-support/15-macro-curator": {
        "fields": ["macros|Macros in the library|number|312", "top_macros|Macros that cover most use|number|40", "unused|Macros unused for a year|number|120", "review_minutes|Minutes to review one macro|number|15", "csat_gap|CSAT points lost when the weakest macro is used|number|3"],
        "sections": [
            ["Library", "Usage: {input}", "{macros} macros, {top_macros} cover most use, {unused} unused for a year.", "Macros save time but can feel robotic. The goal is fast, accurate, human replies, not the most macros."],
            ["Retire", "Archive the {unused} macros unused for a year after a check that no process depends on them. Merge near-duplicates into one.", "Keep a list of what was archived, in case a topic returns."],
            ["Fix the weak ones", "Macros linked to lower CSAT or more reopens are unclear, outdated or cold. The weakest costs {csat_gap} CSAT points when used. Rewrite or retire those first.", "Test each rewrite with a small group and compare reopen rate."],
            ["Write well", "Short, personal, one next step, no jargon. Use placeholders for the name and details and leave room for a personal line.", "Agents should edit before sending, never send a macro unread."],
            ["Ownership", "Give each macro an owner and a review date. Review the {top_macros} most-used macros every quarter and the rest yearly.", "Add a macro for each new product release before it ships."],
        ],
        "metrics": ["Review hours for the heavily used macros|top_macros * review_minutes / 60|{:.1f}", "Macros left after retiring the unused|macros - unused|{:,.0f}", "Share of the library that is unused|unused / macros|{:.0%}"],
    },
    "07-technical-support/16-csat-feedback-analyst": {
        "fields": ["responses|Survey responses|number|620", "tickets|Tickets closed in the period|number|5400", "positive|Responses scoring 4 or 5|number|508", "negative|Responses scoring 1 or 2|number|62", "top_theme|Most common negative theme|text|Slow first reply"],
        "sections": [
            ["Survey readout", "Comments: {input}", "{responses} responses from {tickets} closed tickets. Top negative theme: {top_theme}.", "CSAT is the share of satisfied customers. Report it with the response rate, because a small unrepresentative sample misleads."],
            ["Score", "CSAT is satisfied responses (4 or 5) divided by all responses. Compare it by channel, product area, plan and wait time, not only overall.", "Look at changes over weeks, since single weeks are noisy."],
            ["Themes", "Read a sample of low-score comments and tag the cause: speed, accuracy, tone, product problem or policy. The most common cause is {top_theme}.", "Separate the product's fault from the support team's, and send each to the right owner."],
            ["Drivers", "Check correlation with first response time, number of replies, reopen and handoffs. Customers rate the wait and the effort more than the agent.", "Follow up on every score of 1 or 2 within a day."],
            ["Coaching and action", "Use comments as coaching material, never as a punishment. Share praise and fix one process issue per month.", "Report the response rate and how many low scores were followed up."],
        ],
        "metrics": ["CSAT (share satisfied)|positive / responses|{:.0%}", "Dissatisfied share|negative / responses|{:.1%}", "Survey response rate|responses / tickets|{:.1%}"],
    },
    "07-technical-support/17-known-issue-matcher": {
        "fields": ["issue_id|Matching known issue|text|KI-209: PDF export stalls on large reports", "match_score|Match confidence (0 to 1)|number|0.82", "affected|Customers reporting it|number|34", "workaround|Workaround|text|Export to CSV or split the report into smaller date ranges", "fix_eta|Expected fix|text|Release 3.3 in two weeks"],
        "sections": [
            ["Report", "Report: {input}", "Best match: {issue_id}, confidence {match_score}. {affected} customers affected.", "A known issue list lets you answer in minutes, link the ticket and stop engineering from re-investigating."],
            ["Confirm the match", "Compare symptoms, conditions (browser, size, version) and timing with the issue. Confidence above 0.8 is a likely match. Ask one question to rule out a lookalike.", "If it does not fit, open a new report with the details you gathered."],
            ["Tell the customer", "Explain that this is a known problem, give the workaround ({workaround}) and the expected fix: {fix_eta}. Be honest about dates that can slip.", "Offer to notify them when the fix ships."],
            ["Link and count", "Link the ticket to the known issue so the count of affected customers is accurate. The count helps engineering rank the fix.", "Escalate if a major customer is affected or the count jumps."],
            ["Close", "When the fix ships, tell every linked customer, ask them to confirm and archive the issue after a quiet period.", "Update the help centre article."],
        ],
        "metrics": ["Customers to notify when fixed|affected|{:,.0f}", "Chance this is a different issue|1 - match_score|{:.0%}"],
    },
    "07-technical-support/18-enterprise-response-planner": {
        "fields": ["arr|Annual contract value (USD)|number|480000", "renewal_days|Days to renewal|number|60", "open_tickets|Open severity-2 tickets|number|3", "csm|Account owner|text|Dana, customer success manager", "credit_pct|Credit you may offer (0 to 1)|number|0.05"],
        "sections": [
            ["Account", "Situation: {input}", "ARR {arr} USD, renewal in {renewal_days} days, {open_tickets} open severity-2 tickets. Owner: {csm}.", "For a strategic account, the relationship decides the renewal. Move quickly and make one person accountable."],
            ["First 24 hours", "Acknowledge to the executive sponsor, assign an incident lead, and give a time for the next call. Brief your own executive before the customer does.", "Show a single timeline of every issue so the customer does not repeat the story."],
            ["Recovery plan", "Write a short plan per ticket: cause, fix, date and owner. Hold a weekly call until the tickets close and share a written status after each call.", "Bring engineering to the call, not only support."],
            ["Commercial options", "A service credit of up to {credit_pct} of the annual value is available, subject to approval. Offer it with the plan, never instead of the plan.", "Decide beforehand what you will not offer, such as price cuts that break precedent."],
            ["Renewal", "Review health with the sponsor 30 days before renewal, share the improvements made and agree success measures for the next year.", "Log lessons and fix the process gap that caused the repeat issues."],
        ],
        "metrics": ["Maximum credit (USD)|arr * credit_pct|${:,.0f}", "Revenue at risk per day to renewal (USD)|arr / renewal_days|${:,.0f}"],
    },
    "07-technical-support/19-support-capacity-planner": {
        "fields": ["tickets_week|Tickets per week|number|2400", "aht_min|Average handling time (minutes)|number|14", "shrinkage|Shrinkage: time not on tickets (0 to 1)|number|0.3", "hours_week|Paid hours per agent per week|number|38", "growth_month|Monthly volume growth (0 to 1)|number|0.06"],
        "sections": [
            ["Demand", "Volume: {input}", "{tickets_week} tickets a week at {aht_min} minutes each. Growth {growth_month} per month.", "Staffing is workload divided by productive time, plus room for peaks. Plan for the busiest hours, not the weekly average."],
            ["Workload", "Workload hours = tickets x handling time. Add 15 percent for peaks and make sure the schedule matches the hours when tickets arrive.", "Separate channels: chat needs agents ready right now, email can wait."],
            ["Productive time", "Each agent loses {shrinkage} of paid time to breaks, meetings, training and leave. Count only the remainder as capacity.", "Target occupancy of 75 to 85 percent. Above that, quality and morale fall."],
            ["Growth and deflection", "Volume grows {growth_month} a month. Reduce it with better docs, in-product help and fixes for the top contact reasons before hiring.", "Hire ahead of need by the time it takes to train a person, usually 6 to 8 weeks."],
            ["Review", "Compare forecast and actual weekly, track backlog and first-response time and adjust the plan monthly.", "Cross-train agents so they can cover peaks in other queues."],
        ],
        "metrics": ["Workload hours per week|tickets_week * aht_min / 60|{:,.0f}", "Productive hours per agent|hours_week * (1 - shrinkage)|{:.1f}", "Agents needed before peaks|tickets_week * aht_min / 60 / (hours_week * (1 - shrinkage))|{:.1f}"],
    },
    "07-technical-support/20-bug-report-qualifier": {
        "fields": ["summary|One-line summary|text|Invoice PDF applies the wrong tax rate for Canadian customers", "accounts|Accounts affected|number|2", "reproduced|Reproduced in a test account (yes or no)|text|Yes, on staging", "workaround|Workaround|text|Issue a manual credit note", "impact_usd|Estimated money impact (USD)|number|3400"],
        "sections": [
            ["Report", "Report: {input}", "{summary}. {accounts} accounts affected. Reproduced: {reproduced}.", "A good engineering handoff lets someone reproduce the bug without asking the customer again."],
            ["Reproduction", "Record the exact steps, the expected result, the actual result, the account, the time and the environment. Reproduced: {reproduced}. If not reproduced, list what you tried.", "Attach logs, request ids and screenshots, and strip personal data."],
            ["Scope and severity", "Money, data loss and security issues are severity 1 or 2. Estimated impact is {impact_usd} USD for the accounts found so far. Check how many more accounts might be affected by the same condition.", "Rate by impact and by whether a workaround exists."],
            ["Workaround and customer", "Workaround: {workaround}. Tell the customer what you found, what you are doing and when they will hear next. Do not promise a fix date that engineering has not agreed.", "Link the ticket to the engineering issue."],
            ["Handoff", "Write a title that states the symptom, not the guess at the cause. Include severity, scope, steps, evidence and the support owner, then ask engineering to confirm priority within one day for severity 1 and 2.", "Close the loop with the customer when the fix ships."],
        ],
        "metrics": ["Money impact per affected account (USD)|impact_usd / accounts|${:,.0f}"],
    },
}
