"""Playbooks for the Software Engineering agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "02-software-engineering/11-error-handling-auditor": {
        "fields": ["language|Language|text|Python", "call_site|Call that can fail|text|Payment gateway charge", "failures_week|Failures seen per week|number|85", "silent_share|Share of failures that are swallowed (0 to 1)|number|0.4", "impact|Impact of a silent failure|text|Orders marked paid without taking payment"],
        "sections": [
            ["Code under review", "Excerpt: {input}", "Language: {language}. Risky call: {call_site}.", "An error handler decides three things: who is told, what state the data is left in, and whether to try again."],
            ["Swallowed exceptions", "A bare catch with no logging hides faults. Catch the narrowest error type you can handle and log the rest with context.", "Impact here: {impact}. Never continue as if a failed step succeeded."],
            ["Error messages and context", "Include the operation, the identifiers involved and the original cause. Do not log secrets or full card numbers.", "Wrap errors, do not replace them, so the stack trace survives."],
            ["Retries and idempotency", "Retry only transient failures (timeouts, 429, 503) with exponential backoff and jitter, a retry cap and an idempotency key for any charge.", "Never retry a non-idempotent call without a key: you may take payment twice."],
            ["Fix order", "First stop the silent success. Then add structured logging and an alert on the error rate, then add retries.", "Add a test that makes the call fail and asserts the order is not marked paid."],
        ],
        "metrics": ["Silent failures per week|failures_week * silent_share|{:,.0f}", "Silent failures per year|failures_week * silent_share * 52|{:,.0f}"],
    },
    "02-software-engineering/12-api-sunset-planner": {
        "fields": ["version|Version to retire|text|v1", "clients|Active clients on it|number|140", "calls_day|Calls per day|number|2100000", "top_share|Traffic share of the top 5 clients (0 to 1)|number|0.7", "notice_days|Notice period (days)|number|180"],
        "sections": [
            ["Retirement case", "Usage: {input}", "Version: {version}, {clients} clients, {calls_day} calls a day.", "Retire a version only when the replacement is stable and you can name every remaining caller."],
            ["Who to contact first", "The top 5 clients carry the traffic. Contact them personally, with a named engineer and a migration date.", "For the long tail, use email, a dashboard banner and a response header on every call."],
            ["Signals in the API", "Add Deprecation and Sunset headers with the date and a link to the guide. Log the client id of every call to the old version.", "Publish the date in the changelog, the docs and the status page."],
            ["Timeline", "Give {notice_days} days. Run brownouts (short planned failures) at 60, 30 and 7 days before the date so owners notice.", "Return 410 Gone with a pointer to the migration guide after the cutoff, not a silent failure."],
            ["Migration support", "Offer a mapping table of old to new fields, an SDK upgrade path and office hours.", "Track weekly traffic on the old version and extend only for named clients with a plan."],
        ],
        "metrics": ["Calls per day from the top 5 clients|calls_day * top_share|{:,.0f}", "Calls per day from the other clients|calls_day * (1 - top_share)|{:,.0f}", "Average calls per day per client|calls_day / clients|{:,.0f}"],
    },
    "02-software-engineering/13-feature-flag-cleaner": {
        "fields": ["flags|Total flags|number|214", "stale|Flags older than 6 months|number|88", "fully_on|Flags at 100 percent for 90+ days|number|31", "no_owner|Flags with no owner|number|40", "minutes_each|Minutes to remove one flag safely|number|45"],
        "sections": [
            ["Inventory", "Inventory: {input}", "{stale} of {flags} flags are older than 6 months and {fully_on} have been fully on for 90 days or more.", "A flag is short-lived (release), medium (experiment) or permanent (kill switch, entitlement). Only the first two should expire."],
            ["Which to remove first", "Remove fully-on release flags first: the code path is already the only path. Next remove flags at 0 percent that nobody owns.", "Keep kill switches and permission flags, but document them as permanent."],
            ["Ownership", "{no_owner} flags have no owner. Assign each to the team that owns the code, or to the author of the last change.", "Add owner and expiry fields to the flag definition so new flags cannot be created without them."],
            ["Safe removal steps", "Delete the flag check and the dead branch in one change, keep the tests for the surviving path and remove the flag in the tool after deploy.", "Check dashboards and configs that read the flag, and remove flags in batches of ten, not all at once."],
            ["Prevention", "Add a CI check that fails when a flag is past its expiry date and report flag age in the weekly engineering review.", "Cap the number of live release flags per team."],
        ],
        "metrics": ["Hours to remove the fully-on flags|fully_on * minutes_each / 60|{:.1f}", "Share of flags that are stale|stale / flags|{:.0%}"],
    },
    "02-software-engineering/14-module-boundary-checker": {
        "fields": ["modules|Modules in scope|number|24", "cycles|Dependency cycles found|number|3", "violations|Layer violations found|number|11", "rule|Layering rule you want|text|UI calls services, services call domain, nothing calls UI", "owner|Team that owns the boundaries|text|Platform architecture"],
        "sections": [
            ["Graph readout", "Graph: {input}", "{modules} modules, {cycles} cycles, {violations} layer violations. Owner: {owner}.", "A module boundary is a promise: others may use only the public surface, and the inside can change freely."],
            ["Cycles", "Cycles force modules to change and deploy together. Break each cycle by extracting the shared concept into a lower module or by inverting one dependency with an interface.", "Start with the smallest cycle: two modules that import each other."],
            ["Layer rule", "Rule: {rule}.", "Enforce it with an automated check in CI (dependency lint or architecture tests) so the rule holds after you fix today's violations."],
            ["Hidden coupling", "Two modules reading the same database table are coupled even without an import. Give each table one owning module and expose reads through its interface.", "Shared global state, singletons and utility modules that grow without limit are the other usual sources."],
            ["Plan", "Fix cycles first, then violations in the most-changed modules, and add the CI check before new code arrives.", "Track violations per week. The number should fall, not rise."],
        ],
        "metrics": ["Violations per module|violations / modules|{:.2f}", "Issues to fix in total|cycles + violations|{:,.0f}"],
    },
    "02-software-engineering/15-logging-quality-reviewer": {
        "fields": ["service|Service|text|checkout-api", "lines_day|Log lines per day|number|45000000", "cost_gb|Ingest cost per GB (USD)|number|0.5", "bytes_line|Average bytes per line|number|400", "debug_share|Share of lines at debug level (0 to 1)|number|0.55"],
        "sections": [
            ["Samples under review", "Samples: {input}", "Service: {service}.", "A log line should answer who, what, where and why, with enough context to find it again."],
            ["Sensitive data", "Never log passwords, tokens, full card numbers or personal data. Mask or hash identifiers, and scan logs in CI for patterns such as emails and card numbers.", "Treat any sensitive value found in logs as an incident: purge it and rotate the secret."],
            ["Structure", "Use structured logs (JSON) with fixed keys: timestamp, level, service, request id, user id, event name and a short message.", "Do not build messages by joining strings. Pass fields so they stay searchable."],
            ["Levels and noise", "Error means a person should look. Warn means unexpected but handled. Info is for business events. Debug is off by default in production.", "Delete lines such as the one that says only 'here'. They cost money and carry nothing."],
            ["Cost of debug logging", "Sample or disable debug logs in production, and keep a short retention for them.", "Add a trace id to every line so a request can be followed across services."],
        ],
        "metrics": ["Ingest volume per day (GB)|lines_day * bytes_line / 1000000000|{:,.1f}", "Monthly ingest cost (USD)|lines_day * bytes_line / 1000000000 * cost_gb * 30|${:,.0f}", "Monthly cost of debug lines (USD)|lines_day * bytes_line / 1000000000 * cost_gb * 30 * debug_share|${:,.0f}"],
    },
    "02-software-engineering/16-cache-strategy-advisor": {
        "fields": ["reads_s|Reads per second|number|800", "writes_s|Writes per second|number|2", "hit_rate|Expected cache hit rate (0 to 1)|number|0.92", "origin_ms|Origin response time (ms)|number|120", "ttl_s|Acceptable staleness (seconds)|number|60"],
        "sections": [
            ["Access pattern", "Pattern: {input}", "{reads_s} reads and {writes_s} writes per second. Staleness allowed: {ttl_s} seconds.", "Caches pay off when reads far outnumber writes and a small set of keys gets most of the traffic."],
            ["Where to cache", "Use a CDN for public pages, an in-process cache for tiny hot values and a shared cache (Redis or similar) for data many servers read.", "Each layer you add makes invalidation harder, so add the layer that removes the most load first."],
            ["Keys and expiry", "Build keys from the resource, version and any variant (language, currency). Set a time to live no longer than {ttl_s} seconds and add random jitter so keys do not expire together.", "Cache negative results (not found) for a short time to stop repeated misses."],
            ["Invalidation", "Prefer expiry plus explicit deletion on write. Publish an invalidation event from the writer for keys that must change at once.", "Never cache per-user data under a shared key."],
            ["Stampedes and failure", "On a miss, let one request rebuild the value while others wait or serve the stale copy. If the cache is down, protect the origin with limits instead of sending all traffic to it.", "Monitor hit rate, miss latency and evictions."],
        ],
        "metrics": ["Origin reads per second after caching|reads_s * (1 - hit_rate)|{:,.0f}", "Average response time (ms)|hit_rate * 2 + (1 - hit_rate) * origin_ms|{:,.1f}", "Reduction in origin load|hit_rate|{:.0%}"],
    },
    "02-software-engineering/17-type-safety-planner": {
        "fields": ["language|Language|text|TypeScript", "any_count|Uses of any or untyped values|number|1900", "per_week|Uses you can remove per week|number|60", "bug_share|Share of bugs caused by type errors (0 to 1)|number|0.22", "bugs_quarter|Bugs last quarter|number|140"],
        "sections": [
            ["Starting point", "Stats: {input}", "Language: {language}. {any_count} untyped uses, {bug_share} of last quarter's bugs came from type errors.", "Aim for fewer runtime surprises, not for a perfect score. Start where a wrong type costs most."],
            ["Order of work", "Type the boundaries first: API inputs and outputs, database rows and shared utilities. Then the core domain, then the edges.", "Turn on the strictness flags one at a time and fix each flag's errors before the next."],
            ["Ratchet in CI", "Record today's count as a baseline and fail the build if it rises. Lower the baseline each time you remove uses.", "New code must be fully typed. Old code improves as it is touched."],
            ["Parsing at the edges", "Validate external data at the boundary with a schema library and derive types from the schema, so types and checks cannot drift apart.", "Avoid type assertions that only silence the compiler."],
            ["Measuring the benefit", "Count type-related bugs per quarter and compare with the start. Share the trend, not the lint score.", "Review the ratchet every month and raise the bar when it is easy to clear."],
        ],
        "metrics": ["Weeks to remove all untyped uses|any_count / per_week|{:.0f}", "Type-related bugs last quarter|bugs_quarter * bug_share|{:,.0f}"],
    },
    "02-software-engineering/18-idempotency-reviewer": {
        "fields": ["endpoint|Endpoint or consumer|text|POST /payments", "retry_rate|Share of requests that are retried (0 to 1)|number|0.03", "requests_day|Requests per day|number|120000", "avg_amount|Average amount (USD)|number|48", "key_ttl_h|How long you keep keys (hours)|number|24"],
        "sections": [
            ["What is being reviewed", "Spec: {input}", "Endpoint: {endpoint}.", "Clients, proxies and queues retry. Assume every request and every message can arrive twice, because it can."],
            ["Idempotency keys", "Require a client-generated key in a header. Store the key with the result in the same transaction as the change, under a unique constraint.", "Return the stored result for a repeated key. Reject the same key with a different body."],
            ["Consumers", "Queues and webhooks deliver at least once. Record each processed event id and skip duplicates, or make the handler a pure upsert.", "Order is not guaranteed either: ignore events older than the stored version."],
            ["Retention", "Keep keys at least {key_ttl_h} hours, longer than the longest client retry window.", "Expired keys let a late retry run twice, so make that window longer than any retry policy you control."],
            ["Tests", "Test a double-submit, a retry after a timeout where the first call succeeded, and a crash between charging and recording.", "Run the duplicate tests concurrently, not only one after another."],
        ],
        "metrics": ["Retried requests per day|requests_day * retry_rate|{:,.0f}", "Money at risk of double charging per day (USD)|requests_day * retry_rate * avg_amount|${:,.0f}"],
    },
    "02-software-engineering/19-code-owner-mapper": {
        "fields": ["area|Code area|text|payments/", "commits|Commits in the last 12 months|number|480", "top_author_commits|Commits by the top author|number|298", "authors_left|Authors who have left|number|3", "reviewers|People who review this area|number|2"],
        "sections": [
            ["Ownership readout", "History: {input}", "Area: {area}. {commits} commits, {top_author_commits} by one author.", "Ownership means someone is accountable for the quality, the reviews and the answers to questions about the code."],
            ["Bus factor", "If one person wrote most of an area, losing them stops all work there. Aim for at least two people who can change and review each area.", "{authors_left} former authors means knowledge has already left the team."],
            ["Orphaned areas", "List areas with no commits for 6 months or more and no named owner. Decide for each: assign, archive or delete.", "Unowned code that still runs in production is the highest-risk kind."],
            ["CODEOWNERS file", "Map each directory to a team, not a person, and require review from that team. Keep the file in CI so a missing owner fails the check.", "Review it every quarter against the org chart."],
            ["Knowledge transfer", "Pair the main author with a second person on the next change, write a short architecture note and record a walkthrough.", "Rotate reviewers so {reviewers} does not stay the answer to every question."],
        ],
        "metrics": ["Share of commits by the top author|top_author_commits / commits|{:.0%}", "Commits by everyone else|commits - top_author_commits|{:,.0f}"],
    },
    "02-software-engineering/20-codebase-onboarding-guide": {
        "fields": ["repo|Repository|text|acme/platform monorepo", "setup_hours|Hours setup takes today|number|8", "setup_goal|Setup goal (hours)|number|1", "hires_year|New engineers per year|number|12", "first_task|Suggested first task|text|Fix a small bug in the notifications service"],
        "sections": [
            ["Overview", "Overview: {input}", "Repository: {repo}.", "Write for a new engineer on day one: what the system does, who uses it and where the code for each part lives."],
            ["Setup that works", "Give one command that builds, seeds data and runs the tests. Run it on a fresh machine every month so the guide stays true.", "Setup today takes {setup_hours} hours. The goal is {setup_goal}."],
            ["Map of the code", "Add a diagram of the main services and a table: folder, purpose, owner, how to run its tests.", "Link to the three files that explain the most about how the system works."],
            ["First week", "Day 1 setup, day 2 read the map and trace one request, day 3 first task: {first_task}, day 5 first merge.", "Assign a buddy, and a mentor outside the team for questions that feel too small to ask."],
            ["Team norms", "Branch naming, pull request size, review time target, test expectations and how to ask for help.", "Ask each new engineer to fix any unclear step in the guide as their first documentation change."],
        ],
        "metrics": ["Hours saved per hire if setup meets the goal|setup_hours - setup_goal|{:,.1f}", "Hours saved per year|(setup_hours - setup_goal) * hires_year|{:,.0f}"],
    },
}
