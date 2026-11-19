"""Playbooks for the Engineering & Product Management agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "11-management/11-delegation-coach": {
        "fields": ["tasks|Tasks you hold|number|14", "delegable|Tasks that could be delegated|number|8", "hours_week|Hours a week you spend on delegable tasks|number|11", "person|Person you will delegate to|text|Sam, a senior engineer who wants to grow", "check_in|Check-in rhythm|text|Weekly 15 minutes"],
        "sections": [
            ["Your list", "Tasks: {input}", "{tasks} tasks, {delegable} could be delegated, taking {hours_week} hours a week. Candidate: {person}.", "Delegation is how a manager scales. The question is not whether you can do it faster, but who should learn it and what only you can do."],
            ["What to delegate", "Delegate work that is repeatable, that someone else could do 80 percent as well and that grows another person. Keep decisions on people, strategy and anything with legal or security risk.", "Ask: if I did not exist, who would do this?"],
            ["Match to the person", "Match the task to the person's skill and ambition: {person}. Stretch them, but not beyond what they can recover from. Give less guidance as they prove themselves.", "Use levels: do as told, research and recommend, decide and tell me, decide and act."],
            ["Brief well", "State the outcome, why it matters, the deadline, the limits of authority, the resources and how success is judged. Ask them to repeat the plan in their own words.", "Agree check-ins at the start: {check_in}."],
            ["Follow through", "Review the result, give specific feedback, share credit publicly and avoid taking the task back when it is imperfect. Take it back only for risk you cannot accept.", "Every quarter, hand over one more task."],
        ],
        "metrics": ["Share of your tasks that can be delegated|delegable / tasks|{:.0%}", "Hours a year you could free|hours_week * 48|{:,.0f}"],
    },
    "11-management/12-promotion-packet-builder": {
        "fields": ["employee|Employee|text|Jordan, Senior Engineer", "target_level|Target level|text|Staff Engineer", "months_at_scope|Months operating at the target level|number|11", "required_months|Months you expect before promotion|number|6", "evidence_items|Evidence items collected|number|9"],
        "sections": [
            ["Case", "Notes: {input}", "{employee} for {target_level}. {months_at_scope} months at that scope, {evidence_items} evidence items.", "A promotion packet shows that the person already works at the next level, consistently, with proof from others."],
            ["Map to the level", "List the level's expectations (scope, impact, leadership, craft) and match each with specific work: what they did, the result in numbers and who benefited. Cite documents, not adjectives.", "Show the shape of the work: ambiguity handled, influence without authority."],
            ["Evidence", "Use metrics, shipped work, written designs, peer and partner feedback in their own words and examples of raising the quality of others. Include a candid note on gaps.", "Peers outside the team are the strongest voices."],
            ["Timing and consistency", "Expect sustained performance at level for {required_months} months or more. The person has {months_at_scope}. Check that the evidence is recent and spread over time.", "One big project is not a pattern."],
            ["Process", "Draft with the employee, get calibration feedback early, write for readers who do not know the person and agree the message to give if the answer is not yet.", "A no must come with a clear plan and a date to review."],
        ],
        "metrics": ["Months beyond the expected tenure at level|months_at_scope - required_months|{:+.0f}", "Evidence per month at level|evidence_items / months_at_scope|{:.1f}"],
    },
    "11-management/13-conflict-mediation-guide": {
        "fields": ["parties|People involved|text|Alex and Riya, both senior engineers", "weeks|Weeks the conflict has lasted|number|6", "affected|Teammates affected|number|3", "decision_owner|Who decides ownership|text|The engineering manager, with the architect's input", "follow_up_days|Days until the follow-up|number|14"],
        "sections": [
            ["Situation", "Summary: {input}", "Parties: {parties}. Going for {weeks} weeks, {affected} teammates affected.", "Most conflicts are about unclear roles, scarce resources or different goals. Handle them early, before they harden."],
            ["Listen first", "Meet each person alone. Ask what happened, what they need and what they think the other needs. Separate facts from interpretations, and do not take sides in these conversations.", "Check your own part: unclear ownership is often a management gap."],
            ["Joint conversation", "Set ground rules, have each person say what they need and what is at stake, find shared goals and list options together. Keep to the issue and to specific behaviour.", "Stop and take a break if it escalates."],
            ["Decide and agree", "Where the issue is a decision (ownership), the decision maker is {decision_owner}. Decide, explain why and write it down. Agree behaviours both will keep.", "Cover how disagreements in reviews will be handled in future."],
            ["Follow up", "Check in after {follow_up_days} days with each person, ask the affected teammates how it feels and keep notes. Involve HR if behaviour breaches conduct rules.", "Escalate if the agreement is not kept."],
        ],
        "metrics": ["Weeks per teammate affected|weeks / affected|{:.1f}", "Days from now to the follow-up|follow_up_days|{:,.0f}"],
    },
    "11-management/14-retro-facilitator": {
        "fields": ["team|Team|text|Platform squad", "people|People in the retro|number|8", "minutes|Retro length (minutes)|number|60", "prev_actions|Actions from the last retro|number|4", "prev_done|Actions completed|number|1"],
        "sections": [
            ["Context", "Notes: {input}", "Team: {team}, {people} people, {minutes} minutes. Last retro: {prev_done} of {prev_actions} actions done.", "A retro helps a team change how it works. If nothing changes, people stop caring."],
            ["Start with last time", "Review the previous actions first. Only {prev_done} of {prev_actions} were done. Ask why, drop the ones that are no longer worth doing and keep the rest.", "Repeated problems mean the actions were too big or had no owner."],
            ["Format", "Gather data (timeline, metrics, sticky notes), group themes, vote and then dig into the top two or three. Vary the format so it stays fresh, and keep a safe, no-blame tone.", "Allocate time: about a quarter for data, half for discussion and a quarter for actions."],
            ["Good actions", "Choose at most two or three actions. Make each small, with an owner, a date and a way to see it is done. Put them in the same tracker as normal work.", "An action nobody owns will not happen."],
            ["Follow through", "Revisit the actions in the next stand-ups, share outcomes with your stakeholders and track how many are done as a team measure.", "End by asking what was useful about the retro itself."],
        ],
        "metrics": ["Completion rate of last retro's actions|prev_done / prev_actions|{:.0%}", "Minutes of discussion per person|minutes / people|{:.1f}"],
    },
    "11-management/15-headcount-justifier": {
        "fields": ["team_size|Current team size|number|8", "request|Engineers requested|number|2", "loaded_cost|Fully loaded yearly cost per engineer (USD)|number|210000", "slipped_value|Yearly value of the slipped roadmap items (USD)|number|900000", "load_ratio|Current load as a multiple of target|number|1.8"],
        "sections": [
            ["Request", "Data: {input}", "Team of {team_size}, asking for {request}. Load is {load_ratio} times the target.", "A headcount case answers: what happens if we do not hire, what do we get if we do and why not solve this another way."],
            ["The problem", "Show the load and the delivery gap with numbers: on-call hours, tickets, slipped items and their value. Show the trend and what caused it, not only a snapshot.", "Check attrition and burnout risk. A load of {load_ratio} times target puts people at risk of leaving."],
            ["Alternatives", "Compare the options: reduce scope, automate, change priorities, contract help or move people from another team. Explain why each was rejected or is already in use.", "Leaders hire for needs they have already tried to meet another way."],
            ["Cost and value", "Cost is the loaded yearly cost times the number of engineers. Value is the delivery you recover and the risk you reduce. Be honest about the ramp-up time of 3 to 6 months.", "Show the break-even in months."],
            ["Ask and measures", "State the exact ask, the start date, what will be delivered in 6 and 12 months and the metrics you will report (load, delivery, on-call hours).", "Offer a plan if the answer is no, with what will not be delivered."],
        ],
        "metrics": ["Cost of the request per year (USD)|request * loaded_cost|${:,.0f}", "Delivery value at stake per year (USD)|slipped_value|${:,.0f}", "Value to cost ratio|slipped_value / (request * loaded_cost)|{:.1f}"],
    },
    "11-management/16-first-90-days-planner": {
        "fields": ["role|Role|text|Engineering manager, platform team", "reports|Direct reports|number|9", "one_on_one_min|Minutes per one-on-one|number|45", "weeks_to_plan|Weeks before you present your plan|number|8", "early_win|Early win to aim for|text|Cut the weekly incident count by fixing the top recurring alert"],
        "sections": [
            ["Starting point", "Context: {input}", "Role: {role}. {reports} reports. Plan due in {weeks_to_plan} weeks.", "The first 90 days set your reputation. Learn first, build relationships, then change things with evidence."],
            ["Days 1 to 30: learn", "Hold a one-on-one with each report ({one_on_one_min} minutes), meet peers and key partners, read the roadmap, the incident history and the metrics. Ask the same questions of everyone and look for patterns.", "Do not announce big changes yet. Do fix small, obvious pain."],
            ["Days 31 to 60: decide", "Write down what you heard, share it with the team, choose two or three priorities and agree with your manager on how success is judged. Aim for the early win: {early_win}.", "Check priorities with the team before presenting them upward."],
            ["Days 61 to 90: act", "Present the plan, start the changes, set up team rituals (one-on-ones, retros, metrics review) and give the team clear goals. Ask for feedback on your own style.", "Celebrate early results and credit the team."],
            ["Risks", "Do not change too much at once, avoid blaming your predecessor, keep promises small and watch the low-morale report closely.", "Check in with your boss every week."],
        ],
        "metrics": ["Hours of one-on-one time per cycle|reports * one_on_one_min / 60|{:.1f}", "Weeks left after your plan is presented|13 - weeks_to_plan|{:.0f}"],
    },
    "11-management/17-tradeoff-advisor": {
        "fields": ["capacity_weeks|Engineer-weeks available this quarter|number|30", "ask_a_weeks|Effort of the sales request (engineer-weeks)|number|8", "ask_b_weeks|Effort of the support fixes (engineer-weeks)|number|10", "ask_c_weeks|Effort of the platform upgrade (engineer-weeks)|number|12", "ask_a_value|Value of the sales request (USD)|number|300000"],
        "sections": [
            ["Requests", "Asks: {input}", "Capacity {capacity_weeks} engineer-weeks. Requests need {ask_a_weeks}, {ask_b_weeks} and {ask_c_weeks}.", "Prioritisation is deciding what not to do. Make the trade-off visible, so others can see and challenge it."],
            ["Compare on the same terms", "For each request state the value (revenue, risk reduced, hours saved), the effort, the deadline and what happens if you wait. Convert to money where you can.", "Include the cost of delay: a deadline from a vendor or a security fix has a date, a nice-to-have does not."],
            ["Fit to capacity", "Together the requests need more than the capacity. Rank by value per week of effort, give priority to fixed deadlines and security, and keep 20 percent of capacity free for surprises.", "Check dependencies between requests, since one may unlock another."],
            ["Options", "Offer a partial scope for the large request, a later date for another or a smaller version of the upgrade. Present at least two combinations that fit the capacity.", "Say who decides if the stakeholders disagree."],
            ["Communicate", "Write the decision in one page: what we will do, what we will not do, why and when we will look again. Tell each requester before it is published.", "Record it so the same argument is not repeated next month."],
        ],
        "metrics": ["Total effort requested (engineer-weeks)|ask_a_weeks + ask_b_weeks + ask_c_weeks|{:,.0f}", "Shortfall against capacity (engineer-weeks)|ask_a_weeks + ask_b_weeks + ask_c_weeks - capacity_weeks|{:+,.0f}", "Sales request value per engineer-week (USD)|ask_a_value / ask_a_weeks|${:,.0f}"],
    },
    "11-management/18-skip-level-prep-assistant": {
        "fields": ["people|People you will meet|number|14", "minutes_each|Minutes per conversation|number|30", "engagement|Latest engagement score (0 to 100)|number|64", "benchmark|Company benchmark (0 to 100)|number|74", "manager|Manager of the team|text|Chris"],
        "sections": [
            ["Purpose", "Signals: {input}", "{people} people, {minutes_each} minutes each. Engagement {engagement} against {benchmark}. Manager: {manager}.", "A skip-level conversation gives you ground truth from the people closest to the work. Listen, do not fix on the spot."],
            ["Set it up", "Tell the manager why and what you will do with the information. Tell the team the meeting is for learning, that what they say will not be attributed without consent and that it is not a review of them or the manager.", "Keep the same format for everyone."],
            ["Questions", "What is going well, what is slowing you down, how are priorities set, how do decisions get made, what would you change first and what support do you need from me.", "Ask for examples and follow with 'tell me more'."],
            ["Listen for patterns", "Look for themes across conversations, not single stories: unclear priorities, slow decisions or workload. The gap of {benchmark} minus {engagement} points suggests real concerns.", "Separate issues the manager can fix from issues that need you."],
            ["Follow-up", "Share themes without names with the manager, coach them to act, agree two or three actions with dates and tell the team what you will do within two weeks.", "Close the loop at the next skip level."],
        ],
        "metrics": ["Hours of conversations|people * minutes_each / 60|{:.1f}", "Gap to the company benchmark (points)|benchmark - engagement|{:+.0f}"],
    },
    "11-management/19-blameless-review-facilitator": {
        "fields": ["incident|Incident|text|Checkout outage after a configuration push", "minutes_down|Minutes of impact|number|47", "minutes_to_detect|Minutes to detect|number|9", "actions|Actions agreed|number|5", "action_owners|Actions with a named owner and date|number|3"],
        "sections": [
            ["Incident", "Timeline: {input}", "{incident}: {minutes_down} minutes of impact, detected after {minutes_to_detect} minutes.", "A blameless review assumes people acted sensibly with what they knew. The aim is to fix the system, not to find a culprit."],
            ["Prepare", "Build the timeline from logs, chat and the paging tool before the meeting. Invite the people involved and someone neutral to facilitate. Share the draft a day early.", "Record times in UTC."],
            ["Run the session", "Walk the timeline and ask what people saw and what they understood at each point. Ask how and what questions rather than why-did-you. Look for contributing factors, not a single root cause.", "Stop any blame and bring the talk back to conditions."],
            ["Contributing factors", "Look at detection, response, tooling, process, knowledge and design. A late alert ({minutes_to_detect} minutes) and a missing runbook are system gaps, not personal failures.", "Note what went well so it is kept."],
            ["Actions", "Agree small actions with owners and dates. {action_owners} of {actions} actions have both today. Fix the rest before the meeting ends.", "Track actions to completion and review the metric one month later."],
        ],
        "metrics": ["Share of the outage spent before detection|minutes_to_detect / minutes_down|{:.0%}", "Actions still missing an owner or date|actions - action_owners|{:,.0f}"],
    },
    "11-management/20-feedback-writer": {
        "fields": ["person|Person|text|Taylor", "situation|Situation|text|Tuesday's design review", "behaviour|Observed behaviour|text|Interrupted two junior engineers while they presented", "impact|Impact|text|They stopped presenting and two edge cases were missed", "request|What you ask for next time|text|Let each presenter finish, then ask questions"],
        "sections": [
            ["Feedback for", "Notes: {input}", "Person: {person}. Situation: {situation}.", "Good feedback is specific, timely and about behaviour, not character. It helps the person see what you saw."],
            ["Describe what you saw", "In {situation} I saw this: {behaviour}. State facts you observed, without adjectives or guesses about motive.", "Avoid always and never."],
            ["Say the impact", "The effect was: {impact}. Link the behaviour to results the person cares about, for the team, the customer or their own goals.", "Also share what they do well that you want kept, if it is true and specific."],
            ["Make a request", "For next time I ask: {request}. Invite their view: what was going on for you? Listen before you decide what to do.", "Agree a small next step and a time to check."],
            ["Deliver it well", "Do it in private, soon after the event and in person or on a call. Keep it short, stay calm and follow up in writing if useful.", "Give positive feedback with the same care and frequency."],
        ],
        "metrics": [],
    },
}
