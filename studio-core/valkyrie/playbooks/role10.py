"""Playbooks for the FinOps and Cloud Cost agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "10-finops-cloud-cost/01-cloud-bill-anomaly": {
        "fields": ["baseline|Normal daily cost (USD)|number|42", "current|Current daily cost (USD)|number|610", "days_since|Days since the spike began|number|3", "threshold_pct|Alert threshold above baseline (percent)|number|30", "recent_change|Recent change or launch|text|New batch export job launched on Monday"],
        "sections": [
            ["Spike", "Spend data: {input}", "Baseline {baseline} USD per day; now {current} USD; started {days_since} days ago. Recent change: {recent_change}."],
            ["Detect", "Flag when daily cost exceeds the baseline by {threshold_pct} percent and by an absolute floor (for example 50 USD) to avoid noise on tiny services. Baseline = median of the same weekday over 4 weeks.", "Use cost anomaly detection by service, region, account and cost-allocation tag at the same time."],
            ["Likely causes", "NAT Gateway: traffic to S3, ECR or APIs through NAT rather than VPC endpoints (0.045 USD per GB processed). Others: runaway autoscaling, a log level change, a retry storm, cross-region replication, data transfer out, and forgotten test clusters.", "Check CloudWatch BytesOutToDestination, flow logs and the top talkers."],
            ["Contain", "Stop the bleeding first: add S3 and DynamoDB gateway endpoints (free), cap autoscaling max, pause the job, and set a budget action. Then fix the root cause.", "Record the cost already incurred and ask the provider for credit for genuine mistakes."],
            ["Prevent", "Tag every resource with owner and cost centre, set budgets with alerts at 80 and 100 percent, and review the top 10 movers weekly.", "Add the launch checklist item: estimate the cost of any new data path."],
        ],
        "metrics": ["Spike multiple|current / baseline|{:.1f}x", "Excess cost per day|current - baseline|${:,.0f}", "Excess cost so far|(current - baseline) * days_since|${:,.0f}", "Projected monthly excess if unchecked|(current - baseline) * 30|${:,.0f}"],
    },
    "10-finops-cloud-cost/02-k8s-rightsizing-advisor": {
        "fields": ["request_vcpu|CPU requested per pod (vCPU)|number|4", "p95_vcpu|p95 CPU used per pod (vCPU)|number|0.45", "replicas|Replicas|number|6", "headroom_pct|Headroom above p95 (percent)|number|30", "vcpu_price|Price per vCPU-month (USD)|number|25"],
        "sections": [
            ["Workload", "Metrics: {input}", "{replicas} replicas requesting {request_vcpu} vCPU, p95 usage {p95_vcpu} vCPU."],
            ["Method", "Right-size requests from at least 14 days of data covering a peak: request = p95 usage x (1 + headroom), here {headroom_pct} percent headroom. Memory: request equal to limit near the p99 plus 20 percent, because memory is not compressible and over-commit causes OOM kills.", "Do not cut CPU on workloads with startup bursts without a startupProbe or a higher burst limit."],
            ["Apply safely", "Roll out the Vertical Pod Autoscaler in recommendation mode first, change one workload at a time, watch throttling (container_cpu_cfs_throttled_periods), restarts and p99 latency for a week.", "Never cut below the minimum needed for a node to schedule the pod."],
            ["After requests shrink", "Smaller requests only save money when nodes are consolidated: enable Cluster Autoscaler or Karpenter, use bin-packing and spot for stateless workloads.", "Track cluster allocation efficiency; healthy is above 60 percent of node CPU requested and above 40 percent used."],
            ["Governance", "Set LimitRanges and ResourceQuota per namespace, publish a monthly waste report per team, and require requests in the deployment template.", "Re-run each quarter as traffic changes."],
        ],
        "metrics": ["Utilisation of requested CPU|p95_vcpu / request_vcpu|{:.0%}", "Recommended request (vCPU)|p95_vcpu * (1 + headroom_pct / 100)|{:.2f}", "Monthly saving|(request_vcpu - p95_vcpu * (1 + headroom_pct / 100)) * replicas * vcpu_price|${:,.0f}"],
    },
    "10-finops-cloud-cost/03-idle-resource-reaper": {
        "fields": ["volume_tb|Unattached volumes (TB)|number|2.8", "gb_price|Volume price (USD per GB-month)|number|0.08", "idle_albs|Idle load balancers|number|3", "alb_price|Load balancer fixed cost (USD per month)|number|22", "zombie_vms|Zombie VMs|number|2", "vm_price|VM cost (USD per month)|number|70"],
        "sections": [
            ["Inventory", "Found: {input}", "{volume_tb} TB unattached, {idle_albs} idle load balancers, {zombie_vms} zombie VMs."],
            ["Idle criteria", "Volumes: unattached for 14 days or more. Load balancers: no healthy targets or under 100 requests per day for 14 days. VMs: CPU under 5 percent and network under 5 MB per day for 14 days, no recent logins. Check tags for owner and keep-until dates.", "Never delete on metrics alone; confirm with the owner."],
            ["Safe reaping", "Step 1 notify the owner and wait 7 days. Step 2 snapshot volumes and stop VMs rather than terminate. Step 3 delete after 30 more days with the snapshot as a backup. Keep a log of every deletion.", "Protect anything tagged do-not-delete or tied to compliance retention."],
            ["Hidden waste", "Old snapshots and AMIs, unused Elastic IPs (charged when idle), orphaned NAT gateways, dev databases running nights and weekends, empty ECR repositories with large images.", "Schedule non-production environments off outside working hours: about 65 percent saved."],
            ["Prevention", "Require owner and expiry tags, run the scan weekly, and publish a leaderboard by team.", "Automate: lifecycle policies for snapshots and a budget alert on idle-asset spend."],
        ],
        "metrics": ["Volumes monthly cost|volume_tb * 1000 * gb_price|${:,.0f}", "Load balancers monthly cost|idle_albs * alb_price|${:,.0f}", "Zombie VMs monthly cost|zombie_vms * vm_price|${:,.0f}", "Total monthly waste|volume_tb * 1000 * gb_price + idle_albs * alb_price + zombie_vms * vm_price|${:,.0f}"],
    },
    "10-finops-cloud-cost/04-ri-savings-planner": {
        "fields": ["od_monthly|On-demand monthly spend (USD)|number|4100", "baseline_vcpu|Steady baseline (vCPU)|number|120", "discount_pct|Savings Plan discount (percent)|number|27", "coverage_pct|Share of spend to commit (percent)|number|70", "min_usage_pct|Lowest observed usage vs baseline (percent)|number|85"],
        "sections": [
            ["Baseline", "Compute baseline: {input}", "{baseline_vcpu} vCPU steady; on-demand spend {od_monthly} USD per month."],
            ["Commit sizing", "Commit to the floor of your usage, not the average: look at the minimum hourly spend over 3 months. Commit about {coverage_pct} percent of baseline; leave room for rightsizing and Graviton migration, which reduce what you need.", "Rightsize before committing, otherwise you lock in waste."],
            ["Choosing the instrument", "Compute Savings Plans: flexible across instance family, region and Fargate/Lambda, 1-year no-upfront gives roughly 20 to 30 percent off. Reserved Instances: deeper discount for fixed families and convertible options. Standard 3-year gives the best discount but least flexibility.", "Start with 1-year no-upfront; layer 3-year only for truly permanent workloads."],
            ["Risk", "Break-even: the commit pays off if you use at least (1 - discount) of it. At a 27 percent discount you need 73 percent utilisation. Observed minimum usage: {min_usage_pct} percent.", "Stagger purchases monthly or quarterly so expirations are spread."],
            ["Governance", "Track coverage (target 60 to 80 percent) and utilisation (target above 95 percent) weekly; set an alert for utilisation below 90 percent.", "Assign a single owner for purchases and review them at renewal 60 days ahead."],
        ],
        "metrics": ["Committed spend share (on-demand equivalent)|od_monthly * coverage_pct / 100|${:,.0f}", "Monthly savings|od_monthly * coverage_pct / 100 * discount_pct / 100|${:,.0f}", "Annual savings|od_monthly * coverage_pct / 100 * discount_pct / 100 * 12|${:,.0f}", "Break-even utilisation|100 - discount_pct|{:.0f}%"],
    },
    "10-finops-cloud-cost/05-llm-token-optimizer": {
        "fields": ["tokens_m|Monthly tokens (millions)|number|500", "high_price|High-effort model price (USD per 1M tokens)|number|15", "low_price|Low-effort model price (USD per 1M tokens)|number|1", "simple_pct|Share of calls that are simple (percent)|number|70", "trim_pct|Prompt tokens removable by trimming (percent)|number|20"],
        "sections": [
            ["Usage", "Usage: {input}", "{tokens_m} million tokens per month at {high_price} USD per million on the high-effort model."],
            ["Routing", "Send classification, extraction, formatting and short Q and A to the low-effort tier; reserve the high tier for multi-step reasoning, long synthesis and code generation. Route with a cheap classifier or rules, with a fallback up to the high tier when confidence is low.", "Evaluate quality on a held-out set of 200 real prompts before switching; require at least 98 percent of baseline accuracy."],
            ["Trim prompts", "Remove repeated instructions, long few-shot examples (use two), verbose JSON schemas and unneeded context. Use structured outputs with short field names and set max_tokens.", "Enable prompt caching for the stable prefix; cached input often costs about 90 percent less."],
            ["Other levers", "Cache identical requests, batch non-urgent jobs through batch APIs (about 50 percent cheaper), truncate chat history with summaries, and cap retries.", "Output tokens cost 3 to 5 times input tokens, so shorten answers first."],
            ["Guardrails", "Track cost per task, quality score and latency per route; alert on spend per tenant. Re-test routing when models or prices change.", "Roll out gradually behind a flag."],
        ],
        "metrics": ["Current monthly cost|tokens_m * high_price|${:,.0f}", "Cost after routing and trimming|tokens_m * (1 - trim_pct / 100) * (simple_pct / 100 * low_price + (1 - simple_pct / 100) * high_price)|${:,.0f}", "Monthly saving|tokens_m * high_price - tokens_m * (1 - trim_pct / 100) * (simple_pct / 100 * low_price + (1 - simple_pct / 100) * high_price)|${:,.0f}"],
    },
    "10-finops-cloud-cost/06-egress-cost-reducer": {
        "fields": ["nat_tb|Traffic to S3 through NAT (TB per month)|number|18", "nat_price|NAT processing price (USD per GB)|number|0.045", "az_tb|Cross-AZ traffic (TB per month)|number|6", "az_price|Cross-AZ price, both directions (USD per GB)|number|0.02", "internet_tb|Internet egress (TB per month)|number|3"],
        "sections": [
            ["Traffic profile", "Flows: {input}", "{nat_tb} TB through NAT, {az_tb} TB cross-AZ, {internet_tb} TB to the internet per month."],
            ["Gateway endpoints", "S3 and DynamoDB gateway endpoints are free and remove the NAT processing charge on that traffic. Add a route table entry and an endpoint policy. Use interface endpoints (about 7 USD per month per AZ plus 0.01 per GB) for ECR, STS, Secrets Manager and other heavy services.", "This is usually the fastest, safest win."],
            ["Cross-AZ chatter", "Find chatty service pairs in flow logs. Fix with topology-aware routing (Kubernetes topology hints, zone-aware load balancing), co-locate chatty services, and read from replicas in the same AZ.", "Keep one AZ per replica only if availability needs allow; do not trade resilience for pennies."],
            ["Internet egress", "Put a CDN in front of public downloads (cheaper egress and caching), compress responses, and serve large artifacts from regional mirrors.", "Cross-region replication is egress too; replicate only what you must."],
            ["Verify", "Use VPC flow logs and Cost Explorer filtered on usage types (NatGateway-Bytes, DataTransfer-Regional-Bytes) before and after.", "Re-check monthly: new services re-create the leaks."],
        ],
        "metrics": ["NAT processing cost on S3 traffic|nat_tb * 1000 * nat_price|${:,.0f}", "Cross-AZ transfer cost|az_tb * 1000 * az_price|${:,.0f}", "Saving from an S3 gateway endpoint (per month)|nat_tb * 1000 * nat_price|${:,.0f}"],
    },
    "10-finops-cloud-cost/07-storage-tiering-planner": {
        "fields": ["size_tb|Data to tier (TB)|number|45", "std_price|Standard price (USD per GB-month)|number|0.023", "cold_price|Target tier price (USD per GB-month)|number|0.004", "objects_m|Objects (millions)|number|90", "transition_per_1k|Transition request price (USD per 1,000 objects)|number|0.05"],
        "sections": [
            ["Data set", "Bucket: {input}", "{size_tb} TB across {objects_m} million objects."],
            ["Pick the tier", "Unknown or changing access: Intelligent-Tiering (automatic, small monitoring fee per object, skips objects under 128 KB). Known cold logs: lifecycle to Glacier Instant Retrieval at 90 days when accessed quarterly, Glacier Flexible at 180 days, Deep Archive at 365 days for compliance.", "Check retrieval needs and minimum storage durations (90 or 180 days) before moving."],
            ["Cost trap: small objects", "Transition requests are billed per object, and tiny objects can cost more to move than to keep. Compact small log files into larger archives (for example hourly gzip bundles of 128 MB or more) before transition.", "Average object size here: see the figures below."],
            ["Lifecycle rule", "Write: filter by prefix logs/, transition to the target tier after 90 days, expire after the retention period (for example 400 days), abort incomplete multipart uploads after 7 days and expire noncurrent versions after 30.", "Test on one prefix first and compare the bill after a full cycle."],
            ["Risk", "Retrieval fees and delays: Glacier Flexible takes minutes to hours. Keep an index of what is archived and tell users the retrieval time.", "Enable storage lens to find buckets that never get read."],
        ],
        "metrics": ["Current monthly cost|size_tb * 1000 * std_price|${:,.0f}", "Monthly cost after tiering|size_tb * 1000 * cold_price|${:,.0f}", "Monthly saving|size_tb * 1000 * (std_price - cold_price)|${:,.0f}", "One-time transition cost|objects_m * 1000 * transition_per_1k|${:,.0f}", "Payback (months)|objects_m * 1000 * transition_per_1k / (size_tb * 1000 * (std_price - cold_price))|{:.1f}", "Average object size (KB)|size_tb * 1000000000 / (objects_m * 1000000)|{:,.0f}"],
    },
    "10-finops-cloud-cost/08-unit-economics-tracker": {
        "fields": ["infra|Monthly infrastructure cost (USD)|number|3200", "llm|Monthly LLM cost (USD)|number|480", "runs_m|Agent runs per month (millions)|number|1.6", "tenants|Active tenants|number|400", "revenue|Monthly recurring revenue (USD)|number|48000"],
        "sections": [
            ["Inputs", "Cost data: {input}", "Infra {infra} USD, LLM {llm} USD, {runs_m} million runs, {tenants} tenants, revenue {revenue} USD."],
            ["Definitions", "COGS per tenant = (infra + LLM + support tooling + payment fees) / active tenants. COGS per 1,000 runs = COGS / runs x 1,000. Include only costs that scale with usage; keep R and D and sales out of COGS.", "Define an active tenant (one run in the last 30 days) and keep it fixed."],
            ["Margin targets", "SaaS gross margin 75 to 80 percent; AI products often 55 to 70 percent. Below 50 percent, change pricing, caching or model routing.", "Look at the distribution: the top 10 percent of tenants usually drive most of the cost."],
            ["Segmentation", "Compute unit cost per plan and per tenant size; find tenants with negative margin and decide: reprice, cap or move to usage pricing.", "Allocate shared costs by usage drivers (runs, storage), not evenly."],
            ["Tracking", "Publish monthly with trend lines, split fixed from variable cost, and show forecast at 2x volume.", "Tie each cost to a tag or account so the numbers reconcile with the invoice."],
        ],
        "metrics": ["COGS per tenant|(infra + llm) / tenants|${:,.2f}", "COGS per 1,000 runs|(infra + llm) / (runs_m * 1000)|${:,.2f}", "Gross margin|(revenue - infra - llm) / revenue|{:.1%}", "Revenue per tenant|revenue / tenants|${:,.0f}"],
    },
    "10-finops-cloud-cost/09-budget-alert-router": {
        "fields": ["budget|Monthly budget (USD)|number|20000", "spent|Spent so far (USD)|number|17600", "day|Day of the month|number|14", "days_in_month|Days in the month|number|30", "owner|Budget owner and channel|text|Data-Eng squad lead, #data-eng-finops, data-eng@example.com"],
        "sections": [
            ["Status", "Budget status: {input}", "{spent} of {budget} USD spent on day {day} of {days_in_month}. Owner: {owner}."],
            ["Forecast", "Linear run-rate forecast = spent / days elapsed x days in month. Use a seasonality-aware forecast if the workload is spiky, and compare both. Alert on forecast, not only on actual spend.", "Thresholds: 80 percent of forecast above budget is a warning; 100 percent is a page to the owner; actual spend above 100 percent escalates to the director."],
            ["Routing", "Send to the squad Slack channel and owner by email; add the finance partner when the forecast exceeds budget by more than 10 percent; page only for runaway spend that can double within 24 hours.", "Include in every alert: forecast, overrun amount, top three cost drivers, change since last week and a link to the dashboard."],
            ["Action menu", "Pause non-production jobs, scale down dev clusters, schedule heavy batch jobs off-peak, rightsize, or request a budget increase with a reason.", "The owner acknowledges within one business day; unacknowledged alerts escalate."],
            ["Hygiene", "Tag-based allocation must cover 95 percent of spend or the squad budgets are meaningless. Review budgets quarterly.", "Suppress duplicates: one alert per threshold per month."],
        ],
        "metrics": ["Budget used|spent / budget|{:.0%}", "Forecast month-end spend|spent / day * days_in_month|${:,.0f}", "Forecast overrun|spent / day * days_in_month - budget|${:,.0f}", "Daily spend allowed to stay on budget|(budget - spent) / (days_in_month - day)|${:,.0f}"],
    },
    "10-finops-cloud-cost/10-finops-monthly-brief": {
        "fields": ["total|Total cloud spend this month (USD)|number|24500", "mom_pct|Change versus last month (percent)|number|-9", "savings|Savings realised this month (USD)|number|4200", "revenue|Revenue this month (USD)|number|98000", "coverage_pct|Commitment coverage (percent)|number|68"],
        "sections": [
            ["Headline", "Ledger: {input}", "Total spend {total} USD, {mom_pct} percent versus last month; savings realised {savings} USD."],
            ["Variance explanation", "Break the change into volume (usage growth), rate (discounts, commitments, price changes) and mix (service shift). Name the top three movers and the reason for each.", "Separate one-time items (credits, true-ups) from run-rate changes."],
            ["Savings", "Report realised savings (already in the bill) separately from identified savings (in the pipeline). Count only validated changes and avoid double counting.", "Show the cumulative total year to date against the annual target."],
            ["Unit economics", "Show cloud cost as a percent of revenue (target under 15 for SaaS, under 25 for AI heavy) and cost per active tenant, with a trend.", "Commitment coverage {coverage_pct} percent: target 60 to 80 percent coverage and above 95 percent utilisation."],
            ["Next month", "List three actions with owners and expected dollar impact, plus the forecast and risk (launches, migrations, renewals).", "Keep the brief to one page."],
        ],
        "metrics": ["Last month spend|total / (1 + mom_pct / 100)|${:,.0f}", "Change in spend|total - total / (1 + mom_pct / 100)|{:+,.0f} USD", "Savings as a share of the spend without savings|savings / (total + savings)|{:.1%}", "Cloud cost as a share of revenue|total / revenue|{:.1%}"],
    },
}
