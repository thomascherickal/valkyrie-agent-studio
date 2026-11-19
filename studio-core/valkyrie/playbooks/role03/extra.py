"""Playbooks for the DevOps & SRE agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "03-devops-sre/11-oncall-load-analyzer": {
        "fields": ["pages|Pages in the period|number|212", "weeks|Weeks in the period|number|4", "after_hours|Pages outside working hours|number|61", "engineers|Engineers in the rotation|number|9", "top_service_pages|Pages from the noisiest service|number|74"],
        "sections": [
            ["Load readout", "Stats: {input}", "{pages} pages over {weeks} weeks with {engineers} engineers in the rotation.", "Sustainable on-call means few pages, mostly in working hours, spread fairly and almost all needing a human."],
            ["Targets", "Common guidance is at most two pages per 12-hour shift and rarely more than one night disturbed per week.", "Count pages per shift, not per week, and track night pages separately because they cost recovery time."],
            ["Fairness", "Compare pages and night hours per person. Rotate weekends and holidays fairly, and give time off after a bad night.", "A rotation of fewer than 6 people burns people out. Add engineers or share the rotation with another team."],
            ["Noisiest service", "One service produced {top_service_pages} of the pages. Fix or tune its alerts before adding people to the rota.", "For each page ask: did it need a human, was it urgent and was there a runbook."],
            ["Actions", "Delete or downgrade pages nobody acted on, automate the common fix and review the numbers monthly with the whole rotation.", "Pay or compensate for after-hours pages according to your policy."],
        ],
        "metrics": ["Pages per week|pages / weeks|{:,.1f}", "Share outside working hours|after_hours / pages|{:.0%}", "Pages per engineer per week|pages / weeks / engineers|{:.1f}"],
    },
    "03-devops-sre/12-alert-noise-reducer": {
        "fields": ["alert|Noisiest alert|text|CPUHigh", "fired|Times it fired|number|310", "actioned|Times a human acted on it|number|4", "minutes_each|Minutes spent per firing|number|6", "hourly_cost|Cost of an engineer hour (USD)|number|90"],
        "sections": [
            ["History", "History: {input}", "Noisiest alert: {alert}, fired {fired} times and led to action {actioned} times.", "An alert is good when firing means a person must do something now. Everything else is a dashboard, a ticket or noise."],
            ["Ranking", "Rank alerts by firing count multiplied by the share that needed no action. The top of this list gives the biggest relief for the least work.", "Check flapping alerts separately: they open and close repeatedly and multiply the count."],
            ["Tuning options", "Lengthen the 'for' duration, raise the threshold, alert on symptoms (user impact, error budget burn) and not on causes (CPU), and group related alerts into one page.", "Send low-urgency alerts to chat or tickets, not to the pager."],
            ["Delete or keep", "Delete an alert if it has not led to action in 90 days and no incident would have been missed. Keep it as a dashboard panel instead.", "Review every deleted alert against past incidents first."],
            ["Process", "Hold a monthly alert review, require every new alert to have an owner, a runbook link and a severity, and track the action rate as a team metric.", "Aim for an action rate above 70 percent."],
        ],
        "metrics": ["Action rate of the noisiest alert|actioned / fired|{:.1%}", "Hours wasted on it|(fired - actioned) * minutes_each / 60|{:,.0f}", "Cost of the wasted time (USD)|(fired - actioned) * minutes_each / 60 * hourly_cost|${:,.0f}"],
    },
    "03-devops-sre/13-dr-plan-reviewer": {
        "fields": ["rto_h|Target recovery time RTO (hours)|number|4", "rpo_h|Target data loss RPO (hours)|number|1", "backup_h|Hours between backups|number|24", "restore_h|Measured restore time (hours)|number|9", "last_test|When the plan was last tested|text|Never"],
        "sections": [
            ["Plan under review", "Plan: {input}", "Targets: RTO {rto_h} hours, RPO {rpo_h} hours. Last tested: {last_test}.", "A plan that has not been exercised is a hypothesis. Evidence from a restore drill is the only proof."],
            ["Data loss check", "Backups every {backup_h} hours mean up to that much data can be lost. The target is {rpo_h} hours.", "Close the gap with more frequent snapshots, log shipping or replication to a second region."],
            ["Recovery time check", "A measured restore of {restore_h} hours against a target of {rto_h} hours means the plan fails its own target.", "Time the whole chain: detect, decide, restore, verify and switch traffic."],
            ["Hidden dependencies", "Check DNS, identity provider, secrets store, container registry, certificate authority and third-party APIs. A recovery that needs a broken dependency cannot start.", "Keep backups and recovery credentials outside the failure domain, in another region or account."],
            ["Drill programme", "Run a restore test every quarter and a full failover every year. Record time, problems found and fixes made.", "Keep the plan printed or offline, because the wiki may be down too."],
        ],
        "metrics": ["Worst-case data loss exceeds target by (hours)|backup_h - rpo_h|{:+.0f}", "Restore time over target (hours)|restore_h - rto_h|{:+.1f}"],
    },
    "03-devops-sre/14-helm-chart-reviewer": {
        "fields": ["chart|Chart name|text|payments-api", "replicas|Replica count|number|1", "min_replicas|Replicas you require|number|3", "cpu_request_m|CPU request (millicores)|number|0", "image_tag|Image tag in values|text|latest"],
        "sections": [
            ["Values under review", "Values: {input}", "Chart: {chart}. Image tag: {image_tag}.", "Chart defaults are what the next team will deploy without reading. Make the safe choice the default one."],
            ["Image", "Pin an immutable tag or a digest. A tag of {image_tag} gives different pods on each restart and makes rollback guesswork.", "Set the pull policy to IfNotPresent for pinned tags and scan the image in CI."],
            ["Resources", "Set requests and limits for CPU and memory. With no requests the scheduler packs pods blindly. A CPU request of {cpu_request_m} millicores gives no guarantee.", "Base the numbers on measured p95 usage plus headroom."],
            ["Availability", "Use at least {min_replicas} replicas for a service that must stay up, spread across zones, with a PodDisruptionBudget and readiness and liveness probes.", "You have {replicas} replica now: one node drain means an outage."],
            ["Upgrade safety", "Render with helm template and diff against the live release. Check for renamed values, immutable field changes and CRD updates, and test an upgrade from the oldest supported version.", "Lock chart and dependency versions in the lock file."],
        ],
        "metrics": ["Replicas short of the minimum|min_replicas - replicas|{:,.0f}"],
    },
    "03-devops-sre/15-secret-rotation-planner": {
        "fields": ["secrets|Secrets in scope|number|86", "old_secrets|Secrets older than policy|number|23", "shared|Secrets shared by several services|number|9", "no_owner|Secrets without an owner|number|11", "minutes_each|Minutes to rotate one secret|number|40"],
        "sections": [
            ["Inventory", "Inventory: {input}", "{old_secrets} of {secrets} secrets are older than policy, {shared} are shared and {no_owner} have no owner.", "Rotate for two reasons: to limit how long a leaked secret works and to prove you can replace one in an emergency."],
            ["Order of work", "Start with long-lived, shared secrets with a wide reach, such as database admin passwords and cloud keys. Then the old, owned secrets.", "Give every unowned secret an owner first: nobody can rotate what nobody knows."],
            ["Zero-downtime rotation", "Create the new secret, make the system accept both, switch clients to the new one, confirm the old one is unused and then revoke it.", "Use dual credentials where the system supports it, or short-lived credentials from a vault instead of static ones."],
            ["Sharing", "Give each service its own credential so that one leak has a small reach and rotation does not need all teams at once.", "Remove secrets from code, images and chat history, and scan for them in CI."],
            ["Automation", "Move to a secrets manager with automatic rotation for databases and cloud keys. Alert on secrets near expiry.", "Run a rotation drill every quarter for the most critical secret."],
        ],
        "metrics": ["Hours to rotate the old secrets by hand|old_secrets * minutes_each / 60|{:,.1f}", "Share of secrets that are old|old_secrets / secrets|{:.0%}"],
    },
    "03-devops-sre/16-blast-radius-mapper": {
        "fields": ["dependency|Dependency|text|auth-service", "callers|Services that call it|number|14", "no_fallback|Callers with no fallback|number|6", "hourly_revenue|Revenue per hour that depends on it (USD)|number|18000", "outage_hours|Expected outage hours per year|number|4"],
        "sections": [
            ["Map", "Service map: {input}", "Dependency: {dependency}, called by {callers} services, {no_fallback} of them with no fallback.", "A dependency's blast radius is every service that fails or degrades when it fails, directly or through a chain."],
            ["Hard and soft dependencies", "Mark each call as hard (cannot work without it) or soft (can degrade). Make soft whatever you can: cached tokens, default values or reduced features.", "Check the chains: A calls B calls {dependency}."],
            ["Protection patterns", "Use timeouts shorter than the caller's own, retries with limits, circuit breakers, bulkheads and a cached last-known-good response.", "Test each pattern by switching the dependency off in a drill, not just by reading the code."],
            ["Redundancy", "Run the dependency across zones and, if the cost of an outage justifies it, across regions. A single region is a single point of failure.", "Compare the cost of redundancy with the yearly expected loss."],
            ["Priority", "Fix the {no_fallback} callers with no fallback first, starting with the ones on the checkout and login paths.", "Track the number of hard dependencies on shared services as a risk metric."],
        ],
        "metrics": ["Expected yearly loss from outages (USD)|hourly_revenue * outage_hours|${:,.0f}", "Share of callers with no fallback|no_fallback / callers|{:.0%}"],
    },
    "03-devops-sre/17-deploy-freeze-advisor": {
        "fields": ["event|Event or period|text|Black Friday week", "queued|Changes queued|number|31", "budget_left|Error budget left (percent)|number|38", "incidents|Incidents in the last 7 days|number|2", "risky_share|Share of queued changes that are high risk (0 to 1)|number|0.25"],
        "sections": [
            ["Situation", "Calendar: {input}", "Period: {event}. {queued} changes queued, {budget_left} percent of the error budget left, {incidents} recent incidents.", "A freeze trades speed for safety. Use it when the cost of an incident is much higher than the cost of waiting."],
            ["Decision rule", "Freeze everything but fixes when the budget is below 25 percent or a major event starts in less than 48 hours. Allow low-risk changes through a fast lane otherwise.", "Document who can approve an exception and what it needs: rollback plan, on-call aware, a flag to disable."],
            ["Risk of the queue", "High-risk changes (schema, auth, payments, infrastructure) deserve a review even outside a freeze. Count how many of the queue fall in this group.", "Many small changes are safer than one big batch after the freeze, so release the backlog in stages."],
            ["During the freeze", "Keep the deploy pipeline working, allow security patches and reverts, add extra on-call cover and run a daily check on the error budget.", "Announce the start and end dates to every team."],
            ["After the freeze", "Release the backlog gradually, watch the error budget and review whether the freeze prevented incidents or only delayed work.", "If you freeze often, fix the release process instead."],
        ],
        "metrics": ["High-risk changes in the queue|queued * risky_share|{:,.0f}", "Error budget burned so far (percent)|100 - budget_left|{:.0f}"],
    },
    "03-devops-sre/18-log-retention-tuner": {
        "fields": ["app_tb|Application logs per month (TB)|number|40", "app_days|Application log retention now (days)|number|90", "needed_days|Days you actually search back|number|21", "price_tb|Storage cost per TB per month (USD)|number|23", "compliance|Compliance requirement|text|Audit logs 7 years, access logs 1 year"],
        "sections": [
            ["Volumes today", "Volumes: {input}", "Application logs: {app_tb} TB per month kept {app_days} days. Compliance: {compliance}.", "Keep each class as long as it is useful or required, and no longer. Retention is a cost and a risk."],
            ["Classify the logs", "Audit and security logs: keep per the rule. Access logs: moderate. Application logs: short. Debug logs: very short.", "Write the retention for each class into a policy and set it in the tooling, not by hand."],
            ["Tier the storage", "Keep recent logs in hot searchable storage, move older ones to cheap object storage and index only what you search.", "People rarely search past {needed_days} days: check your query history before choosing."],
            ["Compliance and deletion", "Where the law requires deletion (personal data), delete on schedule and prove it. Where it requires retention, store immutable copies with access controls.", "Keep personal data out of logs to avoid the conflict."],
            ["Savings", "Cut retention for application logs from {app_days} to a value just above what you search, and sample or drop debug logs.", "Review the policy yearly and after any change in the rules."],
        ],
        "metrics": ["Stored volume today (TB)|app_tb * app_days / 30|{:,.0f}", "Stored volume at the searched window (TB)|app_tb * needed_days / 30|{:,.0f}", "Monthly saving on application logs (USD)|app_tb * (app_days - needed_days) / 30 * price_tb|${:,.0f}"],
    },
    "03-devops-sre/19-dns-change-verifier": {
        "fields": ["hostname|Hostname|text|api.example.com", "ttl_s|Current TTL (seconds)|number|3600", "low_ttl_s|TTL you will set before the change (seconds)|number|60", "traffic_rps|Requests per second to this name|number|1200", "lead_h|Hours before the change you lower the TTL|number|2"],
        "sections": [
            ["Change under review", "Change: {input}", "Hostname: {hostname}. Current TTL: {ttl_s} seconds.", "DNS is cached by resolvers you do not control, so a change reaches different users at different times."],
            ["Lower the TTL first", "Lower the TTL to {low_ttl_s} seconds at least {lead_h} hours before the change, and always longer than the old TTL, so caches expire the long TTL first.", "Restore a higher TTL a day after the change is stable."],
            ["Cutover", "Prefer weighted records or a canary share first. Keep the old target running and serving until traffic has drained.", "Do not delete the old endpoint for at least the old TTL plus a safety margin."],
            ["Verification", "Query the authoritative servers and several public resolvers, check the certificate and the health checks on the new target, and watch traffic on both sides.", "Check records you did not intend to touch, especially MX, SPF and TXT."],
            ["Rollback", "Keep the old record values written down. Rollback is the same change in reverse and takes the TTL to take effect, so keep the TTL low until you are sure.", "Name who can change DNS during the window and who decides to roll back."],
        ],
        "metrics": ["Minutes for the old TTL to expire everywhere|ttl_s / 60|{:,.0f}", "Requests that may still hit the old target during the lowered TTL|traffic_rps * low_ttl_s|{:,.0f}"],
    },
    "03-devops-sre/20-error-budget-policy-writer": {
        "fields": ["service|Service|text|Checkout API", "slo|SLO target (percent)|number|99.9", "window_days|Window (days)|number|30", "used_share|Share of budget used last window (0 to 1)|number|0.8", "owner|Policy owner|text|Head of engineering and head of product"],
        "sections": [
            ["Context", "Context: {input}", "Service: {service}. SLO: {slo} percent over {window_days} days. Owners: {owner}.", "An error budget turns the SLO into a shared allowance for failure. When it is spent, reliability work takes priority."],
            ["Thresholds", "Above 50 percent left: ship normally. Between 25 and 50: ship with extra review and canaries. Below 25: only fixes and reliability work. At zero: freeze features until the budget recovers.", "Agree the numbers with product before an incident, not during one."],
            ["What counts", "Count outages and errors users see. Exclude planned maintenance announced in advance and failures caused by a customer's own system.", "Measure from the user's side where you can, such as the load balancer or a synthetic check."],
            ["Escalation", "If product and engineering disagree on a freeze, escalate to the named owners within one business day. Record every exception and its cost.", "Review the SLO itself if you either never or always exhaust the budget."],
            ["Review", "Review the policy each quarter with burn charts, the incidents behind them and the releases delayed.", "Publish the budget status where product managers will see it weekly."],
        ],
        "metrics": ["Budget in minutes per window|(1 - slo / 100) * window_days * 24 * 60|{:,.0f}", "Minutes of downtime used last window|(1 - slo / 100) * window_days * 24 * 60 * used_share|{:,.0f}", "Minutes left|(1 - slo / 100) * window_days * 24 * 60 * (1 - used_share)|{:,.0f}"],
    },
}
