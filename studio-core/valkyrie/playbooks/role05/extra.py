"""Playbooks for the Data Engineering agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "05-data-engineering/11-cdc-pipeline-designer": {
        "fields": ["tables|Tables to capture|number|14", "peak_updates_s|Peak changes per second|number|300", "target_lag_min|Target lag (minutes)|number|5", "avg_bytes|Average bytes per change event|number|900", "retention_h|Hours the log is retained at the source|number|24"],
        "sections": [
            ["Source", "Source: {input}", "{tables} tables, peak {peak_updates_s} changes per second, target lag {target_lag_min} minutes.", "Change data capture reads the database log instead of querying tables, so it sees deletes and does not load the primary."],
            ["Capture design", "Take a consistent snapshot, record the log position and then stream changes from that position. Use a log-based tool such as Debezium and a replication slot with a lag alert.", "An unread replication slot can fill the source disk. Alert on slot lag and retention."],
            ["Delivery and ordering", "Partition events by primary key so changes to one row stay in order. Deliver at least once and make the sink idempotent with a merge on key and log position.", "Keep the operation type (insert, update, delete) and a commit timestamp on every event."],
            ["Schema changes", "Use a schema registry with compatibility rules, treat new nullable columns as safe and route breaking changes to a review.", "Test what happens on a column rename and on a table with no primary key."],
            ["Operations", "Monitor end-to-end lag, event throughput and dead letters. Rehearse a re-snapshot, because you will need one.", "The log is kept {retention_h} hours at the source: recover from an outage inside that window or re-snapshot."],
        ],
        "metrics": ["Peak throughput (MB per second)|peak_updates_s * avg_bytes / 1000000|{:.2f}", "Data per day at peak rate (GB)|peak_updates_s * avg_bytes * 86400 / 1000000000|{:,.0f}"],
    },
    "05-data-engineering/12-data-contract-author": {
        "fields": ["dataset|Dataset|text|orders_daily", "owner|Owning team|text|Payments data team", "fresh_by|Fresh by (UTC hour)|number|6", "min_rows|Minimum rows per day|number|20000", "consumers|Known consumers|number|9"],
        "sections": [
            ["Dataset", "Spec: {input}", "Dataset: {dataset}. Owner: {owner}. Known consumers: {consumers}.", "A data contract is an agreement between the team that produces a dataset and the teams that depend on it."],
            ["Schema", "List every column with name, type, nullability, allowed values and an example. Mark the primary key and which columns hold personal data.", "State the grain in one sentence: one row per what."],
            ["Meaning", "Define each business term, the unit (cents, not dollars) and the time zone, and say how late data or corrections are handled.", "Link to the source system and the transformation code."],
            ["Quality and freshness", "Freshness: ready by {fresh_by}:00 UTC. Volume: at least {min_rows} rows a day. Uniqueness on the key, no nulls in required columns and value ranges for amounts.", "Run these checks on every load and publish the results to consumers."],
            ["Change process", "Additive changes need a notice. Breaking changes (rename, type change, removal) need a new version, a deprecation period and agreement from the {consumers} consumers.", "Name the on-call contact and the support channel."],
        ],
        "metrics": ["Hours of the day available to consumers after refresh|24 - fresh_by|{:.0f}", "Minimum rows per hour|min_rows / 24|{:,.0f}"],
    },
    "05-data-engineering/13-partition-strategy-advisor": {
        "fields": ["table_tb|Table size (TB)|number|6", "days_kept|Days of data|number|730", "query_days|Days a typical query reads|number|7", "partition_mb|Target partition size (MB)|number|512", "skew_share|Share of rows owned by the biggest customer (0 to 1)|number|0.12"],
        "sections": [
            ["Table", "Profile: {input}", "Table: {table_tb} TB over {days_kept} days. Typical query reads {query_days} days.", "Partitioning lets a query skip data it does not need. It helps only if the filter matches the partition key."],
            ["Choose the key", "Partition by event date when most queries filter on a time range. Cluster or sort within each partition by the next most common filter, here customer id.", "Avoid high-cardinality partition keys such as user id: they create millions of tiny partitions."],
            ["Size", "Aim for partitions of about {partition_mb} MB or more. Daily partitions suit large tables, monthly ones suit small ones.", "Too many small files slow queries and metadata. Compact them on a schedule."],
            ["Skew", "The biggest customer holds {skew_share} of the rows. Check for hot partitions and hot keys, and consider salting or splitting that customer.", "Look at the distribution before choosing the key, not after."],
            ["Enforce and monitor", "Require a filter on the partition column in queries on large tables and track bytes scanned per query.", "Re-evaluate the strategy when query patterns change."],
        ],
        "metrics": ["Share of the table a typical query reads|query_days / days_kept|{:.1%}", "Data read per typical query (GB)|table_tb * 1000 * query_days / days_kept|{:,.0f}", "Partitions at one per day|days_kept|{:,.0f}"],
    },
    "05-data-engineering/14-dedup-strategy-designer": {
        "fields": ["rows_day|Rows per day|number|50000000", "dup_rate|Duplicate rate (0 to 1)|number|0.034", "window_h|Dedup window (hours)|number|48", "key|Natural key|text|event_id plus source", "row_bytes|Average bytes per row|number|300"],
        "sections": [
            ["Problem", "Report: {input}", "Natural key: {key}. Window: {window_h} hours.", "Duplicates come from retries, replays, overlapping extracts and the same entity entered twice. Each has a different fix."],
            ["Exact duplicates", "Deduplicate on the natural key within a time window using a row number over the key ordered by ingest time, or a merge with the key as the match condition.", "Do it as early as possible, before aggregates and joins multiply the error."],
            ["Late data", "A window of {window_h} hours keeps state bounded. Events arriving later than the window are logged and reconciled in a daily batch.", "Choose the window from the real lateness distribution."],
            ["Fuzzy matching", "For people and companies, normalise (case, spaces, punctuation), block by a cheap key such as postcode and compare candidate pairs with a similarity score. Send mid-score pairs to review.", "Prefer merging with a reversible link table over destroying records."],
            ["Survivorship and checks", "Choose which values win: latest, most complete or from the most trusted source. Test that counts before and after match the duplicate rate.", "Alert when the duplicate rate moves by more than a third."],
        ],
        "metrics": ["Duplicate rows per day|rows_day * dup_rate|{:,.0f}", "Storage wasted per day (GB)|rows_day * dup_rate * row_bytes / 1000000000|{:,.1f}"],
    },
    "05-data-engineering/15-scd-modeler": {
        "fields": ["dimension|Dimension|text|Customer", "rows|Rows in the dimension|number|2500000", "change_rate|Share of rows that change per month (0 to 1)|number|0.08", "months|Months of history kept|number|36", "tracked_cols|Columns whose history you track|number|4"],
        "sections": [
            ["Dimension", "Change description: {input}", "Dimension: {dimension}, {rows} rows. {tracked_cols} columns need history.", "Slowly changing dimensions decide how a warehouse remembers what an entity looked like at the time of each fact."],
            ["Pick the type", "Type 1 overwrites (no history, use for corrections). Type 2 adds a row per change with valid-from and valid-to dates (use when reports need the value at the time). Type 3 keeps one previous value.", "Mix types by column: track tier with type 2 and fix typos with type 1."],
            ["Keys", "Give each version a surrogate key and keep the natural key. Facts join to the surrogate key that was current at the event time.", "Add a current-flag column to make the common query simple."],
            ["Load logic", "Compare incoming rows with the current version on the tracked columns only. On a change, close the old row (valid-to) and insert the new one in one transaction. Make the load idempotent.", "Handle late-arriving changes by re-opening affected facts."],
            ["Growth", "At this change rate the dimension grows each month by the amount shown below. Watch size and consider tracking fewer columns or snapshotting instead.", "Test with a customer who changes three times in a day."],
        ],
        "metrics": ["New versions per month|rows * change_rate|{:,.0f}", "Extra rows over the history window|rows * change_rate * months|{:,.0f}", "Dimension size after the window (rows)|rows + rows * change_rate * months|{:,.0f}"],
    },
    "05-data-engineering/16-dag-migration-planner": {
        "fields": ["jobs|Jobs to migrate|number|420", "hidden_deps|Jobs with hidden dependencies|number|60", "per_week|Jobs migrated per week|number|25", "critical|Business-critical jobs|number|45", "parallel_weeks|Weeks of parallel running per wave|number|2"],
        "sections": [
            ["Inventory", "Jobs: {input}", "{jobs} jobs, {hidden_deps} with hidden dependencies, {critical} business-critical.", "Migration fails on what nobody wrote down. Discover real dependencies from logs and file timestamps, not only from the schedule."],
            ["Waves", "Wave 1: simple, low-risk jobs to learn the platform. Wave 2: jobs in the same dependency chain together. Final wave: critical jobs with the most testing.", "Migrate a whole chain at once so you never run half a pipeline on each side."],
            ["Parity", "Run old and new in parallel for {parallel_weeks} weeks and compare row counts, checksums and key aggregates. Treat any unexplained difference as a blocker.", "Keep the new system read-only (writing to a shadow location) until the comparison passes."],
            ["Rebuild, not lift", "Make jobs idempotent, add retries, alerts, data-quality checks and owners as you move them. Delete jobs nobody uses.", "Ask each owner to confirm that the output is still used."],
            ["Cutover and rollback", "Switch consumers in stages, keep the old job disabled but runnable for a month and agree a rollback trigger in advance.", "Track burn-down: jobs migrated, jobs deleted and jobs left."],
        ],
        "metrics": ["Weeks at the current pace|jobs / per_week|{:.0f}", "Waves of critical jobs at the same pace|critical / per_week|{:.1f}"],
    },
    "05-data-engineering/17-feature-store-reviewer": {
        "fields": ["features|Features reviewed|number|38", "dual_logic|Features computed twice (training and serving)|number|14", "stale_hours|Hours of staleness at serving|number|24", "allowed_hours|Staleness the model tolerates (hours)|number|4", "owners|Features with a named owner|number|21"],
        "sections": [
            ["Features", "Specs: {input}", "{features} features. {dual_logic} are computed separately for training and serving.", "A feature store gives training and serving the same definition, so the model sees the same numbers it was trained on."],
            ["Training and serving skew", "Computing a feature twice invites differences. Define it once and compute it for both paths, or test that both give the same value on a sample.", "Log served feature values and compare their distribution with training."],
            ["Leakage", "Training features must be computed as of the prediction time: no data from after the event and nothing derived from the label. Use point-in-time joins.", "A model that looks too good is often leaking."],
            ["Freshness", "Serving data is {stale_hours} hours old and the model tolerates {allowed_hours}. Add streaming updates or a faster batch for the features that move quickly.", "Record each feature's freshness target and alert when it is missed."],
            ["Ownership and reuse", "Every feature needs an owner, a description, a data source and tests. Search the catalog before creating a feature, to avoid duplicates under different names.", "Retire features no model uses."],
        ],
        "metrics": ["Share of features computed twice|dual_logic / features|{:.0%}", "Staleness over the tolerance (hours)|stale_hours - allowed_hours|{:+.0f}", "Features without an owner|features - owners|{:,.0f}"],
    },
    "05-data-engineering/18-data-retention-planner": {
        "fields": ["dataset|Dataset|text|Clickstream events", "tb_year|New data per year (TB)|number|80", "years_kept|Years currently kept|number|6", "years_needed|Years you actually need|number|2", "price_tb|Storage cost per TB per month (USD)|number|23"],
        "sections": [
            ["Catalog", "Catalog: {input}", "Dataset: {dataset}. Adds {tb_year} TB per year, kept {years_kept} years, needed {years_needed}.", "Keep data while it has a purpose, a legal duty or a proven use. Keeping everything forever is a cost and a risk."],
            ["Retention by class", "Classify each dataset: legal records (keep by law), operational data, analytics data and personal data. Set a period for each from the purpose, not from habit.", "For personal data, the period must match the stated purpose, and deletion requests must reach every copy."],
            ["Tiering and aggregation", "Keep detailed data hot for the period you analyse it, then aggregate and archive or delete the detail.", "Clickstream is rarely used at event level after a year or two."],
            ["Deleting safely", "Delete by partition and by policy, record each deletion run, and protect legal holds from deletion jobs.", "Include backups and derived tables in the schedule, or they keep the data alive."],
            ["Savings and review", "Cutting from {years_kept} to {years_needed} years frees the storage shown below. Review retention yearly with legal and the data owners.", "Publish the schedule in the data catalog."],
        ],
        "metrics": ["Stored today (TB)|tb_year * years_kept|{:,.0f}", "Stored after the change (TB)|tb_year * years_needed|{:,.0f}", "Monthly saving (USD)|tb_year * (years_kept - years_needed) * price_tb|${:,.0f}"],
    },
    "05-data-engineering/19-sql-style-reviewer": {
        "fields": ["query_lines|Lines in the query|number|120", "ctes|Common table expressions used|number|0", "joins|Joins in the query|number|6", "runs_day|Runs per day|number|48", "owner|Owner|text|Finance analytics"],
        "sections": [
            ["Query", "SQL: {input}", "{query_lines} lines, {joins} joins, runs {runs_day} times a day. Owner: {owner}.", "Readable SQL is cheaper to fix. The next reader is usually you, six months later."],
            ["Structure", "Use common table expressions with clear names, one step each. Avoid deep subquery nesting and repeated logic. Put each clause on its own line with consistent capitalisation.", "This query has {ctes} common table expressions, which suggests it is one long block."],
            ["Joins", "Use explicit JOIN ... ON, never comma joins with the condition in WHERE. Check that each join key is unique on the side you expect, since a many-to-many join multiplies rows silently.", "Use LEFT JOIN deliberately and filter on the joined table in the ON clause, not in WHERE."],
            ["Correctness traps", "NULL is not equal to anything, so use IS NULL. COUNT of a column skips NULLs. Add every non-aggregated column to GROUP BY. Compare dates with half-open ranges and state the time zone. Do not ORDER BY a column position.", "Avoid SELECT * in views and exports, because a new column breaks consumers."],
            ["Performance", "Filter early, select only needed columns, avoid functions on indexed columns in WHERE and check the plan for scans on large tables.", "Add a test on row counts and uniqueness for the result."],
        ],
        "metrics": ["Lines per join|query_lines / joins|{:.0f}", "Runs per month|runs_day * 30|{:,.0f}"],
    },
    "05-data-engineering/20-catalog-documenter": {
        "fields": ["table|Table name|text|fct_subscriptions", "owner|Data owner|text|Revenue analytics", "columns|Number of columns|number|34", "documented|Columns with a description|number|11", "users_month|Monthly users of the table|number|65"],
        "sections": [
            ["Table", "Metadata: {input}", "Table: {table}. Owner: {owner}. {documented} of {columns} columns are described.", "A catalog entry should let a new analyst decide in a minute whether the table answers their question."],
            ["Summary", "Start with one sentence on the grain (one row per what), the business purpose and the typical questions it answers.", "Add the freshness, the time zone and the known limitations."],
            ["Columns", "Describe each column in plain language with unit and allowed values. Tag personal data, keys and metrics. Start with the most queried columns.", "Description coverage today is shown below. Aim for 100 percent on the important tables."],
            ["Lineage and quality", "Show upstream sources, the model that builds it and the downstream dashboards. Display the latest test results and freshness, so people can trust the data.", "Link the code and the owner's channel."],
            ["Access and usage", "State who may use it, the personal data it holds and how to request access. Add three example queries.", "Review entries with the owner each quarter and flag tables nobody has used for a year."],
        ],
        "metrics": ["Column documentation coverage|documented / columns|{:.0%}", "Columns still to describe|columns - documented|{:,.0f}"],
    },
}
