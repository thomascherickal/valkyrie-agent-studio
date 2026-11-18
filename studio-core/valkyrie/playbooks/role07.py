"""Playbooks for the Technical Support agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "07-technical-support/01-ticket-triager": {
        "fields": ["tier|Customer tier|text|Enterprise (Premier support)", "module|Product module|text|SSO and SAML login", "users_affected|Users affected|number|800", "first_response_sla_min|First-response SLA (minutes)|number|30", "minutes_open|Minutes since the ticket arrived|number|5"],
        "sections": [
            ["Ticket", "Text: {input}", "Customer tier: {tier}. Module: {module}. Users affected: {users_affected}."],
            ["Priority rules", "P1: production down or data loss, many users, no workaround. P2: major feature broken or severe degradation with a workaround. P3: single-user or minor defect. P4: question or feature request.", "Raise one level for Enterprise or Premier tiers and for security or billing-impacting issues; never lower on the customer's tone alone."],
            ["Routing", "Route by module to the owning queue (SSO and SAML to identity support, billing to finance support). Tag keywords such as 'down', 'outage', 'cannot log in' and 'data loss' for the P1 detector.", "SAML signature or certificate errors almost always point to expired certificates, clock skew or an IdP metadata change: attach the checklist for those."],
            ["SLA clock", "Start the clock at ticket creation. First response target {first_response_sla_min} minutes; {minutes_open} minutes already used.", "A P1 pages the on-call engineer immediately and opens an incident channel; do not wait for the first response."],
            ["First reply", "Acknowledge impact, state the priority assigned, ask only for missing data (timestamp, tenant id, error text) and give the next update time.", "Do not promise a fix time before diagnosis."],
        ],
        "metrics": ["SLA minutes remaining|first_response_sla_min - minutes_open|{:.0f}", "SLA consumed|minutes_open / first_response_sla_min|{:.0%}"],
    },
    "07-technical-support/02-log-bundle-analyzer": {
        "fields": ["component|Component under investigation|text|API gateway to upstream billing service", "errors|Error lines in the window|number|340", "requests|Total requests in the window|number|18000", "window_min|Window length (minutes)|number|10", "deploy_time|Last deploy or config change|text|2026-11-18 10:05Z config reload"],
        "sections": [
            ["Excerpt", "Log: {input}", "Component: {component}. Last change: {deploy_time}."],
            ["Find the root exception", "Read the first error in time order, not the loudest or the last. Later errors are usually fallout. In a stack trace the root cause is the innermost 'Caused by' line, not the top frame.", "Convert all times to UTC and sort across files before reading."],
            ["Common patterns", "ConnectionResetError with 502 means the upstream closed the socket: look for restarts, idle timeout mismatches (load balancer shorter than server keep-alive) or crashes. Timeout means saturation or a slow dependency. OOMKilled means a memory limit. 401 and 403 lines point to expired credentials.", "Correlate the first error with the deploy or config change time."],
            ["Quantify", "Error rate and error spacing show whether it is constant, bursty or growing. Count distinct error signatures, and group by request id, tenant and host.", "A single host producing most errors points to a bad instance."],
            ["Summary format", "Write: first error time, signature, count, affected component, probable cause, evidence lines (with line numbers), and the next check.", "State confidence and what would disprove the theory."],
        ],
        "metrics": ["Error rate|errors / requests|{:.1%}", "Errors per minute|errors / window_min|{:,.1f}"],
    },
    "07-technical-support/03-escalation-packager": {
        "fields": ["version|Product version|text|v2.4.1", "environment|Customer environment|text|Ubuntu 24.04, 16 GB RAM, behind a corporate proxy", "trace_ids|Trace and request IDs|list|tr_991a, tr_991b", "repro_steps|Reproduction steps|longtext|Open Studio and load the saved agent\nClick Run with the Gemini provider\nObserve the 500 error after about 30 seconds", "tried|Already tried|list|Restarted the service, Cleared the cache, Reinstalled v2.4.0"],
        "sections": [
            ["Summary for L3", "Case notes: {input}", "Version {version}. Environment: {environment}.", "Lead with one line: what is broken, since when, for whom and how badly."],
            ["Reproduction", "*{repro_steps}", "Say whether you reproduced it yourself, how often, and on which version."],
            ["Evidence", "Trace IDs: {trace_ids}", "Attach logs with timestamps in UTC, the redacted config, screenshots or a short recording, and the exact request and response."],
            ["Already tried", "*{tried}", "List outcomes, so engineering does not repeat them."],
            ["Impact and ask", "State customer tier, users affected, business deadline, workaround and the specific ask (hotfix, diagnosis, confirmation of a known bug).", "Strip personal data and secrets; check a sample line before attaching a bundle."],
        ],
        "metrics": [],
    },
    "07-technical-support/04-kb-article-drafter": {
        "fields": ["product_area|Product area|text|Local models and Ollama", "symptoms|Symptoms users see|list|Browser console shows a CORS error, Requests to localhost:11434 are blocked", "affected_versions|Affected versions|text|All versions before 2.5", "tickets_per_month|Tickets per month this would deflect|number|12", "minutes_per_ticket|Handling minutes per ticket|number|18"],
        "sections": [
            ["Article header", "Resolution notes: {input}", "Area: {product_area}. Affected: {affected_versions}.", "Title: state the symptom in the user's words, for example 'Fix: Ollama requests blocked by CORS error'."],
            ["Symptoms", "*{symptoms}", "Include the exact error text so the article is findable by search."],
            ["Cause and fix", "Explain the cause in one or two sentences, then give numbered steps with commands that can be copied. State the expected result after each step and how to verify the fix.", "Show the setting from the resolution notes exactly, and warn about restarting the service so the change applies."],
            ["If it still fails", "List the next two checks and when to contact support, with the information to include (version, logs, trace id).", "Link related articles and the release that fixes it permanently."],
            ["Quality and impact", "One problem per article, tested by someone who was not on the ticket, reviewed every 6 months or at each major release. Tag by product area and error code.", "Expected deflection: see the figures below."],
        ],
        "metrics": ["Support hours saved per month|tickets_per_month * minutes_per_ticket / 60|{:,.1f}", "Support hours saved per year|tickets_per_month * minutes_per_ticket * 12 / 60|{:,.0f}"],
    },
    "07-technical-support/05-sla-breach-predictor": {
        "fields": ["sla_min|SLA target (minutes)|number|30", "elapsed_min|Minutes elapsed|number|22", "queue_ahead|Tickets ahead in the queue|number|3", "agents_online|Agents online|number|2", "touch_min|Average minutes to first touch per ticket|number|6"],
        "sections": [
            ["Queue snapshot", "Snapshot: {input}", "SLA {sla_min} minutes; {elapsed_min} elapsed; {queue_ahead} tickets ahead with {agents_online} agents online."],
            ["Risk model", "Risk grows when remaining time is shorter than the projected wait. Projected wait = tickets ahead / agents online x average first-touch time. Flag when projected wait exceeds remaining time, or when more than 75 percent of the SLA has elapsed.", "Weight by tier: Enterprise P1 breaches matter more than P3 free-tier ones."],
            ["Alert levels", "Amber at 50 percent of the SLA elapsed and unassigned; red at 75 percent or projected breach. Send red alerts to the queue lead and the on-call manager, not only a channel.", "Include ticket link, owner, customer tier and the minutes left."],
            ["Interventions", "Reassign to an available agent, pull in a swarm, post a holding reply that counts as a first response if policy allows, or escalate to engineering for P1.", "Pause the clock only for states the contract permits (waiting on customer)."],
            ["Retrospective", "Review all breaches weekly: cause (staffing, routing, handoff, time zone) and fix. Track breach rate and near-miss rate.", "Staff to the forecast arrival rate; Erlang C helps size shifts."],
        ],
        "metrics": ["Minutes left|sla_min - elapsed_min|{:.0f}", "Projected minutes to first touch|queue_ahead / agents_online * touch_min|{:.1f}", "Projected breach margin (minutes)|sla_min - elapsed_min - queue_ahead / agents_online * touch_min|{:.1f}"],
    },
    "07-technical-support/06-config-validator": {
        "fields": ["ir_version|Config schema version|text|1.0.0", "allowed_levels|Allowed thinking_level values|list|low, medium, high", "providers|Supported providers|list|gemini, openrouter, ollama", "required_keys|Required top-level keys|list|id, name, role, version, system_prompt, model_config_spec, tools, input_schema, output_schema"],
        "sections": [
            ["Snippet", "Config: {input}", "Schema version {ir_version}."],
            ["Syntax checks", "YAML pitfalls: tabs instead of spaces, inconsistent indentation, unquoted strings containing a colon or a hash, values like yes/no/on/off parsed as booleans, and a duplicated key. A comment starts at ' #'.", "Report line and column of the first error, then re-validate after each fix."],
            ["Enum checks", "thinking_level must be one of the following values.", "*{allowed_levels}", "A value such as 'ultra' is invalid. Suggest the closest allowed value instead of only rejecting it."],
            ["Required fields and types", "Required keys present:", "*{required_keys}", "Check types: temperature is a number between 0 and 2, max_tokens a positive integer, tools a list with name, description and parameters, schemas as key to type maps."],
            ["Provider checks", "Supported providers:", "*{providers}", "Confirm that the model name is valid for the provider and that the matching API key is configured before running."],
        ],
        "metrics": [],
    },
    "07-technical-support/07-api-error-explainer": {
        "fields": ["api|API and plan|text|Gemini API, free tier", "quota_rpm|Quota (requests per minute)|number|15", "current_rpm|Your current rate (requests per minute)|number|40", "retry_after_s|Retry-After (seconds)|number|30", "daily_quota|Daily quota (requests)|number|1500"],
        "sections": [
            ["Error", "Payload: {input}", "API: {api}."],
            ["What it means", "4xx errors are the caller's problem, 5xx the server's. 400 malformed request, 401 missing or bad credentials, 403 permission or region, 404 wrong path or model name, 408 timeout, 409 conflict, 422 validation, 429 rate or quota exceeded, 500 server fault, 502 and 503 temporary upstream trouble.", "RESOURCE_EXHAUSTED with 429 means a quota (requests per minute or per day, or tokens) was used up."],
            ["Your situation", "Quota {quota_rpm} requests per minute and {daily_quota} per day; you are sending about {current_rpm} per minute.", "Wait the Retry-After time ({retry_after_s} seconds) before retrying."],
            ["Fix steps", "1. Add retries with exponential backoff and jitter (1, 2, 4, 8 seconds), honouring Retry-After. 2. Throttle the client to stay under the limit. 3. Batch or cache repeated prompts. 4. Move to a paid tier or another provider for more headroom.", "Do not retry 400, 401, 403 or 404: they will fail again."],
            ["Escalate when", "Contact support if 5xx persists longer than 15 minutes, the quota page shows capacity but 429 continues, or the error id is not documented. Include the request id, time in UTC and model name.", "Check the provider status page first."],
        ],
        "metrics": ["Over quota by|max(0, current_rpm - quota_rpm)|{:.0f} requests per minute", "Rate versus quota|current_rpm / quota_rpm|{:.1f}x", "Minimum spacing between requests (seconds)|60 / quota_rpm|{:.1f}"],
    },
    "07-technical-support/08-onboarding-concierge": {
        "fields": ["team_size|Team size|number|50", "identity|Identity provider|text|Okta", "repo_host|Source host|text|GitHub", "target_pct|Target activation by day 7 (percent)|number|80", "champion|Customer champion|text|Dana, staff engineer"],
        "sections": [
            ["Customer profile", "Profile: {input}", "{team_size} people, identity {identity}, code on {repo_host}. Champion: {champion}."],
            ["Day 1 to 2", "Kickoff call with the champion; confirm goals and success criteria. Configure SSO with {identity} (SAML or OIDC), enforce MFA, create groups and roles. Connect {repo_host}.", "Success check: 5 pilot users sign in through SSO."],
            ["Day 3 to 4", "Run the quickstart with pilot users on a real service, install the CLI or desktop app, and set up the API keys and provider limits. Review security and data-handling questions.", "Success check: first agent deployed in staging."],
            ["Day 5 to 7", "Invite the wider team in waves, run a 45-minute training, share runbooks and the support channel, and schedule a day-7 review.", "Success check: at least the target share of users have run an agent."],
            ["Health and risks", "Track activation (target {target_pct} percent), time to first deploy, and open blockers. Typical blockers: proxy and firewall rules, SSO attribute mapping, procurement and security review.", "Assign an owner and date to every blocker at kickoff."],
        ],
        "metrics": ["Users to activate by day 7|team_size * target_pct / 100|{:,.0f}", "Pilot group (10 percent, minimum 5)|max(5, team_size / 10)|{:,.0f}"],
    },
    "07-technical-support/09-churn-signal-spotter": {
        "fields": ["escalations_30d|Escalations in the last 30 days|number|3", "days_to_renewal|Days to renewal|number|21", "csat|Latest CSAT (1 to 5)|number|2.1", "arr|Annual contract value (USD)|number|120000", "usage_trend|Change in weekly active users (percent)|number|-25"],
        "sections": [
            ["Account history", "Threads: {input}", "{escalations_30d} escalations in 30 days, CSAT {csat}, usage trend {usage_trend} percent, renewal in {days_to_renewal} days."],
            ["Signals", "Strong: repeat escalations on the same issue, executive complaints, requests for contract terms or data export, a champion who left. Medium: falling usage, unresolved bugs above 30 days, negative sentiment in replies. Weak: slow responses from the customer.", "Look at the trend across tickets: one angry ticket matters less than three polite ones on the same defect."],
            ["Risk score", "Score 0 to 100: 20 points per escalation, plus up to 30 as renewal nears (within 60 days), plus 10 per CSAT point below 3.5. Red above 70, amber 40 to 70, green below.", "Combine with usage data; support signals alone miss silent churn."],
            ["Save plan", "For red accounts: notify the CSM within 24 hours, name an executive sponsor, hold a root-cause call, commit to dates on the open defects and offer a success review before the renewal.", "Document commitments and follow up weekly until renewal."],
            ["Learning", "Record outcomes (saved, churned, expanded) and which signals predicted them to reweight the score each quarter.", "Share top recurring issues with product."],
        ],
        "metrics": ["Churn risk score (0 to 100)|min(100, escalations_30d * 20 + max(0, 60 - days_to_renewal) * 0.5 + max(0, 3.5 - csat) * 10)|{:.0f}", "ARR at risk|arr|${:,.0f}", "ARR per day left to renewal|arr / days_to_renewal|${:,.0f}"],
    },
    "07-technical-support/10-status-page-updater": {
        "fields": ["component|Affected component|text|US-West inference router", "started|Start time|text|10:12 UTC", "impact|Customer-visible impact|text|Some requests are slower than usual and a small share time out", "stage|Current stage|text|Investigating", "next_update_min|Minutes until next update|number|30"],
        "sections": [
            ["Update draft", "Internal state: {input}", "Stage: {stage}. Component: {component}. Started: {started}.", "Title: '{stage}: {component} performance'."],
            ["Message body", "We are {stage} an issue affecting {component}. Since {started}, customers may notice: {impact}", "Next update in {next_update_min} minutes, or sooner if there is a change."],
            ["Tone rules", "Plain language, no internal jargon, no hostnames, no blame on vendors or people, no speculation about cause or time to fix. Say what customers see and what they can do (retry, use another region).", "Use the standard stages in order: Investigating, Identified, Monitoring, Resolved."],
            ["Cadence", "Update at least every 30 minutes for major incidents and 60 minutes for minor ones, even if the update is 'no change'. Post the first update within 15 minutes of confirmation.", "Mark the component status accurately: degraded performance, partial outage or major outage."],
            ["Resolution message", "State when service was restored, the window of impact, and that a summary will follow within 5 working days for major incidents.", "Notify subscribers by email and webhook, and keep the history public."],
        ],
        "metrics": [],
    },
}
