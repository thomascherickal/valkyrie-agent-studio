"""Playbooks for the C-Suite & Executives (CxOs) agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "12-cxos/11-cash-runway-analyst": {
        "fields": ["cash|Cash balance (USD)|number|14200000", "burn|Net burn per month (USD)|number|780000", "hiring_add|Extra monthly cost from the hiring plan (USD)|number|600000", "downside_burn_pct|Burn increase in the downside case (0 to 1)|number|0.15", "trigger_months|Runway at which you act (months)|number|12"],
        "sections": [
            ["Position", "Position: {input}", "Cash {cash} USD, net burn {burn} USD a month, plan adds {hiring_add} USD. Action trigger: {trigger_months} months.", "Runway is how many months you can operate before cash runs out. Report it as a range, and decide the triggers in advance."],
            ["Three cases", "Base: current burn with the hiring plan. Downside: burn rises by {downside_burn_pct} and the pending deals slip a quarter. Upside: the deals close on time. Report months of runway and the cash-out date for each.", "Use cash collections, not bookings, and include annual payments and taxes."],
            ["Triggers", "Agree thresholds with the board: raise or cut when runway in the base case falls to {trigger_months} months, freeze hiring at an earlier threshold. Fundraising takes 6 to 9 months, so start with at least 12 months left.", "Write down which costs you would cut first, and their savings."],
            ["Sensitivities", "Test collections delays of 30 days, a lost top customer, a currency move and a hiring plan that runs early. Identify the one assumption that moves the date most.", "Update weekly if runway is below 12 months."],
            ["Decisions", "Prepare the cuts that would extend runway by 3, 6 and 12 months and what each would cost in growth. Present them with the base case, not after the downside happens.", "Review the plan monthly with the CFO."],
        ],
        "metrics": ["Runway at current burn (months)|cash / burn|{:.1f}", "Runway with the hiring plan (months)|cash / (burn + hiring_add)|{:.1f}", "Runway in the downside case (months)|cash / ((burn + hiring_add) * (1 + downside_burn_pct))|{:.1f}"],
    },
    "12-cxos/12-fundraising-narrative-builder": {
        "fields": ["arr|Annual recurring revenue (USD)|number|4100000", "growth|Yearly growth (0 to 3)|number|1.6", "raise|Amount raising (USD)|number|20000000", "burn|Monthly net burn after the raise (USD)|number|830000", "nrr|Net revenue retention (0 to 2)|number|1.18"],
        "sections": [
            ["Facts", "Facts: {input}", "ARR {arr} USD, growth {growth} a year, net retention {nrr}. Raising {raise} USD.", "An investor story is a short argument: a big problem, a product that solves it, proof it works, a team that can scale it and why now."],
            ["The argument", "Problem and who has it, the product and why it wins, the market and why now, proof (growth, retention, customers by name), the team and the plan for the money.", "Put the strongest number on the first slide and the one-sentence story in the first minute."],
            ["Proof points", "Use cohort retention, net revenue retention of {nrr}, payback and growth at scale. Show how the numbers were calculated and avoid cherry-picked periods.", "Anticipate the hard questions: churn, concentration, competition and burn."],
            ["Use of funds", "Show what the {raise} USD buys: hires, product and go-to-market, with the milestones that will be reached and the runway it gives at the planned burn.", "Tie spending to the metric the next round will be judged on."],
            ["Process", "Build a target list of investors by stage and thesis, run the process in a tight window, keep a data room ready and update the story with feedback after each meeting.", "Track meetings, questions and objections in one document."],
        ],
        "metrics": ["Runway after the raise (months)|raise / burn|{:.0f}", "Raise as a multiple of ARR|raise / arr|{:.1f}", "ARR in 12 months at the current growth (USD)|arr * (1 + growth)|${:,.0f}"],
    },
    "12-cxos/13-board-risk-register-keeper": {
        "fields": ["risks|Risks on the register|number|18", "high|Risks rated high|number|5", "without_owner|Risks with no named executive owner|number|2", "overdue|Risks whose review is overdue|number|4", "top_risk|Top risk|text|One customer is 31 percent of revenue"],
        "sections": [
            ["Register", "Risks: {input}", "{risks} risks, {high} rated high, {without_owner} without an owner, {overdue} reviews overdue. Top risk: {top_risk}.", "A board risk register is short, current and owned. It should drive decisions and not sit in a file."],
            ["Rate each risk", "Score likelihood and impact on a 1 to 5 scale, multiply and rank. Define the scales in money and time so ratings are consistent across executives.", "Rate before and after mitigation, so the board sees what the controls achieve."],
            ["Owners and actions", "Each risk has one executive owner, a mitigation with a date and a measure that shows if it is working. Assign owners to the {without_owner} risks that have none.", "Overdue reviews ({overdue}) mean the register is not being used."],
            ["Top risk", "{top_risk}. Describe the exposure, the early warning signs, the plan and the cost of the plan. Show what you would do if it happened.", "Link each major risk to a scenario you have rehearsed."],
            ["Board rhythm", "Review the top 5 each quarter, and the full register twice a year. Show what moved up or down and why, add emerging risks and remove closed ones.", "Report incidents that were on the register and how the controls worked."],
        ],
        "metrics": ["Share of risks rated high|high / risks|{:.0%}", "Risks with a gap in ownership or review|without_owner + overdue|{:,.0f}"],
    },
    "12-cxos/14-executive-pricing-strategist": {
        "fields": ["accounts|Accounts on the plan|number|6200", "price|Current monthly price per account (USD)|number|59", "increase|Proposed increase (0 to 1)|number|0.12", "extra_churn|Extra accounts lost per month from the rise (0 to 1)|number|0.015", "margin|Gross margin (0 to 1)|number|0.8"],
        "sections": [
            ["Decision", "Context: {input}", "{accounts} accounts at {price} USD. Proposed rise {increase}. Extra churn risk {extra_churn}.", "A price change is one of the highest-leverage decisions a company makes. Test it before you apply it to everyone."],
            ["Value and market", "Check what customers get for the price, how it compares with alternatives and what they would pay in surveys. A rise is easier to defend when you have shipped new value since the last one.", "Look at willingness to pay by segment."],
            ["Math", "Compare the gain per account with the revenue lost from extra churn over 12 months, using gross margin. The rise pays if gain per remaining account outweighs lost accounts.", "Include effects on expansion, discounts and support load."],
            ["Roll-out", "Test on new customers first, then give existing customers notice, a grandfathering period or an annual lock-in option. Brief sales and support with the reasons.", "Avoid changes just before renewals of large accounts."],
            ["Measure and reverse", "Track conversion, churn, downgrades and sales feedback weekly, with a rule in advance for when you would pause or roll back.", "Review again after one full billing cycle."],
        ],
        "metrics": ["New price (USD)|price * (1 + increase)|${:,.2f}", "Monthly revenue gain before churn (USD)|accounts * price * increase|${:,.0f}", "Monthly revenue lost to extra churn (USD)|accounts * extra_churn * price * (1 + increase)|${:,.0f}"],
    },
    "12-cxos/15-partnership-evaluator": {
        "fields": ["accounts|Accounts the partner can reach|number|800", "conversion|Expected share who become customers (0 to 1)|number|0.04", "deal_value|Yearly value per customer (USD)|number|24000", "rev_share|Revenue share to the partner (0 to 1)|number|0.25", "own_cac|Your own cost to acquire a customer (USD)|number|14000"],
        "sections": [
            ["Proposal", "Terms: {input}", "Reach {accounts} accounts, expected conversion {conversion}, revenue share {rev_share}.", "A partnership should deliver customers or capability you cannot get as cheaply alone, without giving up control of the customer."],
            ["Strategic fit", "Does the partner reach your ideal customer, share your values and have a brand you want next to yours? Does it help your core strategy or distract from it?", "Talk to the partner's other partners."],
            ["Economics", "Compare the revenue share paid over the customer's life with what you would spend on your own acquisition. A share of {rev_share} for several years can cost more than {own_cac} USD of direct cost.", "Model the case where only half of the expected customers arrive."],
            ["Terms to negotiate", "Limit exclusivity (by segment and time), include performance minimums, keep ownership of the customer data and relationship, set a clear end and a transition plan and agree how brand use is reviewed.", "Avoid terms that block other channels."],
            ["Decision", "Run a pilot with a small group and clear success numbers before the full deal. Decide with a score on fit, economics, risk and effort, and record why.", "Review the partnership every six months."],
        ],
        "metrics": ["Expected customers|accounts * conversion|{:,.0f}", "Yearly revenue from them (USD)|accounts * conversion * deal_value|${:,.0f}", "Yearly share paid to the partner (USD)|accounts * conversion * deal_value * rev_share|${:,.0f}"],
    },
    "12-cxos/16-exec-search-planner": {
        "fields": ["role|Role|text|VP Sales", "weeks_needed|Weeks a typical search takes|number|16", "weeks_left|Weeks until the current leader leaves|number|12", "candidates|Candidates you plan to interview|number|12", "base|Target base salary (USD)|number|280000"],
        "sections": [
            ["Need", "Context: {input}", "Role: {role}. Search takes about {weeks_needed} weeks, the leader leaves in {weeks_left}. {candidates} interviews planned.", "An executive hire shapes the company for years. Be clear about what the next 18 months need, and not only about a person you liked."],
            ["Scorecard", "Write 3 to 5 outcomes for the first 18 months, the experience that predicts them, the style needed and the deal-breakers. Agree the scorecard with the CEO and the board before sourcing.", "Score every candidate on the same scorecard."],
            ["Sourcing", "Use the network and a search firm if the market is thin. Aim for a diverse slate, and approach people who have done this at your stage, not only bigger companies.", "Sell the role: the problem, the team and the support."],
            ["Process", "Stages: screen, hiring manager, panel, case or presentation, references (including backchannel) and a final with the CEO. Debrief each stage the same day and decide using evidence.", "Keep the process under 6 weeks per candidate."],
            ["Offer and landing", "Prepare an offer with base around {base} USD, variable and equity, and close personally. Plan an interim leader because the search takes {weeks_needed} weeks and your leader leaves in {weeks_left}.", "Write a 90-day plan for the new executive."],
        ],
        "metrics": ["Weeks without a leader|weeks_needed - weeks_left|{:+.0f}", "Interviews per week over the search|candidates / weeks_needed|{:.1f}"],
    },
    "12-cxos/17-earnings-call-prep-coach": {
        "fields": ["revenue_growth|Revenue growth (0 to 1)|number|0.22", "guided_growth|Guided growth (0 to 1)|number|0.25", "margin_change|Gross margin change (points)|number|-1.8", "questions|Questions you expect|number|20", "rehearsals|Rehearsals planned|number|3"],
        "sections": [
            ["Results", "Results: {input}", "Growth {revenue_growth} against guidance {guided_growth}. Margin change {margin_change} points.", "An earnings call is a disclosure event. Tell the same story investors will read in the numbers, plainly, and never give new material facts selectively."],
            ["Core messages", "Three messages: what happened this quarter and why, what is changing, and what you expect. Own a miss in the first minute and explain the cause and the fix.", "Reconcile non-standard measures to the standard ones."],
            ["Tough questions", "Prepare {questions} likely questions: the miss against guidance, the margin fall, the guidance cut, the one-time charge, competition and cash. Write short, honest, consistent answers and agree who answers each.", "Do not guess: say you will follow up, and do it publicly."],
            ["Disclosure rules", "Check every statement against fair disclosure and forward-looking statement rules, have legal review the script and the answers and keep the same information in the press release and the call.", "Do not discuss unreleased results outside the call."],
            ["Rehearse", "Hold {rehearsals} rehearsals with a hostile questioner, time the prepared remarks and review the transcript afterwards for tone and clarity.", "Prepare the follow-up emails and the investor meetings after the call."],
        ],
        "metrics": ["Growth versus guidance (points)|(revenue_growth - guided_growth) * 100|{:+.1f}", "Preparation questions per rehearsal|questions / rehearsals|{:.1f}"],
    },
    "12-cxos/18-cyber-risk-briefer": {
        "fields": ["critical_open|Critical findings open|number|3", "mfa|Staff covered by MFA (0 to 1)|number|0.91", "restore_months|Months since the last restore test|number|14", "downtime_cost|Cost of one day of downtime (USD)|number|450000", "recovery_days|Estimated days to recover from ransomware|number|6"],
        "sections": [
            ["Headline", "Summary: {input}", "{critical_open} critical findings open, MFA coverage {mfa}, restore last tested {restore_months} months ago.", "Executives need to know whether the company is safe enough, what could go wrong in money terms and what decision you need from them."],
            ["Business exposure", "Translate technical risk into effect: a ransomware event with {recovery_days} days to recover and {downtime_cost} USD a day of downtime has a cost the board can compare with the budget request.", "Include legal, notice and reputational costs."],
            ["Controls that matter", "Report on a few: multi-factor authentication, patching speed, backups that have been restored in a test, detection and response time and staff training. Show the trend and the target.", "A restore test older than 6 months means you do not know that backups work."],
            ["Decisions needed", "Ask for specific decisions: fund this control, accept this risk until a date, or change this process. Give the cost, the risk reduced and the option of doing nothing.", "Record accepted risks with an owner and a review date."],
            ["Rhythm", "Brief quarterly with one page and a short trend chart, with an immediate escalation path for serious incidents. Run a tabletop exercise each year with the executive team.", "Compare against a standard framework such as NIST CSF."],
        ],
        "metrics": ["Estimated cost of a ransomware event (USD)|downtime_cost * recovery_days|${:,.0f}", "Staff without MFA|1 - mfa|{:.0%}"],
    },
    "12-cxos/19-esg-metrics-reporter": {
        "fields": ["electricity_mwh|Electricity use (MWh)|number|2320", "renewable|Renewable share (0 to 1)|number|0.58", "factor|Grid emissions factor (tCO2e per MWh)|number|0.38", "travel_tco2e|Business travel emissions (tCO2e)|number|310", "baseline_tco2e|Baseline year emissions (tCO2e)|number|1500"],
        "sections": [
            ["Inputs", "Inputs: {input}", "Electricity {electricity_mwh} MWh, {renewable} renewable. Travel {travel_tco2e} tCO2e. Baseline {baseline_tco2e} tCO2e.", "Sustainability reports earn trust when the boundary, method and data quality are clear, not when the numbers are small."],
            ["Boundary and method", "State the organisational boundary, the reporting year and the standard used (for example the Greenhouse Gas Protocol). Report Scope 1, Scope 2 (location and market based) and the Scope 3 categories you can measure.", "Say which categories you excluded and why."],
            ["Calculate", "Scope 2 location-based emissions are electricity multiplied by the grid factor. Market-based emissions use the supplier's factor or certificates for the renewable share. Add travel and the other categories you track.", "Keep the data source, factor and date for each number."],
            ["Targets", "Compare with the baseline year and set a reduction target with interim steps. Describe the actions behind the number (renewable contracts, cloud efficiency, travel policy).", "Report progress honestly, including years when emissions rose."],
            ["Assurance readiness", "Keep a data file with owners, versions and checks, test a sample of numbers against invoices and meter readings and plan for limited external assurance.", "Avoid claims you cannot support."],
        ],
        "metrics": ["Location-based electricity emissions (tCO2e)|electricity_mwh * factor|{:,.0f}", "Estimated emissions after the renewable share (tCO2e)|electricity_mwh * factor * (1 - renewable)|{:,.0f}", "Total with travel (tCO2e)|electricity_mwh * factor * (1 - renewable) + travel_tco2e|{:,.0f}"],
    },
    "12-cxos/20-strategic-bet-reviewer": {
        "fields": ["investment|Total investment (USD)|number|4000000", "stage_one|Investment in the first stage (USD)|number|900000", "success_prob|Probability of success you believe (0 to 1)|number|0.3", "payoff|Value if it succeeds (USD)|number|30000000", "months|Months to the first gate|number|6"],
        "sections": [
            ["Bet", "Proposal: {input}", "Investment {investment} USD, first stage {stage_one} USD. Success probability {success_prob}, payoff {payoff} USD.", "A strategic bet is a decision to invest under uncertainty. Judge the reasoning and the staging, not only the story."],
            ["Assumptions", "List the beliefs that must be true: demand, willingness to pay, ability to meet requirements and the team's ability to execute. Rank by uncertainty and impact and design the cheapest tests of the top ones.", "Ask what would make a smart sceptic say no."],
            ["Expected value", "Expected value is the probability of success times the payoff, minus the investment. Compare it with other uses of the money and include the opportunity cost of the team's time.", "Be wary of probabilities that were chosen to make the answer work."],
            ["Stage the money", "Fund the first stage ({stage_one} USD) to test the biggest assumption in {months} months, with a gate. Release the rest only if the evidence passes the gate.", "Staging keeps your option to stop at a small cost."],
            ["Kill criteria", "Write the signals that would stop the bet before it starts: signed contracts, pilot results, compliance timeline and cost. Agree who decides at the gate and record the decision.", "Review the bet at each gate and share the lessons even if it ends."],
        ],
        "metrics": ["Expected value (USD)|success_prob * payoff - investment|${:,.0f}", "Share of the money at risk in the first stage|stage_one / investment|{:.0%}", "Payoff as a multiple of the investment|payoff / investment|{:.1f}"],
    },
}
