"""Playbooks for the CXO agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "12-cxos/01-board-deck-synthesizer": {
        "fields": ["arr|Ending ARR (USD)|number|4800000", "qoq_pct|ARR growth quarter over quarter (percent)|number|22", "nrr_pct|Net revenue retention (percent)|number|118", "cash|Cash on hand (USD)|number|7000000", "net_burn|Net burn per month (USD)|number|250000", "milestones|Product milestones this quarter|list|Launched the 120-agent studio, Shipped the Rust export, Closed two enterprise pilots"],
        "sections": [
            ["Quarter at a glance", "Metrics: {input}", "ARR {arr} USD, growth {qoq_pct} percent QoQ, NRR {nrr_pct} percent.", "Slide 1 holds five numbers only: ARR, growth, NRR, net burn and runway, each with its change versus plan."],
            ["Growth and efficiency", "Show ARR bridge: starting ARR + new + expansion - contraction - churn = ending ARR. Burn multiple = net burn / net new ARR; under 1.5 is strong, over 3 is a warning at this stage.", "NRR above 110 percent indicates expansion beats churn; below 100 percent means the base is shrinking."],
            ["Cash and runway", "Cash {cash} USD at {net_burn} USD per month. Runway under 18 months means start fundraising or cut; under 12 is urgent.", "Show base, downside and upside runway cases."],
            ["Product milestones", "*{milestones}", "Tie each milestone to a business outcome (pipeline, retention, cost), and flag misses with the recovery date."],
            ["Board asks", "End with the decisions and help needed (hiring, introductions, approvals) and the next quarter's three priorities.", "Send the deck 3 working days ahead, with a one-page memo."],
        ],
        "metrics": ["Runway (months)|cash / net_burn|{:.1f}", "ARR a quarter ago|arr / (1 + qoq_pct / 100)|${:,.0f}", "Net new ARR in the quarter|arr - arr / (1 + qoq_pct / 100)|${:,.0f}", "Burn multiple|net_burn * 3 / (arr - arr / (1 + qoq_pct / 100))|{:.2f}"],
    },
    "12-cxos/02-ma-diligence-reviewer": {
        "fields": ["price|Proposed purchase price (USD)|number|30000000", "target_arr|Target ARR (USD)|number|4000000", "top_customer_pct|Largest customer share of ARR (percent)|number|28", "gpl_count|Copyleft (GPL or AGPL) dependencies in core|number|1", "open_items|Open diligence items|list|Missing IP assignment from two contractors, SOC 2 report expired, Pending customer MSA renewal"],
        "sections": [
            ["Findings so far", "Documents: {input}", "Open items:", "*{open_items}"],
            ["Customer concentration", "Largest customer is {top_customer_pct} percent of ARR. Above 20 percent is a major risk; above 10 percent needs a contract review (term, termination for convenience, change-of-control clause).", "Interview the top five customers before signing; ask for consents where required."],
            ["IP and open source", "Confirm every contributor signed an IP assignment, scan the code (Black Duck, FOSSA) and review the {gpl_count} copyleft dependency in the core. GPL or AGPL in a distributed or network-served core can force source disclosure: remediate before close or price it.", "Check patent encumbrances and third-party code in the repository history."],
            ["Security and compliance", "Request SOC 2 Type II, the latest penetration test, an incident history and the data processing agreements. Check data residency and subprocessors.", "Unresolved high findings become closing conditions or escrow items."],
            ["Valuation effect", "Adjust the price or structure: holdback or escrow of 10 to 15 percent for 18 months, earn-out tied to retention of the top customer, and specific indemnities for IP.", "Rank risks by exposure in dollars and by whether they are fixable before close."],
        ],
        "metrics": ["Price to ARR multiple|price / target_arr|{:.1f}x", "ARR dependent on the largest customer|target_arr * top_customer_pct / 100|${:,.0f}", "Multiple on ARR excluding the largest customer|price / (target_arr * (1 - top_customer_pct / 100))|{:.1f}x", "Suggested escrow at 12.5 percent|price * 0.125|${:,.0f}"],
    },
    "12-cxos/03-annual-operating-plan": {
        "fields": ["start_arr|Starting ARR (USD)|number|4800000", "end_arr|Ending ARR in the base case (USD)|number|9500000", "hires|Planned hires|number|12", "cost_per_hire|Fully loaded cost per hire (USD per year)|number|180000", "gm_pct|Gross margin (percent)|number|78", "other_opex|Other operating expenses (USD per year)|number|2500000"],
        "sections": [
            ["Plan drivers", "Drivers: {input}", "ARR from {start_arr} to {end_arr} USD; {hires} hires; gross margin {gm_pct} percent."],
            ["Scenarios", "Build three cases: base (the plan), downside (growth 30 percent lower, hiring paused after Q2) and upside. Show ARR, gross margin, headcount, burn and runway for each.", "Tie hiring to triggers (net new ARR milestones) so spend can slow if growth does."],
            ["Hiring and cost", "Fully loaded cost = salary + 20 to 30 percent for taxes and benefits + equipment and tools. Hires start mid-quarter on average and ramp 3 to 6 months; model both cost and productivity.", "Cloud COGS should scale with usage; model it per tenant and per million runs."],
            ["Checks", "Test magic numbers: ARR growth above 100 percent requires proof of pipeline coverage (3x), sales capacity and retention above 110 percent NRR. Payback on CAC under 18 months.", "Reconcile to the cash plan and keep at least 18 months of runway in the downside."],
            ["Governance", "Review monthly against plan, reforecast quarterly, and name an owner for every driver.", "Document assumptions so the board can challenge them."],
        ],
        "metrics": ["ARR growth in the plan|end_arr / start_arr - 1|{:.0%}", "Annual cost of planned hires|hires * cost_per_hire|${:,.0f}", "Gross profit on ending ARR|end_arr * gm_pct / 100|${:,.0f}", "Gross profit less new hires and other opex|end_arr * gm_pct / 100 - hires * cost_per_hire - other_opex|${:,.0f}"],
    },
    "12-cxos/04-crisis-comms-strategist": {
        "fields": ["affected_pct|Share of users affected (percent)|number|12", "customers|Customers affected|number|340", "avg_fee|Average monthly fee per customer (USD)|number|1200", "credit_pct|SLA credit (percent of monthly fee)|number|10", "spokesperson|Designated spokesperson|text|CTO, with the VP Support for customer calls"],
        "sections": [
            ["Situation", "Brief: {input}", "{affected_pct} percent of users and {customers} customers affected. Spokesperson: {spokesperson}."],
            ["First hour", "Agree facts, impact and ownership; one approved holding statement; one source of truth (status page). Do not speculate on cause or blame a vendor in public, even if a third party failed.", "Assign roles: incident lead, comms lead, legal, support, executive sponsor."],
            ["Audience matrix", "Customers: status page, email within 60 minutes, account managers call top accounts. Internal: all-hands channel update every 30 to 60 minutes with the same facts customers see. Press and social: short reactive statement only, no proactive pitching. Regulators: assess notification duty (GDPR 72 hours for personal data breaches).", "A third-party outage still needs your own message: customers hold you accountable."],
            ["Message rules", "Acknowledge, state impact, say what is being done and when the next update is, apologise once, and avoid jargon and absolutes like 'no data was lost' until verified.", "Keep a single timeline of every statement for the post-incident review."],
            ["Recovery", "Resolution notice, root-cause summary within 5 working days, credits per the SLA, and a call to affected top accounts. Review what the comms flow got wrong.", "Credits should be offered proactively, not on request."],
        ],
        "metrics": ["SLA credit exposure|customers * avg_fee * credit_pct / 100|${:,.0f}", "Monthly recurring revenue affected|customers * avg_fee|${:,.0f}"],
    },
    "12-cxos/05-ai-transformation-advisor": {
        "fields": ["tickets_week|Tasks per week in the workflow|number|1200", "minutes_task|Minutes per task today|number|8", "automation_pct|Share of tasks automatable (percent)|number|40", "hourly_cost|Fully loaded hourly cost (USD)|number|55", "build_cost|One-time build and rollout cost (USD)|number|60000"],
        "sections": [
            ["Candidate workflows", "Catalog: {input}", "Reference workflow: {tickets_week} tasks per week at {minutes_task} minutes, {automation_pct} percent automatable."],
            ["Scoring", "Score each workflow 1 to 5 on volume, repeatability, data availability, error cost and compliance risk. Rank by ROI x safety: high volume, clear rules and low blast radius first.", "Tier 1 candidates: L1 support triage, internal search, code review assistance, document summaries."],
            ["Compliance and risk", "Legal contract redlines, hiring decisions and credit decisions involve regulated or high-impact judgements: keep a human in the loop, log decisions and check EU AI Act classification and sector rules before automating.", "Require a data classification review: no customer personal data to external models without a data processing agreement."],
            ["Roadmap", "Wave 1 (0 to 3 months): two assistive pilots with human approval and measured accuracy. Wave 2: expand to the proven workflows. Wave 3: higher-stakes work with controls.", "Define success before the pilot: accuracy above 90 percent, handle time reduced by 30 percent, no rise in escalations."],
            ["Adoption", "Train the staff who own the workflow, measure usage and quality weekly, keep a rollback to the manual process, and report realised savings, not projected ones.", "Budget 30 percent of the build for evaluation and monitoring."],
        ],
        "metrics": ["Hours saved per week|tickets_week * minutes_task * automation_pct / 100 / 60|{:,.0f}", "Annual savings|tickets_week * minutes_task * automation_pct / 100 / 60 * hourly_cost * 52|${:,.0f}", "Payback (months)|build_cost / (tickets_week * minutes_task * automation_pct / 100 / 60 * hourly_cost * 52 / 12)|{:.1f}"],
    },
    "12-cxos/06-investor-update-writer": {
        "fields": ["arr|ARR (USD)|number|4800000", "mom_pct|ARR growth month over month (percent)|number|4", "cash|Cash (USD)|number|7000000", "net_burn|Net burn this month (USD)|number|250000", "wins|Wins|list|Launched the 120-agent studio, Signed two enterprise pilots", "asks|Asks|list|Two introductions to enterprise platform teams, A senior Rust hire"],
        "sections": [
            ["Subject and summary", "Highlights: {input}", "Subject line: '<Company> update: ARR {arr} USD, +{mom_pct} percent MoM'.", "Open with a three-line summary: the metric, the main win, the main ask."],
            ["Metrics", "ARR {arr} USD (+{mom_pct} percent), cash {cash} USD, net burn {net_burn} USD.", "Always give the same table each month: ARR, growth, NRR, burn, runway, headcount, with the previous month beside it."],
            ["Wins", "*{wins}", "State outcomes and numbers, not activity. One line each."],
            ["Challenges", "Include one honest problem and what you are doing about it. Investors trust founders who report bad news early.", "Do not bury misses under adjectives."],
            ["Asks", "*{asks}", "Make each ask specific: who, what and why it matters; investors respond to a named target and a one-line blurb they can forward."],
        ],
        "metrics": ["Runway (months)|cash / net_burn|{:.1f}", "Net new ARR this month|arr - arr / (1 + mom_pct / 100)|${:,.0f}", "Burn multiple|net_burn / (arr - arr / (1 + mom_pct / 100))|{:.1f}", "Simple annualised growth (12 x monthly)|mom_pct * 12|{:.0f}%"],
    },
    "12-cxos/07-enterprise-deal-desk": {
        "fields": ["list_acv|List price per year (USD)|number|250000", "discount_pct|Requested discount (percent)|number|25", "term_years|Term (years)|number|3", "gm_pct|Standard gross margin (percent)|number|78", "sla_cost_pct|Extra cost to deliver the requested SLA (percent of cost)|number|10"],
        "sections": [
            ["Deal terms", "Request: {input}", "List {list_acv} USD per year, discount {discount_pct} percent, {term_years} years, SLA cost uplift {sla_cost_pct} percent."],
            ["Discount guardrails", "Up to 10 percent: sales manager. 10 to 20 percent: VP Sales. Above 20 percent: CRO and CFO approval. Trade discount for value: multi-year commitment, annual prepay, logo or case study rights.", "A multi-year term justifies roughly 3 to 5 percent per year of commitment, not 25 percent for free."],
            ["SLA and risk terms", "99.99 percent allows 4.3 minutes of downtime per month; 99.9 allows 43 minutes. Match the SLA to your demonstrated uptime and architecture, and cap credits at 10 to 30 percent of monthly fees.", "Indemnity and liability: cap at 12 months of fees, exclude consequential damages, carve out only IP and confidentiality."],
            ["Margin test", "Compute margin after discount and SLA cost. Floor: 65 percent gross margin for enterprise. Below the floor requires CFO sign-off and a path to recover (price step-ups of 5 to 7 percent per year).", "Check payment terms: net 30, no extended terms beyond net 60."],
            ["Decision", "Approve, counter or decline. Counter with a smaller discount, a tiered SLA (99.9 now, 99.99 with a dedicated tier at a fee) or a shorter ramp.", "Record the final terms and any non-standard clauses for renewal."],
        ],
        "metrics": ["Net price per year|list_acv * (1 - discount_pct / 100)|${:,.0f}", "Total contract value|list_acv * (1 - discount_pct / 100) * term_years|${:,.0f}", "Gross margin after discount and SLA|(list_acv * (1 - discount_pct / 100) - list_acv * (1 - gm_pct / 100) * (1 + sla_cost_pct / 100)) / (list_acv * (1 - discount_pct / 100))|{:.1%}", "Revenue given up over the term|list_acv * discount_pct / 100 * term_years|${:,.0f}"],
    },
    "12-cxos/08-regulatory-horizon-watch": {
        "fields": ["jurisdictions|Jurisdictions|list|European Union, United Kingdom, United States", "risk_class|Likely classification|text|Limited risk, possibly high risk if used for employment or credit decisions", "days_to_deadline|Days to the next compliance date|number|120", "effort_weeks|Estimated effort to close gaps (weeks)|number|10", "controls|Controls in place|list|Run history with timestamps, Role-based access, Human approval step for deployments"],
        "sections": [
            ["Scope", "Area: {input}", "Jurisdictions:", "*{jurisdictions}", "Classification: {risk_class}"],
            ["EU AI Act", "Risk tiers: unacceptable (banned), high-risk (conformity assessment, risk management, data governance, logging, transparency, human oversight, accuracy and robustness), limited (transparency duties) and minimal. High-risk systems must keep automatically generated logs and allow human oversight.", "Confirm current application dates with counsel; timelines and guidance have been adjusted and vary by obligation."],
            ["GDPR and SOC 2", "GDPR: lawful basis, data minimisation, Article 22 limits on automated decisions, DPIA for high-risk processing, breach notice in 72 hours. SOC 2: map logging and oversight to CC7 and change management to CC8.", "Audit trails must show who approved what, when, and which model version ran."],
            ["Control gaps", "Controls in place:", "*{controls}", "Typical gaps: immutable audit logs, retention policy (keep at least 6 months), human-in-the-loop checkpoints for consequential actions, model and prompt versioning."],
            ["Roadmap mapping", "Map each gap to a roadmap item with an owner, a date before the compliance deadline, and a test or evidence artefact.", "Review the regulatory watch list quarterly with legal."],
        ],
        "metrics": ["Slack before the deadline (weeks)|days_to_deadline / 7 - effort_weeks|{:+.1f}", "Weeks available|days_to_deadline / 7|{:.1f}"],
    },
    "12-cxos/09-org-design-modeler": {
        "fields": ["engineers|Engineers|number|42", "managers|Engineering managers|number|4", "pods|Product (stream-aligned) pods|number|5", "platform_engineers|Engineers on platform teams|number|7", "target_span|Target span of control|number|7"],
        "sections": [
            ["Current structure", "Org: {input}", "{engineers} engineers, {managers} managers, {pods} product pods, {platform_engineers} on platform."],
            ["Span of control", "Healthy span for engineering managers is 5 to 8 direct reports (up to 10 for experienced, senior teams). Over 10 weakens coaching and 1:1s; under 4 creates layers without leverage.", "Compute managers needed at the target span of {target_span}."],
            ["Team Topologies", "Stream-aligned teams own a product flow end to end; the platform team provides self-service capabilities that reduce cognitive load. Enabling teams coach; complicated-subsystem teams hold deep expertise.", "Team size of 5 to 9 per pod; one pod should not own more than one major domain."],
            ["Platform sizing", "Platform headcount is typically 10 to 20 percent of engineering. Treat it as a product with customers and a roadmap; if pods route around it, it is mis-scoped.", "Measure platform by adoption, time to first deploy and developer satisfaction."],
            ["Change plan", "Change one thing at a time, explain the reason, move people with their consent where possible, and re-measure after a quarter (delivery time, attrition, engagement).", "Avoid re-orgs more than once a year."],
        ],
        "metrics": ["Current span of control|engineers / managers|{:.1f}", "Managers needed at the target span|engineers / target_span|{:.1f}", "Additional managers|engineers / target_span - managers|{:+.1f}", "Platform share of engineering|platform_engineers / engineers|{:.0%}", "Engineers per pod|(engineers - platform_engineers) / pods|{:.1f}"],
    },
    "12-cxos/10-ceo-weekly-brief": {
        "fields": ["pipeline|Qualified pipeline (USD)|number|1400000", "target|Remaining bookings target this quarter (USD)|number|500000", "uptime|Uptime this month (percent)|number|99.98", "uptime_target|Uptime target (percent)|number|99.95", "offers|Offers accepted|number|2", "open_roles|Open roles|number|9"],
        "sections": [
            ["Headline", "Inputs: {input}", "Open with the one thing the CEO must know or decide this week."],
            ["Go to market", "Pipeline {pipeline} USD against {target} USD remaining target. Healthy coverage is 3x for the quarter; below 2x flags a miss.", "Include commits, slipped deals and the top 3 deals at risk."],
            ["Engineering and reliability", "Uptime {uptime} percent versus {uptime_target} percent target. Report error budget consumed, major incidents and the delivery status of the top 3 releases.", "Say plainly if a date is moving."],
            ["Finance and people", "Cash, burn, runway and collections variance; hiring: {offers} offers accepted of {open_roles} open roles, attrition and any regretted losses.", "Flag compensation or legal items that need a decision."],
            ["Format", "Three-minute read: five headline numbers with arrows, three risks, two decisions. Use red, amber, green words not colour alone.", "Send at the same time each week and hold the template steady."],
        ],
        "metrics": ["Pipeline coverage|pipeline / target|{:.1f}x", "Error budget consumed|(100 - uptime) / (100 - uptime_target)|{:.0%}", "Open roles after accepted offers|open_roles - offers|{:.0f}"],
    },
}
