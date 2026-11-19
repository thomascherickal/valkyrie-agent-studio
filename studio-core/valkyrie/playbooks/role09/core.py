"""Playbooks for the Growth and Product Analytics agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "09-growth-product-analytics/01-funnel-dropoff-analyst": {
        "fields": ["step1|Step 1 users (visited)|number|1000", "step2|Step 2 users (installed)|number|420", "step3|Step 3 users (first run)|number|190", "step4|Step 4 users (deployed)|number|95", "value_per_conversion|Value of one final conversion (USD)|number|40"],
        "sections": [
            ["Funnel counts", "Funnel: {input}", "Counts: {step1}, {step2}, {step3}, {step4}.", "Count unique users per step in the same time window and cohort; mixing sessions and users hides drop-off."],
            ["Reading the rates", "Compute step conversion (step n+1 / step n) and cumulative conversion. The biggest lever is the step with the largest absolute loss in users, weighted by how fixable it is.", "A step with a low rate but few users matters less than a moderate rate at the top of the funnel."],
            ["Diagnose the worst step", "Segment by channel, device, plan and country; compare time-to-step distributions; watch session recordings; read support tickets for the step. Install-to-first-run drops are usually setup errors or unclear next actions.", "Check instrumentation first: a missing event looks exactly like a drop-off."],
            ["Levers", "Remove fields, auto-detect defaults, add a progress indicator, send a reminder within 1 hour, offer a sample project, and put the next action on screen.", "Each lever becomes an experiment with a stated minimum detectable effect."],
            ["Impact estimate", "A 10 percent relative lift on any single step lifts final conversions by the same 10 percent, since steps multiply.", "Prioritise by users lost times ease of fix times value per conversion ({value_per_conversion} USD)."],
        ],
        "metrics": ["Step 1 to 2|step2 / step1|{:.1%}", "Step 2 to 3|step3 / step2|{:.1%}", "Step 3 to 4|step4 / step3|{:.1%}", "Overall conversion|step4 / step1|{:.1%}", "Value of a 10% relative lift at any step|step4 * 0.1 * value_per_conversion|${:,.0f}"],
    },
    "09-growth-product-analytics/02-cohort-retention-modeler": {
        "fields": ["cohort_size|Cohort size (users)|number|3000", "d1|Day 1 retention (percent)|number|62", "d7|Day 7 retention (percent)|number|38", "d30|Day 30 retention (percent)|number|29", "benchmark_d30|Benchmark day 30 retention (percent)|number|25"],
        "sections": [
            ["Cohort", "Data: {input}", "Cohort of {cohort_size} users: D1 {d1}, D7 {d7}, D30 {d30} percent."],
            ["Curve shape", "A healthy curve falls steeply then flattens. If the curve still declines linearly at D30 there is no retained core yet. A flat tail above zero means a habit has formed; the height of the flat tail is the number to improve.", "Compare D7 to D30: a small drop means the users who survive week one stay."],
            ["Definitions", "Use an explicit definition: day N retention is the share active on day N exactly (classic) or on or after day N (rolling). Keep it the same across cohorts, and define 'active' as a core value action, not a login.", "Exclude cohorts that are too young to have reached D30."],
            ["Segmenting", "Compare cohorts by signup channel, plan, first-use feature and company size. Differences between channels often exceed differences over time.", "Benchmark: {benchmark_d30} percent D30 is a reasonable target for developer tools."],
            ["Actions", "Raise D1 by fixing time-to-value; raise D7 with lifecycle email, in-product checklists and a second use case; raise D30 by building habit loops (scheduled runs, integrations, team invites).", "Re-run after each change on new cohorts only."],
        ],
        "metrics": ["Users still active at D30|cohort_size * d30 / 100|{:,.0f}", "Share of D7 users retained to D30|d30 / d7|{:.0%}", "Gap to benchmark (points)|d30 - benchmark_d30|{:+.1f}"],
    },
    "09-growth-product-analytics/03-ab-test-interpreter": {
        "fields": ["n_control|Control users|number|5000", "n_variant|Variant users|number|5020", "rate_control|Control conversion (percent)|number|12.1", "rate_variant|Variant conversion (percent)|number|14.4", "p_value|Reported p-value|number|0.008"],
        "sections": [
            ["Results", "Reported: {input}", "Control {rate_control} percent (n={n_control}); variant {rate_variant} percent (n={n_variant}); p={p_value}."],
            ["Sample ratio mismatch", "Check that the split matches the design before reading results. Chi-square for a 50/50 split = (n_a - n_b) squared / (n_a + n_b). A value above 10.8 (p below 0.001, 1 degree of freedom) means assignment is broken and the result is untrustworthy.", "Typical causes: bots, redirects that drop users, logging loss in one arm."],
            ["Significance", "A p-value below 0.05 is the usual bar when the test was pre-registered. Report the confidence interval of the difference, not only p. Do not stop at the first significant peek; use the planned sample size or a sequential method.", "Multiple variants or metrics need a correction (Bonferroni or Holm)."],
            ["Practical significance", "Compare the absolute lift to the MDE you planned and to the cost of shipping and maintaining. A statistically significant lift of 0.1 points may not be worth it.", "Check guardrail metrics (errors, latency, support tickets) and segment results for harm."],
            ["Verdict rules", "Ship: SRM clean, primary metric significant with lift at or above the MDE, guardrails flat. Iterate: positive but under-powered. Stop: flat or harmful. Run a holdback for a long-term check.", "Document the decision and the learnings."],
        ],
        "metrics": ["Absolute lift (points)|rate_variant - rate_control|{:+.1f}", "Relative lift|(rate_variant - rate_control) / rate_control|{:+.1%}", "SRM chi-square (50/50 split)|(n_control - n_variant) * (n_control - n_variant) / (n_control + n_variant)|{:.2f}"],
    },
    "09-growth-product-analytics/04-activation-metric-finder": {
        "fields": ["action|Candidate activation action|text|3 or more sandbox tests within 48 hours", "users_total|Users analysed|number|2000", "users_with|Users who did the action|number|400", "ret_with|90-day retention with the action (percent)|number|58", "ret_without|90-day retention without it (percent)|number|19"],
        "sections": [
            ["Candidate", "Behaviour data: {input}", "Action: {action}. {users_with} of {users_total} users did it."],
            ["Method", "List early events (first 7 days), compute each event's correlation with 90-day retention, then test thresholds (1, 3, 5 times; within 24, 48, 72 hours). Choose the threshold with the highest lift while still reached by 20 to 40 percent of users.", "Use logistic regression or a decision tree to find combinations, but keep the final metric simple enough to say in one sentence."],
            ["Beware correlation", "Motivated users do everything. Validate causality with an experiment that nudges new users toward the action and measures retention in the nudged group.", "Check that the action is reachable within the first session or two, not a late milestone."],
            ["Compute lift", "Retention with the action {ret_with} percent versus {ret_without} percent without it.", "Prefer an action that is early, frequent, specific and measurable; 'aha moment' candidates: first successful run, first teammate invited, first integration connected."],
            ["Use it", "Make the activation metric the north star for onboarding: put it in the setup checklist, trigger emails when users stall before it, and track the share of signups that activate within the window.", "Re-check the metric every two quarters."],
        ],
        "metrics": ["Retention lift (x)|ret_with / ret_without|{:.1f}x", "Share of users reaching the action|users_with / users_total|{:.0%}", "Extra retained users if all others matched|(users_total - users_with) * (ret_with - ret_without) / 100|{:,.0f}"],
    },
    "09-growth-product-analytics/05-pricing-elasticity-analyst": {
        "fields": ["free_users|Active free users|number|10000", "conv_before|Current free-to-paid conversion (percent)|number|4", "conv_after|Expected conversion after the change (percent)|number|5.5", "free_loss|Free users lost because of the paywall (percent)|number|8", "price|Price (USD per month)|number|29"],
        "sections": [
            ["Change", "Paywall change: {input}", "{free_users} free users; conversion {conv_before} to {conv_after} percent; {free_loss} percent leave; price {price} USD."],
            ["Model", "Paying users after = free users x (1 - loss) x new conversion. Revenue change = (paying after - paying before) x price. Include second-order effects: fewer free users means fewer referrals and a smaller future funnel.", "Run low, base and high cases for conversion and loss; the decision should hold in the base case."],
            ["Elasticity", "Elasticity = percent change in conversion / percent change in price (or access). Absolute values above 1 mean revenue falls when you tighten; below 1 means it rises.", "Estimate from past price tests or a survey (Van Westendorp), not from competitor prices."],
            ["Test before shipping", "Roll out as an A/B test to new signups first, with a pre-registered primary metric (revenue per signup at 60 days) and guardrails (activation, support tickets, NPS).", "Grandfather existing users for one cycle; sudden removals drive complaints and churn."],
            ["Decision rule", "Ship if revenue per signup rises at least 5 percent without a drop in activation or retention beyond the guardrail. Otherwise keep the feature free and monetise team features instead.", "Revisit after 90 days."],
        ],
        "metrics": ["Paying users now|free_users * conv_before / 100|{:,.0f}", "Paying users after|free_users * (1 - free_loss / 100) * conv_after / 100|{:,.0f}", "Monthly revenue change|(free_users * (1 - free_loss / 100) * conv_after / 100 - free_users * conv_before / 100) * price|${:,.0f}"],
    },
    "09-growth-product-analytics/06-attribution-mapper": {
        "fields": ["ad_spend|Paid search spend (USD)|number|27000", "ad_customers|Customers from paid search|number|150", "oss_customers|Customers from GitHub and open source|number|210", "ltv|Customer lifetime value (USD)|number|900", "avg_touches|Average touches before conversion|number|3"],
        "sections": [
            ["Channel data", "Channels: {input}", "Paid search {ad_spend} USD for {ad_customers} customers; open source brought {oss_customers}."],
            ["Models compared", "First touch credits the channel that found the customer (favours discovery channels such as GitHub). Last touch favours search and email. Linear splits credit equally across touches: with about {avg_touches} touches each gets a fixed share.", "Also try position-based (40/20/40) and run an incrementality test, since models alone cannot prove causation."],
            ["CAC rules", "Fully loaded CAC includes spend, tools, agency fees and the people cost of the programme. Free channels still have a cost; compute it from hours.", "Compare CAC to LTV: above 3x is healthy, 1 to 3x is marginal, under 1x loses money."],
            ["Payback", "Aim for CAC payback under 12 months for self-serve and 18 for sales-led, computed on gross margin.", "Report blended CAC (all spend / all customers) alongside the paid CAC."],
            ["Actions", "Shift budget toward channels with LTV:CAC above 3 and rising returns; cap channels whose marginal CAC rises steeply; invest in open source and content, which compound.", "Review quarterly, never mid-campaign."],
        ],
        "metrics": ["Paid search CAC|ad_spend / ad_customers|${:,.0f}", "LTV to CAC ratio (paid)|ltv / (ad_spend / ad_customers)|{:.1f}x", "Blended CAC|ad_spend / (ad_customers + oss_customers)|${:,.0f}", "Linear credit per touch|1 / avg_touches|{:.0%}"],
    },
    "09-growth-product-analytics/07-seo-content-strategist": {
        "fields": ["volume|Monthly search volume of the target keyword|number|1900", "difficulty|Keyword difficulty (0 to 100)|number|22", "ctr|Expected click-through rate at target position (percent)|number|10", "signup_rate|Visit-to-signup rate (percent)|number|3", "signup_value|Value of a signup (USD)|number|60"],
        "sections": [
            ["Topic cluster", "Topics: {input}", "Lead keyword: {volume} searches per month, difficulty {difficulty}."],
            ["Scoring gaps", "Score each keyword: intent (build, compare, fix) x volume x winnability. Winnable means low difficulty, weak incumbents (forums, old posts) and your product being the natural answer. Prefer difficulty under 30 for a young domain.", "Read the top 10 results: if all are docs from large vendors, change the angle (benchmarks, tutorials, comparisons)."],
            ["Content roadmap", "Create a pillar page for the head topic and 5 to 8 supporting posts that answer specific questions and link back. Order by value per effort: bottom-of-funnel comparison and how-to pages first.", "Write for the developer: working code, version numbers, and a runnable repository."],
            ["On-page checklist", "Primary keyword in title, H1 and the first 100 words; descriptive URL; schema markup (HowTo, FAQ); internal links; fast page; an original diagram or benchmark that others will cite.", "Update posts every 6 months with the current versions."],
            ["Measurement", "Track impressions, position, clicks and signups per page. Judge after 90 days, since new pages take months to rank.", "Prune or merge pages that never reach the top 20."],
        ],
        "metrics": ["Expected monthly clicks|volume * ctr / 100|{:,.0f}", "Expected monthly signups|volume * ctr / 100 * signup_rate / 100|{:,.1f}", "Expected monthly value|volume * ctr / 100 * signup_rate / 100 * signup_value|${:,.0f}"],
    },
    "09-growth-product-analytics/08-churn-cohort-explainer": {
        "fields": ["churned|Churned accounts in the period|number|50", "avg_arr|Average ARR per churned account (USD)|number|4800", "churn_never|Churned accounts that never deployed (percent)|number|72", "retained_never|Retained accounts that never deployed (percent)|number|35", "save_rate|Realistic save rate for an intervention (percent)|number|20"],
        "sections": [
            ["Churned accounts", "Facts: {input}", "{churned} accounts churned, {churn_never} percent never deployed versus {retained_never} percent of retained accounts."],
            ["Driver analysis", "Compare churned and retained accounts on feature usage, seat contraction before churn, support tickets, latency or error spikes and champion departures. A driver matters when the gap is large and the segment is big.", "Seat contraction typically precedes cancellation by 30 to 60 days; use it as a leading signal."],
            ["Beware confounding", "Never deployed may reflect poor fit rather than the cause of churn. Validate with an intervention test on a randomly chosen half of new accounts.", "Segment by plan and company size before drawing conclusions."],
            ["Retention actions", "Trigger a guided first-deploy flow on day 2, assign a success engineer to accounts stalled for 10 days, alert on seat contraction above 20 percent, and review latency complaints before renewal.", "Measure each action by deploy rate and 90-day retention."],
            ["Sizing", "Estimate revenue recoverable as churned accounts affected by the driver x average ARR x realistic save rate.", "Report the range, not a single number."],
        ],
        "metrics": ["Churned ARR|churned * avg_arr|${:,.0f}", "Risk ratio (churned versus retained)|churn_never / retained_never|{:.1f}x", "Recoverable ARR|churned * churn_never / 100 * avg_arr * save_rate / 100|${:,.0f}"],
    },
    "09-growth-product-analytics/09-plg-loop-designer": {
        "fields": ["weekly_active|Weekly active users|number|5000", "share_rate|Share of users who share a blueprint (percent)|number|12", "views_per_share|Views per shared link|number|25", "signup_rate|View-to-signup rate (percent)|number|6", "cycle_days|Loop cycle time (days)|number|7"],
        "sections": [
            ["Surface", "Product surface: {input}", "{weekly_active} weekly users; {share_rate} percent share; each link gets {views_per_share} views; {signup_rate} percent sign up."],
            ["Loop design", "Trigger (user finishes an agent) -> action (share link with preview card) -> viewer lands on a working demo -> signs up and clones -> creates and shares. Every step needs under 30 seconds and no signup wall before seeing value.", "Preview cards (Open Graph image) are the ad; make them show the result, not a logo."],
            ["K factor", "K = share rate x views per share x signup rate (invites per user times conversion). K above 1 grows by itself; real products land at 0.1 to 0.4 and use loops to lower acquisition cost.", "Amplification of a paid or organic cohort = 1 / (1 - K) when K is below 1."],
            ["Instrumentation", "Track share clicked, link created, link viewed, signup from link, cloned, activated. Attribute with a ref parameter and measure per-loop cycle time.", "Guard against abuse: rate limit link creation, expire private data, strip secrets from shared blueprints."],
            ["Experiments", "Test the default share prompt, preview image, one-click clone and a reward (credits) after a friend activates. Optimise the weakest step first.", "Judge success by activated users from the loop, not by signups."],
        ],
        "metrics": ["Viral coefficient K|share_rate / 100 * views_per_share * signup_rate / 100|{:.2f}", "New signups per cycle|weekly_active * share_rate / 100 * views_per_share * signup_rate / 100|{:,.0f}", "Amplification 1 / (1 - K)|1 / (1 - share_rate / 100 * views_per_share * signup_rate / 100)|{:.2f}x"],
    },
    "09-growth-product-analytics/10-exec-kpi-narrator": {
        "fields": ["wau|Weekly active users now|number|12000", "wau_growth|WAU growth week over week (percent)|number|14", "free_to_paid|Free-to-paid conversion (percent)|number|4.8", "ttfd|Median time to first deploy (minutes)|number|6", "ttfd_target|Target time to first deploy (minutes)|number|5"],
        "sections": [
            ["Headline", "KPIs: {input}", "Open with the single most important change and its cause: WAU {wau}, growth {wau_growth} percent week over week."],
            ["Narrative structure", "Use: what moved, why, so what, now what. Pair every number with a comparison (last week, target) and one sentence of cause from data, not guesses.", "Distinguish signal from noise: week-over-week moves under 5 percent on small bases are usually noise; look at the 4 week trend."],
            ["Conversion and efficiency", "Free-to-paid {free_to_paid} percent: compare to the quarter average and to a 3 to 5 percent norm for self-serve developer tools.", "Time to first deploy {ttfd} minutes against a {ttfd_target} minute target."],
            ["Risks and asks", "Name one risk with owner and date, and one ask with a decision deadline. Limit to three bullets per section.", "Flag metric definition changes explicitly so the series stays comparable."],
            ["Style", "Under 250 words, plain language, same layout each week, numbers formatted consistently (percent, thousands), no adjectives without data.", "Link the dashboard for details instead of pasting tables."],
        ],
        "metrics": ["WAU last week|wau / (1 + wau_growth / 100)|{:,.0f}", "Net WAU added|wau - wau / (1 + wau_growth / 100)|{:,.0f}", "Time to first deploy versus target|ttfd / ttfd_target|{:.2f}x"],
    },
}
