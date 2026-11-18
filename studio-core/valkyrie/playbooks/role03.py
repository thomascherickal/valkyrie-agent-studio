"""Playbooks for the DevOps and SRE agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "03-devops-sre/01-incident-commander": {
        "fields": ["affected_pct|Share of users affected (percent)|number|18", "revenue_per_min|Normal revenue per minute (USD)|number|2500", "recent_change|Most recent change|text|Deploy #412 at 14:02 UTC", "responders|Responders on call|list|IC: Sam, Ops lead: Priya, Comms lead: Jo, Scribe: Lee", "update_min|Status update cadence (minutes)|number|30"],
        "sections": [
            ["Incident declaration", "Alert: {input}", "Impact: {affected_pct} percent of users. Last change: {recent_change}.", "Declare SEV-1 for customer-facing outage or data loss, SEV-2 for major degradation with a workaround. When unsure, declare high and downgrade later."],
            ["Roles", "*{responders}", "The Incident Commander coordinates and decides; they do not debug. Separate the Ops lead (hands on keyboard), Comms lead (status page, customers) and Scribe (timeline)."],
            ["First 15 minutes", "1. Open the incident channel and bridge. 2. State impact in one line. 3. Check the latest change and roll it back if it correlates in time. 4. Assign an owner and a deadline for every action. 5. Post the first external update.", "Mitigate before diagnosing: rollback, failover, feature flag off, scale up or shed load."],
            ["Communication cadence", "Internal and external updates every {update_min} minutes even when there is nothing new: say what is known, what is being done and when the next update comes.", "Escalate to executives at 30 minutes for SEV-1 without a mitigation in sight."],
            ["Exit and handoff", "Resolve only when the SLI is back to normal for 30 minutes. Hand over to a fresh IC after 4 hours. Schedule the blameless postmortem within 5 working days.", "Record the timeline in UTC with source links."],
        ],
        "metrics": ["Revenue at risk per hour|revenue_per_min * 60 * affected_pct / 100|${:,.0f}", "Status updates in the first 4 hours|240 / update_min|{:.0f}"],
    },
    "03-devops-sre/02-postmortem-author": {
        "fields": ["root_cause|Root cause in one line|text|No TTL on session keys let Redis fill its memory during the promo", "timeline|Timeline (one event per line)|longtext|14:02 Promo email sent\n14:20 Redis memory at 95%\n14:31 Alert fired\n15:37 Keys evicted, service restored", "customers_affected|Customers affected|number|12000", "duration_min|Incident duration (minutes)|number|95", "detect_min|Time to detect (minutes)|number|29"],
        "sections": [
            ["Summary", "Incident: {input}", "Root cause: {root_cause}", "Impact: {customers_affected} customers for {duration_min} minutes."],
            ["Timeline", "*{timeline}", "Use UTC, one line per event, and mark detection, escalation, mitigation and resolution."],
            ["Five whys", "Why did customers see errors? Why did that component fail? Why was it allowed to? Why did no safeguard catch it? Why did detection take {detect_min} minutes?", "Stop when you reach a process or design gap you can change. Avoid ending on 'human error'; ask what made the error easy."],
            ["Contributing factors", "Check each: missing limit or TTL, no capacity test for the promo, alert threshold too high, unclear ownership, unsafe default.", "Write findings about systems, never about named people (blameless)."],
            ["Action items", "Each ticket must be SMART: specific, measurable, with an owner and a date. Include one detect, one prevent and one mitigate item.", "Track completion; unfinished actions are the most common cause of repeat incidents."],
        ],
        "metrics": ["Customer-minutes of impact|customers_affected * duration_min|{:,.0f}", "Detection share of outage|detect_min / duration_min|{:.0%}"],
    },
    "03-devops-sre/03-terraform-reviewer": {
        "fields": ["environment|Target environment|text|production", "total_changes|Resources changed in the plan|number|14", "replaced|Resources marked for replacement|number|1", "destroyed|Resources marked for destroy|number|0", "state_backup|State backup and rollback|text|S3 versioned state, RDS snapshot taken 10 minutes ago"],
        "sections": [
            ["Plan summary", "Plan diff: {input}", "Environment: {environment}. {total_changes} changes, {replaced} replacements, {destroyed} destroys."],
            ["Destructive changes", "Any line marked -/+ or 'forces replacement' on a stateful resource (databases, volumes, buckets, queues) deletes data. Require a snapshot, a maintenance window and prevent_destroy on critical resources.", "Look for renamed resources: move them with a moved block or terraform state mv instead of letting Terraform destroy and recreate."],
            ["IAM and exposure", "Reject wildcard actions such as iam:* or Resource * on production. Scope to the exact actions and ARNs, add conditions, and flag new 0.0.0.0/0 ingress rules and public buckets.", "A policy that can edit IAM can grant itself anything: treat iam:* as admin."],
            ["Blast radius rules", "Block the apply if the plan changes more than 20 resources in one state, touches networking and compute together, or mixes unrelated teams' resources.", "Split large states by environment and domain, and apply with -target only in emergencies."],
            ["Safety net", "Rollback and state protection: {state_backup}", "Apply from CI with a saved plan file, require two approvals for production, and run policy checks (OPA, Checkov) before apply."],
        ],
        "metrics": ["Destructive share of the plan|(replaced + destroyed) / total_changes|{:.0%}"],
    },
    "03-devops-sre/04-k8s-manifest-linter": {
        "fields": ["workload|Workload name|text|checkout-api", "replicas|Replicas|number|3", "min_available|PodDisruptionBudget minAvailable|number|2", "cpu_request_m|CPU request per pod (millicores)|number|250", "mem_limit_mi|Memory limit per pod (MiB)|number|512"],
        "sections": [
            ["Manifest", "Spec: {input}", "Workload {workload} with {replicas} replicas, {cpu_request_m}m CPU requested, {mem_limit_mi} MiB limit."],
            ["Health probes", "Add a readinessProbe (gates traffic), a livenessProbe (restarts a stuck container, never check dependencies) and a startupProbe for slow starters. Set a sensible failureThreshold and timeoutSeconds.", "A missing readiness probe sends traffic to pods that are still booting."],
            ["Resources", "Every container needs requests and limits. Set memory request equal to limit; avoid CPU limits on latency-sensitive services because throttling hurts p99, but keep CPU requests accurate for scheduling.", "Empty resources means BestEffort QoS: the first pod evicted under pressure."],
            ["Availability", "Create a PodDisruptionBudget (minAvailable {min_available} of {replicas}) and spread replicas with topologySpreadConstraints across zones. A single replica cannot be drained without downtime.", "Set a rolling update with maxUnavailable 0 and maxSurge 25 percent for zero-downtime deploys."],
            ["Security", "Run as non-root with readOnlyRootFilesystem, drop all capabilities, set allowPrivilegeEscalation false, use a seccompProfile of RuntimeDefault and pin images by digest.", "Never use the latest tag, and use a dedicated ServiceAccount with automountServiceAccountToken off unless needed."],
        ],
        "metrics": ["Voluntary disruptions allowed|replicas - min_available|{:.0f}", "Total CPU requested (millicores)|replicas * cpu_request_m|{:,.0f}", "Total memory limit (MiB)|replicas * mem_limit_mi|{:,.0f}"],
    },
    "03-devops-sre/05-slo-burn-monitor": {
        "fields": ["slo_pct|SLO target (percent)|number|99.9", "err_1h_pct|Error rate over 1 hour (percent)|number|1.2", "err_6h_pct|Error rate over 6 hours (percent)|number|0.8", "budget_left_pct|Error budget remaining (percent)|number|18", "window_days|SLO window (days)|number|30"],
        "sections": [
            ["Inputs", "Metrics: {input}", "SLO {slo_pct} percent over {window_days} days; budget left {budget_left_pct} percent; 1h error rate {err_1h_pct} percent; 6h {err_6h_pct} percent."],
            ["Burn rate", "Burn rate = observed error rate / (100 - SLO). A burn rate of 1 uses exactly the whole budget over the window; 14.4 uses 2 percent of a 30-day budget in one hour.", "Always read the burn rate with a long and a short window so the alert resolves quickly after recovery."],
            ["Paging thresholds", "Page: burn above 14.4 over 1 hour and 5 minutes (2 percent of budget), or above 6 over 6 hours and 30 minutes (5 percent). Ticket: burn above 1 over 3 days.", "Below those, record it on the dashboard; do not wake anyone."],
            ["Budget policy", "Above 50 percent budget left: ship normally. 10 to 50 percent: extra review for risky changes. Under 10 percent: freeze feature launches and spend the time on reliability.", "Define who can override the freeze and record every override."],
            ["Follow-up", "Attribute budget burn to causes (deploys, dependencies, capacity) and review the top cause monthly.", "If the SLO is always green, it may be too loose; if always red, too strict or the service needs investment."],
        ],
        "metrics": ["Burn rate (1 hour)|err_1h_pct / (100 - slo_pct)|{:.1f}x", "Burn rate (6 hours)|err_6h_pct / (100 - slo_pct)|{:.1f}x", "Hours until budget is exhausted at the 1h burn|budget_left_pct / 100 * window_days * 24 / (err_1h_pct / (100 - slo_pct))|{:.1f}"],
    },
    "03-devops-sre/06-ci-pipeline-optimizer": {
        "fields": ["install_min|Install step (minutes)|number|4", "build_min|Build step (minutes)|number|9", "test_min|Test step (minutes)|number|1", "cache_gain_pct|Expected build saving from caching (percent)|number|70", "runs_per_day|Pipeline runs per day|number|60"],
        "sections": [
            ["Timings", "Observed: {input}", "Serial total {install_min} + {build_min} + {test_min} minutes per run, {runs_per_day} runs per day."],
            ["Cache fixes", "Cache dependencies keyed on the lockfile hash (actions/cache or setup-node cache). Use sccache or the Rust target directory cache with Swatinem/rust-cache. Use remote Docker layer caching with buildx.", "A cache miss on every run usually means the key includes a changing value such as the commit SHA."],
            ["Parallelism", "Run lint, unit tests and build as parallel jobs with needs only where truly dependent. Shard the test suite across a matrix by historical duration.", "The critical path is the longest dependent chain; shorten that first, not the shortest job."],
            ["Skip unneeded work", "Use path filters and a changed-files check so docs-only changes skip the build. Cancel superseded runs with concurrency groups.", "Move slow end-to-end tests to merge-queue or nightly if they exceed 10 minutes."],
            ["Target", "Aim for pull request feedback in under 10 minutes; developer flow breaks above that. Track p50 and p90 pipeline time and the flaky-rerun rate weekly.", "Beware of larger runners that only hide a serial design."],
        ],
        "metrics": ["Time saved per run (minutes)|build_min * cache_gain_pct / 100|{:.1f}", "Pipeline time after caching (minutes)|install_min + build_min * (1 - cache_gain_pct / 100) + test_min|{:.1f}", "Runner-minutes saved per month|build_min * cache_gain_pct / 100 * runs_per_day * 22|{:,.0f}"],
    },
    "03-devops-sre/07-capacity-planner": {
        "fields": ["current_qps|Current peak QPS|number|4000", "cpu_now_pct|CPU utilization at peak now (percent)|number|62", "forecast_qps|Forecast peak QPS|number|9500", "instances_now|Instances now|number|12", "target_cpu_pct|Target peak CPU (percent)|number|60"],
        "sections": [
            ["Demand", "Forecast: {input}", "Peak {current_qps} QPS at {cpu_now_pct} percent CPU now; forecast {forecast_qps} QPS."],
            ["Headroom model", "Assume CPU scales roughly linearly with QPS until saturation, then latency climbs sharply. Plan to peak CPU of 60 percent so that losing one zone (N+1) or a traffic spike does not exceed 80 percent.", "Validate linearity with a load test; memory, connection pools and downstream databases often saturate before CPU."],
            ["Scaling plan", "Compute instances needed = current instances x projected CPU / target CPU. Round up and add N+1 for the largest failure domain.", "Prefer autoscaling on a leading signal (queue depth, requests per instance) with a minimum floor for the peak."],
            ["Dependencies", "Check the database, cache, message broker and third-party rate limits against the same forecast. The slowest-scaling component sets the date.", "Order long-lead items (reserved instances, quota increases) at least 8 weeks ahead."],
            ["Review cadence", "Re-forecast monthly using the p95 growth rate of the last 90 days. Alert when projected CPU breaches the target within 60 days.", "Record forecast versus actual to improve the model."],
        ],
        "metrics": ["Projected CPU with no scaling|cpu_now_pct * forecast_qps / current_qps|{:.0f}%", "Instances needed at target CPU|instances_now * cpu_now_pct * forecast_qps / (current_qps * target_cpu_pct)|{:.1f}", "Additional instances|instances_now * cpu_now_pct * forecast_qps / (current_qps * target_cpu_pct) - instances_now|{:.1f}"],
    },
    "03-devops-sre/08-runbook-generator": {
        "fields": ["service|Service and owner|text|Orders Postgres, owned by the Platform team", "max_connections|max_connections setting|number|500", "threshold_pct|Alert threshold (percent)|number|85", "pooler|Connection pooler|text|PgBouncer in transaction mode", "escalation|Escalation path|text|Page the database on-call after 15 minutes, then the Platform lead"],
        "sections": [
            ["Alert", "Rule: {input}", "Service: {service}. Pooler: {pooler}."],
            ["Impact and triage", "The alert fires at {threshold_pct} percent of {max_connections} connections. At 100 percent new connections are refused and the application throws errors.", "First confirm it is real: check whether the connection count is rising or flat, and whether a deploy or batch job started."],
            ["Diagnostic commands", "SELECT state, count(*) FROM pg_stat_activity GROUP BY 1; to see idle versus active. SELECT pid, now() - xact_start, query FROM pg_stat_activity WHERE state <> 'idle' ORDER BY 2 DESC; to find long transactions.", "Look for idle in transaction sessions and connection leaks per application client; group by application_name."],
            ["Mitigation", "Fastest safe steps: pause the batch job, restart the leaking client, then terminate idle in transaction sessions older than 5 minutes with pg_terminate_backend. Raise the pooler pool size only after checking database CPU.", "Rollback: undo the last deploy or config change if the rise started with it."],
            ["Escalation and closure", "{escalation}", "After recovery set idle_in_transaction_session_timeout, add a client-side pool limit, and record the cause in the alert annotation."],
        ],
        "metrics": ["Connections at alert threshold|max_connections * threshold_pct / 100|{:,.0f}", "Connections left before saturation|max_connections * (100 - threshold_pct) / 100|{:,.0f}"],
    },
    "03-devops-sre/09-chaos-test-designer": {
        "fields": ["steady_state|Steady-state hypothesis|text|Checkout success rate stays at or above 99.5% and p95 latency under 400 ms", "rps|Normal requests per second|number|800", "blast_pct|Blast radius (percent of traffic)|number|5", "duration_min|Experiment duration (minutes)|number|15", "abort_rule|Abort condition|text|Checkout success rate below 98% for 2 minutes"],
        "sections": [
            ["Experiment target", "Target: {input}", "Steady state: {steady_state}"],
            ["Hypothesis", "State it as: when the fault is injected, the steady-state metric stays within bounds because of the failover or retry design.", "Run in staging first, then production at a small blast radius during business hours when engineers are present."],
            ["Fault design", "Choose one variable: instance kill, region or AZ blackhole, 200 to 500 ms latency injection, packet loss, dependency 5xx, expired certificate, clock skew. Ramp slowly.", "For failover, measure detection time, switchover time and data loss (RPO) separately."],
            ["Blast radius and safety", "Limit to {blast_pct} percent of traffic for {duration_min} minutes. Abort rule: {abort_rule}", "Have a one-command stop, an on-call observer and customer support informed before starting."],
            ["Analysis", "Compare the metric to the baseline, list surprises (alerts that did not fire, retries that amplified load), and file a fix for each.", "Repeat after fixes, then automate the drill as a quarterly game day."],
        ],
        "metrics": ["Requests exposed to the fault|rps * 60 * duration_min * blast_pct / 100|{:,.0f}", "Requests per minute in the blast radius|rps * 60 * blast_pct / 100|{:,.0f}"],
    },
    "03-devops-sre/10-rollback-verifier": {
        "fields": ["canary_p99|Canary p99 latency (ms)|number|420", "baseline_p99|Baseline p99 latency (ms)|number|95", "canary_err_pct|Canary error rate (percent)|number|0.9", "baseline_err_pct|Baseline error rate (percent)|number|0.2", "canary_traffic_pct|Canary traffic share (percent)|number|5"],
        "sections": [
            ["Canary readings", "Stats: {input}", "Canary p99 {canary_p99} ms versus baseline {baseline_p99} ms; errors {canary_err_pct} percent versus {baseline_err_pct} percent; canary gets {canary_traffic_pct} percent of traffic."],
            ["Gate thresholds", "Roll back automatically if p99 exceeds 1.2x baseline, if the error rate exceeds baseline by 0.5 points or 2x, or if any saturation metric (CPU, memory, queue) exceeds 85 percent.", "Compare the canary to a concurrently running baseline, not to yesterday's numbers, to cancel time-of-day effects."],
            ["Statistical care", "At 5 percent traffic the canary may see too few requests to trust a ratio. Require at least 1,000 requests and a 10-minute soak before judging error rates.", "Use a one-sided test or a Mann-Whitney check on latency; watch the whole distribution, not only the mean."],
            ["Decision", "Rollback on any breach; hold and extend soak on borderline readings; promote in steps 5, 25, 50, 100 percent only when every gate passes.", "Rollback itself is a deploy: confirm the previous version, database compatibility and feature flag state first."],
            ["After the decision", "Record the metrics, version and decision. For a rollback, open an issue with the failing signal and block the next promotion until it is fixed.", "Keep the previous version warm for at least one hour."],
        ],
        "metrics": ["p99 ratio (canary / baseline)|canary_p99 / baseline_p99|{:.1f}x", "Error rate delta (points)|canary_err_pct - baseline_err_pct|{:.2f}", "Error rate ratio|canary_err_pct / baseline_err_pct|{:.1f}x"],
    },
}
