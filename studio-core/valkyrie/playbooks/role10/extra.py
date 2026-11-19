"""Playbooks for the FinOps & Cloud Cost agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "10-finops-cloud-cost/11-commitment-coverage-checker": {
        "fields": ["spend|Monthly eligible compute spend (USD)|number|410000", "coverage|Share covered by commitments (0 to 1)|number|0.52", "steady|Share of spend that is steady (0 to 1)|number|0.7", "discount|Discount on committed usage (0 to 1)|number|0.3", "utilization|Commitment utilization (0 to 1)|number|0.97"],
        "sections": [
            ["Usage", "Usage: {input}", "{spend} USD a month, {coverage} covered, {steady} steady, utilization {utilization}.", "Commitments trade flexibility for a lower price. Cover the steady base, leave the variable part on demand."],
            ["Coverage target", "Aim to cover about 80 percent of the steady baseline, since you can adjust later but cannot cancel. Coverage above the baseline risks paying for unused hours.", "Use the lowest hourly usage over 3 months as the floor."],
            ["Utilization", "Utilization below 95 percent means you pay for hours you do not use. Check the commitments that expire next and match them to the real baseline.", "Prefer flexible plans over instance-specific ones when your fleet changes often."],
            ["Where to add", "The gap between current coverage and the steady baseline is the room to add. Buy in steps, for example a quarter of the gap each month, and watch utilization after each step.", "Stagger terms so not everything expires at once."],
            ["Governance", "Assign one owner, review monthly, keep a calendar of expiries and decide in advance to renew, resize or let lapse.", "Track effective savings rate, not only coverage."],
        ],
        "metrics": ["Steady spend not yet covered (USD per month)|spend * (steady - coverage)|${:,.0f}", "Saving from covering the gap (USD per month)|spend * (steady - coverage) * discount|${:,.0f}", "Wasted commitment (USD per month)|spend * coverage * (1 - utilization)|${:,.0f}"],
    },
    "10-finops-cloud-cost/12-spot-instance-advisor": {
        "fields": ["vcpu_total|vCPU in scope|number|380", "vcpu_tolerant|vCPU that tolerate interruption|number|180", "on_demand_hour|On-demand price per vCPU-hour (USD)|number|0.04", "spot_discount|Spot discount (0 to 1)|number|0.65", "hours_month|Hours per month the workloads run|number|730"],
        "sections": [
            ["Workloads", "Profile: {input}", "{vcpu_total} vCPU in scope, {vcpu_tolerant} tolerate interruption.", "Spot capacity is spare cloud capacity at a deep discount, and it can be taken back with two minutes' notice."],
            ["What fits", "Fits: batch jobs, CI runners, rendering, stateless workers behind a queue and the stateless part of a web tier with spare capacity. Does not fit: databases, single-instance services and work that cannot restart.", "The test is simple: can the work stop at any moment and resume elsewhere."],
            ["Design for interruption", "Handle the termination notice by draining, checkpoint long jobs and make tasks idempotent. Use several instance types and zones so one pool drying up does not stop you.", "Keep a minimum on-demand base so the service stays up."],
            ["Tooling", "Use an autoscaling group with a mixed instances policy, or a cluster autoscaler with spot node groups, and a capacity-optimised allocation strategy.", "Alert on interruption rate and on jobs that restart often."],
            ["Roll out", "Start with CI and batch, measure interruptions and savings for a month, then move stateless services in steps.", "Report savings against the on-demand baseline."],
        ],
        "metrics": ["On-demand cost of the tolerant workloads (USD per month)|vcpu_tolerant * on_demand_hour * hours_month|${:,.0f}", "Saving on spot (USD per month)|vcpu_tolerant * on_demand_hour * hours_month * spot_discount|${:,.0f}", "Share of vCPU that fits spot|vcpu_tolerant / vcpu_total|{:.0%}"],
    },
    "10-finops-cloud-cost/13-cross-az-traffic-analyst": {
        "fields": ["tb_month|Cross-zone traffic per month (TB)|number|900", "price_gb|Price per GB crossing a zone (USD)|number|0.02", "avoidable|Share of it you can keep in one zone (0 to 1)|number|0.5", "replication_tb|Replication traffic you must keep (TB)|number|140", "zones|Zones in use|number|3"],
        "sections": [
            ["Traffic", "Matrix: {input}", "{tb_month} TB a month crosses zones at {price_gb} USD per GB. Zones: {zones}.", "Traffic within a zone is free and traffic between zones is billed in both directions on most clouds."],
            ["Where it comes from", "Service-to-service calls spread across zones, database replicas read from another zone, load balancers that spread evenly and replication between brokers. List the top sources by volume.", "Use flow logs and a cost allocation view to see them."],
            ["Locality fixes", "Turn on zone-aware routing in the mesh and load balancer, schedule chatty services together with pod affinity and read from a replica in the same zone.", "Keep enough capacity in each zone so that locality does not cause overload."],
            ["What to keep", "Replication across zones is the price of availability. {replication_tb} TB a month is deliberate, so reduce it only through compression and batching.", "Never trade away high availability for savings without a decision."],
            ["Verify", "Track cross-zone gigabytes per request and per service weekly and check latency improved, since local calls are also faster.", "Add the check to design reviews for new services."],
        ],
        "metrics": ["Monthly cost of cross-zone traffic (USD)|tb_month * 1000 * price_gb|${:,.0f}", "Saving from locality (USD per month)|tb_month * avoidable * 1000 * price_gb|${:,.0f}", "Traffic that is deliberate replication|replication_tb / tb_month|{:.0%}"],
    },
    "10-finops-cloud-cost/14-tagging-policy-auditor": {
        "fields": ["resources|Resources|number|12400", "with_owner|Resources with an owner tag|number|8804", "with_cost_center|Resources with a cost center tag|number|7192", "monthly_spend|Monthly cloud spend (USD)|number|620000", "untagged_spend|Spend on untagged resources (USD per month)|number|114000"],
        "sections": [
            ["Coverage", "Tags: {input}", "{resources} resources. Untagged spend: {untagged_spend} USD of {monthly_spend} USD a month.", "Tags turn a cloud bill into answers: who spends what, and on which product."],
            ["Required keys", "Require a short, fixed set: owner, cost-center, environment, application and data-classification. Define the allowed values and the format once, in a policy document.", "More than ten required keys will not be maintained."],
            ["Consistency", "Normalise case and spelling (prod, production, PRD) with a list of allowed values. Fix the existing resources with a script and check the result.", "Use tag policies and infrastructure-as-code modules that add the tags by default."],
            ["Enforcement", "Block creation of resources without required tags where the platform supports it and report weekly on the rest to each owner. Inherit tags from the account or project when you can.", "Give untagged spend its own line in the report so someone feels the cost."],
            ["Allocation", "Use tags and account structure for showback, and a rule for shared costs that cannot be tagged (networking, support). Review ownership every quarter since people change teams.", "Track tag coverage by spend, not by resource count."],
        ],
        "metrics": ["Owner tag coverage|with_owner / resources|{:.0%}", "Cost center tag coverage|with_cost_center / resources|{:.0%}", "Share of spend that is untagged|untagged_spend / monthly_spend|{:.0%}"],
    },
    "10-finops-cloud-cost/15-chargeback-allocator": {
        "fields": ["shared_total|Shared cost per month (USD)|number|186000", "team_usage|This team's share of the main usage driver (0 to 1)|number|0.22", "team_name|Team|text|Payments", "direct_cost|The team's direct cloud cost (USD per month)|number|95000", "fixed_share|Share of shared cost split evenly as a platform fee (0 to 1)|number|0.2", "teams|Teams sharing the platform|number|6"],
        "sections": [
            ["Costs to allocate", "Costs: {input}", "{shared_total} USD of shared cost a month. Team: {team_name}, direct cost {direct_cost} USD, {team_usage} of usage.", "Allocation should drive good behaviour and be easy to explain. Perfect precision is not the goal."],
            ["Choose drivers", "Use a measurable driver for each pool: requests or CPU for Kubernetes, bytes for networking, ingest volume for observability and headcount or tickets for support.", "A driver the team can influence changes behaviour. A flat split does not."],
            ["Platform fee", "Charge {fixed_share} of shared cost evenly as a base fee for the platform everyone needs, and the rest by usage.", "Review the split once a year, never mid-quarter."],
            ["Showback first", "Show the numbers for two or three months before charging, so teams can question and fix them. Publish the method and the data behind each line.", "Handle disputes with a simple process and a deadline."],
            ["Use the results", "Report total cost per team (direct plus allocated), unit cost per customer or request and trends. Use it in planning, not as a punishment.", "Revisit drivers when architecture changes."],
        ],
        "metrics": ["Even platform fee per team (USD)|shared_total * fixed_share / teams|${:,.0f}", "Usage-based share for this team (USD)|shared_total * (1 - fixed_share) * team_usage|${:,.0f}", "Total cost including allocation (USD)|direct_cost + shared_total * (1 - fixed_share) * team_usage + shared_total * fixed_share / teams|${:,.0f}"],
    },
    "10-finops-cloud-cost/16-database-cost-tuner": {
        "fields": ["db_monthly|Database spend (USD per month)|number|58000", "cpu_util|Average CPU utilization (0 to 1)|number|0.18", "right_size_saving|Saving from one size smaller (0 to 1)|number|0.4", "dev_monthly|Spend on dev and staging databases (USD per month)|number|14000", "off_hours_share|Share of the week they could be off (0 to 1)|number|0.65"],
        "sections": [
            ["Usage", "Usage: {input}", "{db_monthly} USD a month. Average CPU {cpu_util}. Dev and staging: {dev_monthly} USD.", "Databases are often over-provisioned because resizing feels risky. Measure, then change in small steps."],
            ["Right-size", "At low CPU, move down one instance size at a time during a quiet period, watch latency, connections and memory for a week and keep the option to roll back.", "Check peaks, not only averages, and memory pressure before cutting."],
            ["Storage and IOPS", "Provisioned IOPS above need is pure waste: move to a storage type with a baseline that fits or lower the setting. Delete unused indexes and old data, and archive cold partitions.", "Compression and partitioning reduce storage and IO."],
            ["Environments", "Stop dev and staging databases outside working hours with a schedule, use smaller sizes and snapshot-and-restore for rarely used copies.", "Delete abandoned databases after a notice period."],
            ["Replicas and backups", "Keep the replicas you need for availability and reads, not by habit. Set backup retention by policy and move older snapshots to cheaper storage.", "Check the cost of cross-region copies."],
        ],
        "metrics": ["Saving from right-sizing (USD per month)|db_monthly * right_size_saving|${:,.0f}", "Saving from stopping dev and staging off hours (USD per month)|dev_monthly * off_hours_share|${:,.0f}", "Total saving (USD per month)|db_monthly * right_size_saving + dev_monthly * off_hours_share|${:,.0f}"],
    },
    "10-finops-cloud-cost/17-observability-cost-reducer": {
        "fields": ["bill|Monthly observability bill (USD)|number|96000", "log_share|Share of the bill from logs (0 to 1)|number|0.5", "debug_share|Share of log volume that is debug (0 to 1)|number|0.4", "series_unused|Share of metric series never queried (0 to 1)|number|0.4", "trace_sample|Share of traces now kept (0 to 1)|number|1"],
        "sections": [
            ["Bill", "Volumes: {input}", "{bill} USD a month. Logs are {log_share} of it.", "Keep the data that answers questions during incidents, and stop paying for what nobody reads."],
            ["Logs", "Cut debug logs in production ({debug_share} of volume), drop noisy health-check lines, sample repeated errors and set retention by class. Route low-value logs to cheap storage instead of the search index.", "Check with each team before dropping a source."],
            ["Metrics", "Find high-cardinality labels (user id, request id) and remove them. Delete series never queried in the dashboards or alerts, and lower the scrape interval for slow-moving metrics.", "Cardinality, not volume of points, drives most metric cost."],
            ["Traces", "Keep {trace_sample} of traces today. Use tail-based sampling that keeps all errors and slow requests and a small share of normal ones.", "Keep full traces for the critical paths."],
            ["Governance", "Show each team its own telemetry cost, set budgets, and review the top ten cost drivers monthly. Negotiate commitments with the vendor after usage is trimmed, not before.", "Track cost per request as a unit metric."],
        ],
        "metrics": ["Log cost (USD per month)|bill * log_share|${:,.0f}", "Saving from cutting debug logs (USD per month)|bill * log_share * debug_share|${:,.0f}", "Non-log spend that goes on unused metric series (USD per month)|bill * (1 - log_share) * series_unused|${:,.0f}"],
    },
    "10-finops-cloud-cost/18-forecast-variance-explainer": {
        "fields": ["forecast|Forecast (USD)|number|1200000", "actual|Actual (USD)|number|1380000", "volume_effect|Variance from higher usage (USD)|number|108000", "one_off|One-off items (USD)|number|40000", "price_effect|Variance from price and discounts (USD)|number|32000"],
        "sections": [
            ["Variance", "Summary: {input}", "Forecast {forecast} USD, actual {actual} USD.", "A good variance story separates what happened (volume), what it cost (price), what changed (mix) and what will not repeat (one-offs)."],
            ["Decompose", "Break the gap into volume (more usage), price (rates, discounts, credits), mix (shift to costlier services or regions) and one-offs. Check that the pieces add up to the total.", "State the effect of each in dollars and in percent of forecast."],
            ["Interpret", "A volume effect of {volume_effect} USD may be healthy if revenue grew with it. Compare with unit cost per customer or per request.", "One-offs of {one_off} USD should not change the run rate."],
            ["Price effects", "Check the commitment coverage, expiring credits, list price changes and exchange rates. {price_effect} USD came from price and discounts.", "Ask whether the forecast assumed discounts that were not yet in place."],
            ["Action", "Update the forecast run rate without one-offs, fix the assumptions that missed and agree actions with owners for any avoidable part.", "Share the story with finance in one page and the same format each month."],
        ],
        "metrics": ["Total variance (USD)|actual - forecast|${:,.0f}", "Variance as a share of forecast|(actual - forecast) / forecast|{:+.1%}", "Variance not explained yet (USD)|actual - forecast - volume_effect - one_off - price_effect|${:,.0f}"],
    },
    "10-finops-cloud-cost/19-saas-license-optimizer": {
        "fields": ["seats|Seats purchased|number|480", "active_share|Share of seats active in 90 days (0 to 1)|number|0.61", "seat_price|Price per seat per year (USD)|number|420", "renewal_days|Days to renewal|number|70", "buffer|Spare seats you want to keep (0 to 1)|number|0.1"],
        "sections": [
            ["Licences", "Usage: {input}", "{seats} seats at {seat_price} USD, {active_share} active. Renewal in {renewal_days} days.", "Pay for people who use the tool. Seats go unused because accounts are never removed when people leave or change roles."],
            ["Find waste", "List accounts with no activity for 90 days, accounts of people who left and users on a higher tier than their activity needs. Ask managers to confirm before removing.", "Use your identity provider to automate removals when someone leaves."],
            ["Right-size the contract", "Renew for the active seats plus a buffer of {buffer}. Ask for a lower tier where features are not used and for the right to reduce seats at the anniversary.", "Do this well before the notice date: some contracts auto-renew."],
            ["Negotiate", "Use the usage data, a competitor quote and a longer term for a better price per seat. Avoid committing to growth you have not planned.", "Ask for a true-up (pay later for extra seats) instead of paying now."],
            ["Keep it clean", "Review usage every quarter, tie seat requests to a manager approval and record owners and renewal dates for every tool in one list.", "Reclaim seats automatically after 60 days of inactivity."],
        ],
        "metrics": ["Active seats|seats * active_share|{:,.0f}", "Seats to renew with a buffer|seats * active_share * (1 + buffer)|{:,.0f}", "Yearly saving from right-sizing (USD)|(seats - seats * active_share * (1 + buffer)) * seat_price|${:,.0f}"],
    },
    "10-finops-cloud-cost/20-gpu-utilization-analyst": {
        "fields": ["gpus|GPUs|number|64", "hourly_cost|Cost per GPU-hour (USD)|number|2.5", "utilization|Average utilization (0 to 1)|number|0.31", "idle_share|Share of GPU-hours idle between jobs (0 to 1)|number|0.22", "target_util|Target utilization (0 to 1)|number|0.6"],
        "sections": [
            ["Fleet", "Metrics: {input}", "{gpus} GPUs at {hourly_cost} USD an hour, utilization {utilization}, target {target_util}.", "Accelerators are the most expensive hardware you run, so idle time is the most expensive waste."],
            ["Find the idle time", "Split utilization into compute use, memory use and idle time between jobs. Low compute with high memory points to small batch sizes or data loading limits, not to a need for more GPUs.", "Check the input pipeline: slow data loading starves the GPU."],
            ["Scheduling", "Use a scheduler that packs jobs, supports gang scheduling and preemption, and shares GPUs (MIG or time slicing) for small jobs. Queue time and idle time both fall when scheduling improves.", "Give every team a quota and a priority class."],
            ["Buy or rent", "Reserve a base load for steady training and use spot or on-demand capacity for bursts. Do not buy more until utilization passes the target.", "Compare cost per training run or per million inferences across options."],
            ["Hygiene", "Shut down idle notebooks automatically, tag jobs with owner and project and report cost per team weekly.", "Set an alert when utilization drops below 20 percent for an hour."],
        ],
        "metrics": ["Monthly GPU cost (USD)|gpus * hourly_cost * 730|${:,.0f}", "Monthly cost of idle time (USD)|gpus * hourly_cost * 730 * idle_share|${:,.0f}", "GPUs needed at the target utilization|gpus * utilization / target_util|{:.0f}"],
    },
}
