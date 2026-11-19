"""Playbooks for the Data Engineering agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "05-data-engineering/01-etl-pipeline-designer": {
        "fields": ["rows_per_hour|Rows per hour|number|500000", "row_bytes|Average row size (bytes)|number|1500", "late_hours|Late-arrival window (hours)|number|72", "freshness_min|Freshness target (minutes)|number|60", "orchestrator|Orchestrator|text|Airflow with Cloud Composer"],
        "sections": [
            ["Source and target", "Spec: {input}", "Volume {rows_per_hour} rows per hour at {row_bytes} bytes. Orchestrator: {orchestrator}."],
            ["Idempotent design", "Land raw payloads untouched in a partitioned raw table, then transform. Make every task rerunnable: write to a partition with MERGE on a natural key or overwrite the partition atomically, never append blindly.", "Use the logical run time, not the wall clock, as the partition key so backfills reproduce the same output."],
            ["Late and duplicate data", "Webhooks arrive out of order and more than once. Dedupe on the event id, keep ingested_at and event_at, and reprocess a trailing window of {late_hours} hours each run.", "Use a watermark per source and record it in a state table."],
            ["Failure handling", "Retry transient errors with exponential backoff (3 to 5 tries, jitter). Route records that fail validation to a dead-letter table with the error and payload, alert when the dead-letter rate exceeds 0.5 percent.", "Pipelines should fail loudly on schema change instead of loading nulls."],
            ["SLA and monitoring", "Freshness SLA {freshness_min} minutes: alert on the age of the newest event and on row-count deviation from the same hour last week.", "Document ownership and a replay runbook."],
        ],
        "metrics": ["Rows per day|rows_per_hour * 24|{:,.0f}", "Raw volume per day (GB)|rows_per_hour * 24 * row_bytes / 1000000000|{:,.1f}", "Raw volume per month (TB)|rows_per_hour * 24 * 30 * row_bytes / 1000000000000|{:,.2f}"],
    },
    "05-data-engineering/02-dbt-model-generator": {
        "fields": ["grain|Grain of the model|text|One row per order", "unique_key|Unique key|text|order_id", "statuses|Accepted status values|list|pending, paid, refunded, cancelled", "warn_hours|Freshness warn threshold (hours)|number|12", "mart_name|Downstream mart|text|fct_orders"],
        "sections": [
            ["Contract", "Source table: {input}", "Grain: {grain}. Unique key: {unique_key}. Downstream mart: {mart_name}."],
            ["Staging model", "One staging model per source table named stg_<source>__<table>: select only needed columns, rename to snake_case, cast types, convert cents to a decimal amount only in marts, and add no joins or business logic.", "Materialise staging as views; keep it 1:1 with the source so lineage is obvious."],
            ["Tests in schema.yml", "On {unique_key} add unique and not_null. On foreign keys add relationships to the parent model. Add accepted_values for status: {statuses}.", "Add a source freshness block with warn_after {warn_hours} hours and error_after twice that."],
            ["Mart model", "Build {mart_name} with ref() to staging, joins resolved at the stated grain, and explicit column documentation. Use incremental models with a unique_key and a lookback window for large facts.", "Add a singular test that sums total_cents in the mart and compares it to staging."],
            ["Conventions", "Use CTE per input at the top of the file, one final select, no select star in marts, and tag models by domain. Run dbt build in CI with state:modified+ and a slim CI schema.", "Fail the job on test failures; severity warn only for freshness."],
        ],
        "metrics": [],
    },
    "05-data-engineering/03-schema-drift-detector": {
        "fields": ["consumers|Downstream consumers|list|mart_arr, billing dashboard, ML churn features", "contract|Compatibility contract|text|Avro in a schema registry with BACKWARD compatibility", "affected_rows|Rows affected|number|120000000", "notice_days|Notice required for breaking changes (days)|number|14"],
        "sections": [
            ["Detected change", "Diff: {input}", "Contract: {contract}"],
            ["Classify", "Breaking: column removal or rename, type narrowing (bigint to int), nullable to required, semantic change of an existing column, key change. Compatible: new nullable column, widening a type, new enum value only if consumers handle unknowns.", "A removed column is always breaking, even if the producer says it is unused."],
            ["Impact", "Consumers to check: {consumers}", "Query lineage and the warehouse access log for readers of the removed column over the last 90 days; {affected_rows} rows are touched by any backfill."],
            ["Response plan", "Alert severity: breaking with active readers is high and blocks the load. Map the replacement (plan_code to user_tier needs a translation table) and keep a compatibility view with the old column name during migration.", "Breaking changes need {notice_days} days notice, a dual-write period and an owner sign-off."],
            ["Prevention", "Register schemas in a registry with a compatibility check in CI, run contract tests on producers, and snapshot information_schema daily to diff.", "Treat unexpected columns as quarantined, not auto-added."],
        ],
        "metrics": [],
    },
    "05-data-engineering/04-data-quality-guardian": {
        "fields": ["rows_per_day|Typical rows per day|number|120000", "tolerance_pct|Row-count tolerance (percent)|number|20", "freshness_hours|Freshness SLA (hours)|number|6", "key_columns|Key columns|list|invoice_id, customer_id", "parent_table|Parent table for referential check|text|dim_customers"],
        "sections": [
            ["Dataset", "Profile: {input}", "About {rows_per_day} rows per day. Keys: {key_columns}."],
            ["Freshness and volume", "Freshness: newest record must be less than {freshness_hours} hours old, checked every 30 minutes. Volume: daily row count must stay within the bounds below; compare to the same weekday in recent weeks for seasonality.", "Fail on zero rows; warn on a deviation beyond the tolerance."],
            ["Column rules", "Null rate of keys: 0 percent. Uniqueness of the primary key. Value ranges (amounts above zero), accepted values for enums and format checks (ISO dates, currency codes).", "Duplicate rate above 0.1 percent on a key means a broken ingestion, not noise."],
            ["Referential checks", "Every customer_id must exist in {parent_table}; allow a short lag for late-arriving dimensions and alert when orphans exceed 0.5 percent.", "Reconcile totals with the source system once per day (row count and sum of amount)."],
            ["Handling failures", "Severity: block publication for key, freshness and reconciliation failures; warn for distribution drift. Route alerts to the dataset owner and quarantine bad rows.", "Tune thresholds from 60 days of history to keep false alerts below one a week."],
        ],
        "metrics": ["Lower row-count bound|rows_per_day * (1 - tolerance_pct / 100)|{:,.0f}", "Upper row-count bound|rows_per_day * (1 + tolerance_pct / 100)|{:,.0f}"],
    },
    "05-data-engineering/05-warehouse-cost-tuner": {
        "fields": ["table_tb|Table size (TB)|number|4", "queries_per_day|Queries per day on the table|number|12", "scan_after_pct|Share of data scanned after tuning (percent)|number|5", "price_per_tb|On-demand price (USD per TB scanned)|number|6.25", "filter_column|Most common filter column|text|event_date"],
        "sections": [
            ["Workload", "Telemetry: {input}", "{table_tb} TB table, {queries_per_day} queries per day, usual filter {filter_column}."],
            ["Partitioning", "Partition on the date column used in nearly every filter ({filter_column}), daily granularity for tables above 1 TB. Require a partition filter so full scans fail fast.", "Keep partitions above roughly 1 GB; thousands of tiny partitions slow metadata."],
            ["Clustering", "Cluster by up to four columns in order of filter frequency and cardinality, such as customer_id then event_name. Clustering helps filters and joins but needs periodic reclustering for heavy writes.", "Verify by comparing bytes processed before and after on the same queries."],
            ["Other levers", "Select only needed columns (columnar storage bills by column), use materialised views for repeated aggregates, set table expiration on raw tails, and cap query cost with maximum bytes billed.", "Move steady workloads to capacity pricing (slot reservations, autoscaling with a baseline) when monthly on-demand spend exceeds about 10,000 USD."],
            ["Governance", "Label queries by team, publish a top-10 expensive-query report weekly and review it with owners.", "Re-measure monthly; clustering degrades as data grows."],
        ],
        "metrics": ["Current monthly scan cost|table_tb * queries_per_day * 30 * price_per_tb|${:,.0f}", "Monthly cost after tuning|table_tb * queries_per_day * 30 * price_per_tb * scan_after_pct / 100|${:,.0f}", "Monthly saving|table_tb * queries_per_day * 30 * price_per_tb * (1 - scan_after_pct / 100)|${:,.0f}"],
    },
    "05-data-engineering/06-lineage-documenter": {
        "fields": ["target_metric|Target metric or table|text|mart_arr.arr_usd", "upstream|Upstream models|list|dim_subs, fct_payments, stg_stripe__invoices", "downstream|Downstream consumers|list|Board dashboard, Finance Looker explore, ARR alert", "refresh|Refresh schedule|text|Hourly at minute 15"],
        "sections": [
            ["Scope", "SQL graph: {input}", "Target: {target_metric}. Refresh: {refresh}."],
            ["Upstream chain", "*{upstream}", "For each hop record the column used, its transformation (rename, cast, sum, case when) and the filter or join that changes row counts."],
            ["Column-level lineage", "Trace from the metric column back to raw columns by parsing the SQL (sqlglot or the dbt manifest). Mark derived columns, filters that exclude rows, and joins that can fan out and double count.", "Check each join key for uniqueness: a many-to-many join is the most common cause of inflated revenue."],
            ["Downstream impact", "*{downstream}", "Before changing a column, list these consumers and notify their owners; the lineage map is the impact analysis."],
            ["Documentation", "Publish lineage in the data catalog (OpenLineage events or dbt docs), tag owners and certify metrics used by finance. Add column descriptions where logic is non-obvious.", "Regenerate lineage on every merge so it never drifts."],
        ],
        "metrics": [],
    },
    "05-data-engineering/07-pii-redaction-planner": {
        "fields": ["regime|Applicable regulation|text|GDPR and CCPA", "pii_columns|Columns identified as PII|number|3", "total_columns|Total columns reviewed|number|4", "retention_days|Raw retention (days)|number|90", "hash_method|Hashing method|text|HMAC-SHA256 with a secret key held in KMS"],
        "sections": [
            ["Column review", "Columns: {input}", "{pii_columns} of {total_columns} columns carry personal data under {regime}."],
            ["Classification", "Direct identifiers: email, name, phone, SSN, government id. Quasi-identifiers: IP address, postal code, birth date, device id, which combine to re-identify. Sensitive: health, financial, precise location.", "Flag free-text columns; they hide emails and names that pattern matching must scan."],
            ["Masking policy", "Deterministic pseudonymisation for join keys: {hash_method}. Truncate IP addresses (last octet for IPv4), generalise ZIP to the first 3 digits, drop SSNs entirely, and encrypt what must be recoverable.", "Plain unsalted SHA-256 of an email is reversible by dictionary attack; always use a keyed hash."],
            ["Access and retention", "Raw PII lives in a restricted zone with column-level security and audit logs; analysts query masked views only. Delete or anonymise raw data after {retention_days} days.", "Support deletion requests by key: record where each subject id is stored."],
            ["Validation", "Scan outputs with a PII detector on a sample after each load, and test that masked values still join across tables.", "Document lawful basis and data processing records for the regime."],
        ],
        "metrics": ["Share of columns holding PII|pii_columns / total_columns|{:.0%}"],
    },
    "05-data-engineering/08-backfill-orchestrator": {
        "fields": ["total_days|Days in the backfill window|number|1035", "chunk_days|Days per chunk|number|7", "workers|Concurrent workers|number|4", "chunk_minutes|Minutes per chunk|number|12", "rate_limit|Source rate limit|text|600 requests per minute shared across workers"],
        "sections": [
            ["Window", "Request: {input}", "{total_days} days in chunks of {chunk_days}, {workers} workers. Source limit: {rate_limit}."],
            ["Chunking", "Split into contiguous date windows aligned to partition boundaries so each chunk writes whole partitions. Process newest first when recent data matters most, otherwise oldest first.", "Make each chunk idempotent (overwrite its partitions) and record state: pending, running, done, failed."],
            ["Rate and load", "Share the rate limit across workers, back off on 429 or 503 with jitter, and pause when warehouse slot usage or replication lag crosses a set level. Run off-peak.", "Never let a backfill compete with the live pipeline for the same partitions; lock or write to a staging table and swap."],
            ["Validation", "After each chunk compare row counts and a sum checksum with the source; fail the chunk on mismatch beyond 0.1 percent. Spot check one day per month.", "Keep a manifest of chunks, durations and errors for audit."],
            ["Resume and stop", "Retry a failed chunk up to 3 times, then park it and continue. Provide a stop switch that finishes current chunks only.", "Downstream models rebuild once at the end, not per chunk."],
        ],
        "metrics": ["Number of chunks|total_days / chunk_days|{:,.0f}", "Wall-clock time (hours)|total_days / chunk_days * chunk_minutes / workers / 60|{:,.1f}"],
    },
    "05-data-engineering/09-streaming-lag-analyst": {
        "fields": ["hot_lag|Lag on the hot partition (messages)|number|450000", "other_lag|Lag on other partitions (messages)|number|120", "consume_rate|Consumer throughput per partition (messages per second)|number|1500", "produce_rate|Producer rate on the hot partition (messages per second)|number|900", "group|Consumer group and topic|text|billing-worker on topic payments.events"],
        "sections": [
            ["Observation", "Metrics: {input}", "Group: {group}. Hot partition lag {hot_lag}; others {other_lag}."],
            ["Skew diagnosis", "One partition far behind the rest means key skew or one slow consumer, not a global capacity shortfall. Check the message key distribution (a hot customer id hashing to partition 3), message size, and per-record processing time on that consumer.", "Compare the consumer's CPU, GC pauses and downstream call latency with its peers."],
            ["Rebalance storms", "Frequent rebalances show up as lag sawtooth and log lines about members leaving. Causes: max.poll.interval.ms exceeded by slow processing, session timeouts, rolling deploys.", "Fix with cooperative-sticky assignment, static membership (group.instance.id), smaller max.poll.records and a longer poll interval."],
            ["Remediation", "Short term: add a dedicated consumer thread or scale processing for the hot partition, skip or park poison messages in a dead-letter topic. Long term: change the partition key (salt hot keys), increase partitions only with an ordering review.", "More consumers than partitions adds nothing: parallelism is capped at the partition count."],
            ["Alerting", "Alert on lag in seconds of data (time lag) rather than messages, and on the lag growth rate. Page when time lag exceeds the SLA for 10 minutes.", "Track lag per partition, not only the group maximum."],
        ],
        "metrics": ["Skew ratio (hot / other)|hot_lag / other_lag|{:,.0f}x", "Net drain rate (messages per second)|consume_rate - produce_rate|{:,.0f}", "Time to drain the hot partition (minutes)|hot_lag / (consume_rate - produce_rate) / 60|{:,.1f}"],
    },
    "05-data-engineering/10-metric-layer-definer": {
        "fields": ["start_mrr|MRR at period start (USD)|number|410000", "expansion_mrr|Expansion MRR (USD)|number|62000", "contraction_mrr|Contraction MRR (USD)|number|18000", "churned_mrr|Churned MRR (USD)|number|30000", "grain|Time grain and dimensions|text|Monthly, by signup cohort and plan"],
        "sections": [
            ["Request", "KPI: {input}", "Grain: {grain}."],
            ["Canonical definitions", "MRR: sum of normalised monthly recurring fees for active subscriptions at period end, excluding one-time fees, usage overage and taxes; annual plans divided by 12.", "NRR = (starting MRR + expansion - contraction - churn) / starting MRR, measured on the cohort that existed at the start only, with new-logo revenue excluded."],
            ["Related metrics", "Gross revenue retention = (starting MRR - contraction - churn) / starting MRR and can never exceed 100 percent. Active user: a user with at least one qualifying event (named in the metric) in the trailing 28 days.", "Define each metric once; dashboards must not recompute it."],
            ["Semantic layer spec", "Write the metric as YAML with name, label, type (ratio, simple), numerator and denominator measures, filters, time dimension, allowed dimensions and an owner. Version it in git and test with known fixtures.", "Include currency handling and the rule for mid-month upgrades (daily proration or period-end snapshot)."],
            ["Quality gates", "Reconcile MRR to the billing system to within 0.5 percent monthly; document edge cases (trials, paused, refunds, reactivations).", "Changing a definition requires a version bump and a restated history."],
        ],
        "metrics": ["Net revenue retention|(start_mrr + expansion_mrr - contraction_mrr - churned_mrr) / start_mrr|{:.1%}", "Gross revenue retention|(start_mrr - contraction_mrr - churned_mrr) / start_mrr|{:.1%}", "Ending MRR from the starting cohort|start_mrr + expansion_mrr - contraction_mrr - churned_mrr|${:,.0f}"],
    },
}
