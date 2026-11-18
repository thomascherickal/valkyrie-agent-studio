"""Playbooks for the Software Engineering agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "02-software-engineering/01-architecture-reviewer": {
        "fields": ["slo|Service level objective|text|99.9% of invoices processed within 5 minutes", "throughput|Peak messages per second|number|150", "per_msg_ms|Processing time per message (ms)|number|20", "instances|Consumer instances|number|4", "spofs|Suspected single points of failure|list|Single Postgres primary, One Kafka cluster, Shared Redis lock"],
        "sections": [
            ["System under review", "RFC summary: {input}", "Objective: {slo}", "Draw the data flow first: every box that can fail independently is a failure domain."],
            ["Single points of failure", "*{spofs}", "For each, record the blast radius, detection time and recovery time. A SPOF is acceptable only with a tested manual failover and a stated RTO."],
            ["Backpressure and capacity", "Peak {throughput} messages per second, {per_msg_ms} ms each, across {instances} instances.", "Bound every queue and buffer. An unbounded queue turns an overload into an out-of-memory crash. Prefer load shedding or pause/resume on the consumer over silent retries."],
            ["Consistency and delivery", "Kafka gives at-least-once delivery, so consumers must be idempotent: dedupe on a business key or use the transactional outbox pattern.", "Check dual writes: updating the database and publishing an event in two steps without an outbox will lose events on a crash between them."],
            ["Coupling and evolution", "Look for shared databases between services, synchronous call chains deeper than three hops, and schema changes without compatibility rules.", "Require a schema registry or versioned event contracts, a dead-letter queue with alerting, and a replay runbook."],
        ],
        "metrics": ["Consumer utilization at peak|throughput * per_msg_ms / (instances * 1000)|{:.0%}", "Capacity per instance (msgs per second)|1000 / per_msg_ms|{:,.0f}", "Instances needed at 60% target utilization|throughput * per_msg_ms / (1000 * 0.6)|{:.1f}"],
    },
    "02-software-engineering/02-pr-code-reviewer": {
        "fields": ["language|Language and framework|text|Python 3.12 with FastAPI and SQLAlchemy", "diff_lines|Lines changed|number|320", "tests_changed|Test files changed|number|0", "risk_areas|Risk areas touched|list|Database access, Auth middleware, Background jobs", "hot_path|Is this a hot path?|text|Yes, runs on every API request"],
        "sections": [
            ["Change under review", "Snippet: {input}", "Stack: {language}. Hot path: {hot_path}. Diff size: {diff_lines} lines, {tests_changed} test files changed."],
            ["Correctness checks", "Boundary conditions (empty, one, max, off by one), null and missing values, integer overflow, time zones, and error paths that swallow exceptions.", "N+1 queries: a database call inside a loop is a defect on a hot path; replace with a batched IN query or a join."],
            ["Resource and concurrency checks", "Every opened file, socket, cursor and lock must be released on all paths (context manager or finally). Check unawaited coroutines, shared mutable state and retries without backoff.", "Unbounded lists built from user input are memory leaks waiting for a large customer."],
            ["Risk areas", "*{risk_areas}", "Auth, money and data deletion changes need a second reviewer and an explicit test for the denied case."],
            ["Tests and review etiquette", "A behaviour change without a test is a request-changes. Ask for a failing test that reproduces each bug fix.", "Label comments: blocking, suggestion, nit. Review at most 400 lines per sitting; defect detection drops sharply above that."],
        ],
        "metrics": ["Review time at 300 lines per hour|diff_lines / 300|{:.1f}", "Comments to expect (1 per 25 lines)|diff_lines / 25|{:.0f}"],
    },
    "02-software-engineering/03-refactor-planner": {
        "fields": ["loc|Lines of code|number|1850", "callers|Number of callers|number|14", "coverage_pct|Unit test coverage (percent)|number|0", "weeks_available|Weeks available|number|8", "facade_target|Target module or service|text|auth service behind an AuthFacade interface"],
        "sections": [
            ["Starting point", "Module metrics: {input}", "{loc} lines, {callers} callers, {coverage_pct} percent coverage. Target: {facade_target}."],
            ["Step 1: pin behaviour", "Write characterization tests that record current outputs for the main paths before touching anything. Aim for at least 80 percent branch coverage of the code you will move.", "With zero coverage, do not refactor and add features in the same pull request."],
            ["Step 2: strangler seam", "Put a facade in front of the old module and route every caller through it. Keep the public signature identical.", "Introduce the new implementation behind a feature flag and compare old and new results in shadow mode before switching."],
            ["Step 3: migrate callers", "Migrate callers one at a time, smallest blast radius first. Each step must be a deployable commit that can be reverted alone.", "Track remaining callers on a burndown. Delete the old code only after one full release with zero traffic."],
            ["Risks and stop rules", "Stop and re-plan if the shadow comparison differs on more than 0.1 percent of calls or if a caller needs a signature change.", "Do not rename public symbols during the extraction; do it after the old path is deleted."],
        ],
        "metrics": ["Callers to migrate per week|callers / weeks_available|{:.1f}", "Coverage gap to 80% target (points)|max(0, 80 - coverage_pct)|{:.0f}", "Lines per caller|loc / callers|{:,.0f}"],
    },
    "02-software-engineering/04-api-contract-designer": {
        "fields": ["current_version|Current API version|text|v1", "consumers|Known consumers|list|Studio UI, CLI, Partner integrations", "auth_scheme|Authentication|text|Bearer token with scope agents:deploy", "sunset_months|Deprecation window (months)|number|6", "idempotency|Idempotency approach|text|Idempotency-Key header, stored for 24 hours"],
        "sections": [
            ["Endpoint", "Spec: {input}", "Current version {current_version}; auth: {auth_scheme}.", "Name resources as plural nouns, use HTTP verbs for actions, and keep deploy-style actions as a sub-resource that returns 202 with a status URL when work is asynchronous."],
            ["Schema rules", "Define request and response in OpenAPI 3.1 with required fields, enums, formats and examples. Return one error shape (RFC 9457 problem details) with a stable machine code.", "Use cursor pagination, ISO 8601 UTC timestamps, and string IDs."],
            ["Breaking change detector", "Breaking: removing or renaming a field, tightening a type or enum, making an optional field required, changing a status code, adding a required parameter.", "Non-breaking: adding optional fields, adding enum values (only if clients are told to tolerate unknowns), new endpoints."],
            ["Versioning and deprecation", "Consumers to notify: {consumers}", "Announce deprecation with a Sunset header and docs link, run both versions for {sunset_months} months, and track per-consumer traffic on the old version before shutdown."],
            ["Safety", "Mutating calls must be safe to retry: {idempotency}", "Document rate limits, 429 with Retry-After, and the exact scopes needed per operation."],
        ],
        "metrics": [],
    },
    "02-software-engineering/05-sql-query-optimizer": {
        "fields": ["engine|Database engine|text|PostgreSQL 16", "table_rows|Rows in the table|number|50000000", "rows_returned|Rows returned per query|number|50", "row_bytes|Average row size (bytes)|number|220", "calls_per_min|Calls per minute|number|600", "current_ms|Current latency (ms)|number|800"],
        "sections": [
            ["Query under review", "SQL: {input}", "Engine: {engine}. {table_rows} rows, about {rows_returned} returned, called {calls_per_min} times per minute at {current_ms} ms."],
            ["Read the plan", "Run EXPLAIN (ANALYZE, BUFFERS). Look for Seq Scan on large tables, a Sort node spilling to disk, row estimates off by 10x from actual rows, and nested loops over large inputs.", "Stale statistics cause bad estimates: run ANALYZE before blaming the query."],
            ["Index recommendation", "Order composite index columns: equality filters first, then the sort column, then range filters. For a filter on a tenant id and ordering by created_at descending, index (org_id, created_at DESC).", "Add INCLUDE columns for an index-only scan, and use CREATE INDEX CONCURRENTLY on live tables."],
            ["Rewrites", "Replace SELECT * with the needed columns, replace OFFSET pagination with keyset pagination (WHERE created_at < last_seen), and add LIMIT to unbounded reads.", "Avoid functions on indexed columns in WHERE; they prevent index use unless you add an expression index."],
            ["Cost of the change", "Each index slows writes and uses disk. Check unused indexes with pg_stat_user_indexes before adding more.", "Target: a selective query returning {rows_returned} rows should finish in under 10 ms from an index."],
        ],
        "metrics": ["Selectivity|rows_returned / table_rows|{:.6%}", "Table size (MB)|table_rows * row_bytes / 1000000|{:,.0f}", "Database busy-seconds per minute|current_ms * calls_per_min / 1000|{:,.0f}"],
    },
    "02-software-engineering/06-dependency-auditor": {
        "fields": ["distribution|Distribution model|text|Hosted SaaS plus downloadable desktop app", "total_deps|Total dependencies (direct and transitive)|number|180", "outdated|Dependencies more than 1 major version behind|number|27", "known_vulns|Dependencies with known CVEs|number|3", "license_policy|License policy|longtext|Allow MIT, Apache-2.0, BSD, ISC\nReview LGPL and MPL\nBlock GPL and AGPL in shipped code"],
        "sections": [
            ["Inventory", "Lockfile: {input}", "{total_deps} dependencies, {outdated} badly outdated, {known_vulns} with known CVEs. Distribution: {distribution}."],
            ["License conflicts", "*{license_policy}", "GPL and AGPL copyleft matters most when you distribute or serve the code; a desktop app that bundles a GPL library must be treated as distribution. Unknown or missing licenses count as blocked until resolved."],
            ["Maintenance health", "Flag a package as unmaintained if there is no release in 24 months, an archived repository, a single maintainer with open security issues, or a deprecation notice.", "For each flagged package, name a replacement or an owner who will vendor and patch it."],
            ["Vulnerabilities", "Triage CVEs by CVSS score, exploit availability and whether the vulnerable function is reachable. Upgrade within 7 days for critical and 30 days for high.", "Pin versions with hashes and run the audit in CI so new findings fail the build."],
            ["Bloat", "Remove packages used by one function you can write in 10 lines, duplicate libraries for the same job, and dev tools listed as runtime dependencies.", "Track install size and cold-start time as budgets."],
        ],
        "metrics": ["Outdated share|outdated / total_deps|{:.0%}", "Vulnerable share|known_vulns / total_deps|{:.1%}"],
    },
    "02-software-engineering/07-migration-assistant": {
        "fields": ["engine|Database engine|text|PostgreSQL 16", "table_rows|Rows in the table|number|12000000", "batch_size|Backfill batch size (rows)|number|5000", "batch_ms|Time per batch (ms)|number|150", "pause_ms|Pause between batches (ms)|number|200"],
        "sections": [
            ["Change", "Schema change: {input}", "Engine: {engine}. Table has {table_rows} rows; backfill in batches of {batch_size}."],
            ["Expand phase", "Add the new column or table as nullable with no default rewrite. Deploy application code that writes to both old and new, and keep reads on the old.", "On large tables avoid ALTER operations that take an ACCESS EXCLUSIVE lock for long; set lock_timeout to 3 seconds and retry."],
            ["Backfill phase", "Copy data in primary-key ordered batches, commit each batch, sleep between batches, and make the job resumable and idempotent.", "Watch replication lag and p95 latency; pause the job automatically if lag exceeds 5 seconds."],
            ["Contract phase", "Switch reads to the new column, verify counts and checksums match, wait one full release, then drop the old column in a separate migration.", "Never drop in the same deploy that stops reading."],
            ["Reversibility", "Every step needs a down script. Test up, down and up again on a production-sized copy. Take a snapshot before the contract step.", "Rollback rule: if error rate rises 2x during backfill, stop the job and keep dual writes."],
        ],
        "metrics": ["Number of batches|table_rows / batch_size|{:,.0f}", "Backfill duration (minutes)|table_rows / batch_size * (batch_ms + pause_ms) / 60000|{:,.1f}"],
    },
    "02-software-engineering/08-tech-debt-triager": {
        "fields": ["churn|Commits touching the file in 90 days|number|48", "complexity|Cyclomatic complexity|number|35", "bugs_per_quarter|Bugs per quarter|number|12", "hours_per_bug|Hours per bug|number|6", "fix_days|Estimated fix effort (engineer-days)|number|15"],
        "sections": [
            ["Debt item", "Item: {input}", "Churn {churn} commits per 90 days, complexity {complexity}, {bugs_per_quarter} bugs per quarter."],
            ["Hotspot logic", "Debt hurts where change is frequent and the code is complex. Hotspot score = churn x complexity. Stable ugly code that nobody touches can wait.", "Get churn from git log over 90 days and complexity from a tool such as radon or lizard."],
            ["Return on investment", "Compare bug-hours per quarter to fix effort. Payback under 2 quarters: do now. 2 to 4 quarters: schedule. Over 4 quarters: accept or document.", "Include indirect costs: onboarding time, incident count and blocked features."],
            ["Ranking rules", "Rank by hotspot score, then by payback. Break ties by customer-facing risk and by whether the item blocks a planned roadmap item.", "Reserve 15 to 20 percent of every sprint for the top three items."],
            ["Tracking", "Record each item with owner, metric to improve and a review date. Close it only when the metric moves, not when the code is merged.", "Re-run the ranking quarterly; the hotspots move."],
        ],
        "metrics": ["Hotspot score|churn * complexity|{:,.0f}", "Bug hours per quarter|bugs_per_quarter * hours_per_bug|{:,.0f}", "Payback in quarters|fix_days * 8 / (bugs_per_quarter * hours_per_bug)|{:.1f}"],
    },
    "02-software-engineering/09-concurrency-debugger": {
        "fields": ["runtime|Runtime|text|Python asyncio with asyncpg and a shared Redis lock", "locks|Locks involved|list|lock1, lock2", "ops_per_sec|Acquisitions per second|number|120", "hold_ms|Average hold time (ms)|number|5", "timeout_ms|Lock timeout (ms)|number|2000"],
        "sections": [
            ["Observed behaviour", "Trace: {input}", "Runtime: {runtime}. Locks: {locks}."],
            ["Deadlock detection", "Build a wait-for graph: an edge from each task to the lock it waits for and from the lock to its holder. Any cycle is a deadlock. Two tasks taking the same two locks in opposite order is the classic inversion.", "Fix by a global lock order (for example by lock id), by acquiring all locks at once, or by removing one lock."],
            ["Async pitfalls", "Check for unawaited coroutines (task created and dropped), blocking calls inside an event loop, await while holding a lock around slow I/O, and tasks cancelled without cleanup.", "Use asyncio.timeout and timeouts on every lock acquire, currently {timeout_ms} ms, and log the holder on timeout."],
            ["Contention", "Lock utilization = acquisitions per second x hold time in seconds. Above 0.7 the queueing delay grows quickly; above 1.0 the lock is a hard bottleneck.", "Shrink the critical section, shard the lock by key, or use optimistic concurrency with a version column."],
            ["Proof of fix", "Reproduce with a stress test with randomised scheduling (many iterations, small sleeps). Add a regression test that fails on the old lock order.", "Ship with a metric for lock wait time and an alert on p99 wait above 100 ms."],
        ],
        "metrics": ["Lock utilization|ops_per_sec * hold_ms / 1000|{:.2f}", "Max throughput of the lock (per second)|1000 / hold_ms|{:,.0f}"],
    },
    "02-software-engineering/10-rust-port-advisor": {
        "fields": ["cpu_share|Share of CPU time in the hotspot (percent)|number|68", "hotspot_speedup|Expected speedup of the hotspot (x)|number|15", "p99_ms|Current p99 latency (ms)|number|42", "monthly_cost|Monthly compute cost of the service (USD)|number|3000", "port_weeks|Estimated port effort (engineer-weeks)|number|3"],
        "sections": [
            ["Profile", "Profile: {input}", "Hotspot takes {cpu_share} percent of CPU; current p99 is {p99_ms} ms."],
            ["Is it worth porting?", "Amdahl's law: overall speedup = 1 / ((1 - p) + p / s) where p is the hotspot share and s its speedup. A 68 percent hotspot caps the gain well below the hotspot speedup.", "Port only pure, CPU-bound, well-tested functions. Do not port I/O-bound code: the bottleneck is the network, not Python."],
            ["Port design", "Expose the function through PyO3 with a maturin build, release the GIL during compute (Python::allow_threads), and move data across the boundary as bytes or arrow buffers, not per-item Python objects.", "Use Tokio only if the Rust side does async I/O; for pure compute use rayon."],
            ["Verification", "Keep the Python version as the oracle. Run property tests and a corpus of real inputs comparing outputs bit for bit, and benchmark with criterion plus the original profile.", "Ship behind a flag and compare p99 in canary before removal."],
            ["Decision rule", "Go if estimated savings pay back the effort within 6 months and p99 matters to an SLO. Otherwise try caching, vectorisation or a C-backed library first.", "Estimated engineer cost: assume roughly 4000 USD per engineer-week."],
        ],
        "metrics": ["Overall speedup (Amdahl)|1 / ((1 - cpu_share / 100) + cpu_share / 100 / hotspot_speedup)|{:.2f}x", "Monthly compute saved|monthly_cost * (1 - ((1 - cpu_share / 100) + cpu_share / 100 / hotspot_speedup))|${:,.0f}", "Payback in months|port_weeks * 4000 / (monthly_cost * (1 - ((1 - cpu_share / 100) + cpu_share / 100 / hotspot_speedup)))|{:.1f}"],
    },
}
