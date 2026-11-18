"""Playbooks for the QA and Test Automation agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "04-qa-test-automation/01-test-plan-architect": {
        "fields": ["criteria_count|Acceptance criteria|number|12", "cases_per_criterion|Average test cases per criterion|number|4", "minutes_per_case|Minutes to automate one case|number|30", "risks|Top risks|list|Token replay, Email delivery delay, Clock skew, Link opened on another device", "platforms|Platforms in scope|list|Chrome, Safari, iOS app, Android app"],
        "sections": [
            ["Scope", "Feature: {input}", "Platforms: {platforms}", "Trace every acceptance criterion to at least one test; untraced criteria are untested promises."],
            ["Risk weighting", "*{risks}", "Score each risk 1 to 5 for likelihood and impact; test depth is proportional to the product. Score 15 or more gets exploratory plus automated negative tests."],
            ["Test matrix", "Cover each criterion with a happy path, a boundary (expiry, limits), a negative (invalid, expired, reused) and a permission case.", "Use equivalence classes and boundary values; for time limits test just before, at and just after the limit."],
            ["Levels and automation", "Push logic to unit tests, contracts to API tests and keep UI end-to-end tests to the critical journeys (the test pyramid: roughly 70 unit, 20 integration, 10 end-to-end).", "Non-functional: security (replay, enumeration), performance at expected load, accessibility, and observability of failures."],
            ["Entry and exit", "Entry: criteria reviewed, test data and environments ready. Exit: no open critical or high defects, all critical-path tests green, risk items signed off.", "Report coverage by risk, not by test count."],
        ],
        "metrics": ["Planned test cases|criteria_count * cases_per_criterion|{:,.0f}", "Automation effort (hours)|criteria_count * cases_per_criterion * minutes_per_case / 60|{:,.1f}"],
    },
    "04-qa-test-automation/02-edge-case-hunter": {
        "fields": ["field_count|Number of fields|number|3", "timezones|Time zones to test|list|America/New_York, Europe/London, Pacific/Auckland, Asia/Kolkata", "limits|Documented limits|list|amount greater than 0, amount at most 1,000,000.00, scheduled_at not in the past", "locales|Locales and scripts|list|en-US, de-DE (comma decimal), ar (right to left), ja-JP"],
        "sections": [
            ["Schema", "Fields: {input}", "{field_count} fields; documented limits are listed below.", "*{limits}"],
            ["Boundary vectors", "For every numeric limit test min minus one step, min, min plus one step, max minus one step, max, max plus one step. For decimals include 0.00, 0.001, 0.005 (rounding), 999999.995 and very long digit strings.", "Add zero, negative zero, NaN, Infinity, and values that overflow 32-bit and 53-bit integers (2147483648, 9007199254740993)."],
            ["Empty and malformed", "Null, missing key, empty string, whitespace only, a single space, very long strings (10,000 characters), wrong type (string for number), duplicated keys.", "Currency: lowercase code, unknown code (XXX), non-ISO symbol, currency with 0 or 3 decimals (JPY, KWD)."],
            ["Unicode and locale", "Test combining characters, emoji, zero-width joiner, right-to-left marks, homoglyphs, and normalisation forms NFC versus NFD. Locales: {locales}", "Check truncation at byte versus character limits and collation order."],
            ["Time and DST", "Time zones: {timezones}", "Test the DST gap (a nonexistent local time such as 02:30 on spring forward), the DST overlap (an ambiguous hour on fall back), 29 February, end of month, year 2038, UTC offsets with 30 or 45 minutes, and timestamps without an offset."],
        ],
        "metrics": ["Minimum vectors (about 12 per field)|field_count * 12|{:,.0f}"],
    },
    "04-qa-test-automation/03-playwright-scripter": {
        "fields": ["base_url|Base URL|text|http://localhost:5173", "test_user|Test account|text|qa-user@example.com (seeded fixture)", "browsers|Browsers|list|chromium, firefox, webkit", "retries|CI retries|number|2", "critical_assertion|Final assertion|text|Deployment status badge shows Deployed"],
        "sections": [
            ["Flow", "User flow: {input}", "Start at {base_url} as {test_user}."],
            ["Locator rules", "Prefer getByRole with an accessible name, then getByLabel, getByText, and getByTestId for ambiguous elements. Avoid CSS chains and XPath tied to layout.", "A test that cannot find an element by role is often exposing an accessibility bug."],
            ["No sleeps", "Never use waitForTimeout. Rely on auto-waiting actions and web-first assertions (expect(locator).toBeVisible(), toHaveText) that retry until the timeout. Wait for network by awaiting the response, not by time.", "Final check: {critical_assertion}"],
            ["Isolation and data", "Each test creates its own data through the API, signs in via a saved storageState, and cleans up. Never depend on the order of tests or shared accounts.", "Run in parallel with one worker per file; stub third-party services with route mocking."],
            ["Configuration", "Browsers: {browsers}. Set retries to {retries} on CI only, trace on first retry, screenshot and video on failure.", "Treat any test that needs a retry to pass as flaky and fix it within a week."],
        ],
        "metrics": [],
    },
    "04-qa-test-automation/04-flaky-test-triager": {
        "fields": ["failed_runs|Failed runs|number|3", "total_runs|Total runs observed|number|20", "runs_per_day|CI runs per day|number|100", "minutes_per_run|Minutes per CI run|number|12", "suspect|Suspected cause|text|Modal backdrop animation not finished before click"],
        "sections": [
            ["Failure evidence", "Logs: {input}", "Failed {failed_runs} of {total_runs} runs. Suspected cause: {suspect}."],
            ["Classify the cause", "Race or ordering: waits for UI or async state with no condition. Clock: dates, timeouts, time zones, sleeps. I/O: network, disk, ports, shared files. Shared state: test order, leaked data, global singletons. Resource: CPU starvation or memory on shared runners.", "Look at the failure message first: timeouts waiting for an element mean race; assertion on a value off by one hour means clock."],
            ["Reproduce", "Run the single test 100 times in a loop, with CPU throttling and in parallel with other tests. Use rr or trace viewers for a captured failure.", "If it only fails in CI, compare runner size, parallelism and test order."],
            ["Fix, then quarantine", "Fix by waiting on a condition not a time, injecting a fake clock, using unique ports and data, and isolating state. Quarantine rule: move to a quarantine suite after 2 flaky failures in 14 days, with an owner and a 7-day deadline.", "Never solve flakiness with a bigger timeout alone."],
            ["Metrics", "Track flake rate per test and for the suite; fail the build on new tests that flake in a 20-run pre-merge check.", "A retry that passes is data, not a success."],
        ],
        "metrics": ["Flake rate|failed_runs / total_runs|{:.0%}", "Wasted CI minutes per day if rerun|failed_runs / total_runs * runs_per_day * minutes_per_run|{:,.0f}"],
    },
    "04-qa-test-automation/05-api-fuzz-generator": {
        "fields": ["auth|Authentication|text|Bearer token for a low-privilege test tenant", "max_body_kb|Documented max body size (KB)|number|1024", "budget_cases|Fuzz cases to run|number|5000", "cases_per_sec|Request rate (cases per second)|number|50", "expected_errors|Expected error contract|text|400 with a problem JSON body, never 500 and never a stack trace"],
        "sections": [
            ["Target", "Endpoint: {input}", "Auth: {auth}. Expected behaviour on bad input: {expected_errors}."],
            ["Malformed structure", "Truncated JSON, trailing commas, duplicate keys, deeply nested arrays (10,000 levels), invalid UTF-8, a BOM, wrong Content-Type, empty body, and an array where an object is expected.", "A parser error must produce a 400, never a 500 or a hang."],
            ["Type confusion", "Send a number for a string, null for required, an object for a string, a list of 1 million items, booleans as strings, and numbers like 1e999 and -0.", "For string fields that hold YAML or file paths add path traversal (../../etc/passwd), null bytes and template injection markers."],
            ["Size and rate", "Bodies at the limit ({max_body_kb} KB), one byte over, and 100x over to check the 413 response. Use very long header values and many query parameters.", "Check compression bombs and slow-body uploads for resource exhaustion."],
            ["Run plan", "Run {budget_cases} cases at {cases_per_sec} per second against staging only, record status codes, latency and server logs, and flag any 5xx, hang above 5 seconds or memory growth.", "Add every crash as a permanent regression case in the corpus."],
        ],
        "metrics": ["Fuzz run time (minutes)|budget_cases / cases_per_sec / 60|{:.1f}", "Oversize body to test (KB)|max_body_kb + 1|{:,.0f}"],
    },
    "04-qa-test-automation/06-coverage-gap-finder": {
        "fields": ["branch_pct|Branch coverage now (percent)|number|64", "target_pct|Branch coverage target (percent)|number|85", "total_branches|Total branches|number|420", "minutes_per_test|Minutes to write one branch test|number|15", "critical_files|Critical files|list|llm_router.py, subscription_manager.py"],
        "sections": [
            ["Uncovered code", "Report: {input}", "Branch coverage {branch_pct} percent; target {target_pct} percent over {total_branches} branches."],
            ["Prioritisation", "Cover first: error handling and fallback branches, security and money paths, then branches that changed recently. Skip generated code, trivial getters and defensive asserts.", "Critical files: {critical_files}"],
            ["Test drafting", "For an uncovered else branch, find the condition in the if, build the smallest input that makes it false, and assert the specific outcome (return value, raised exception, log or state change).", "Use parametrised tests for related branches and fake the dependency (client, clock) that causes the path."],
            ["Quality over percentage", "Coverage shows what ran, not what was checked. Run mutation testing (mutmut, cargo-mutants) on the files you touch; a surviving mutant is a weak assertion.", "Reject tests without assertions."],
            ["Gates", "Enforce a floor in CI on changed lines (diff coverage 85 percent), not only the total, and never lower the floor without a recorded reason.", "Review the uncovered list monthly."],
        ],
        "metrics": ["Branches to cover|total_branches * (target_pct - branch_pct) / 100|{:,.0f}", "Estimated effort (hours)|total_branches * (target_pct - branch_pct) / 100 * minutes_per_test / 60|{:,.1f}"],
    },
    "04-qa-test-automation/07-regression-selector": {
        "fields": ["total_tests|Tests in the full suite|number|1800", "avg_test_sec|Average test duration (seconds)|number|4", "shards|Parallel CI shards|number|4", "impacted_pct|Estimated share of tests impacted (percent)|number|12", "always_run|Always-run smoke tests|list|auth smoke, billing smoke, API health"],
        "sections": [
            ["Change set", "Changed files: {input}", "Full suite: {total_tests} tests across {shards} shards."],
            ["Selection method", "Build a map from source files to tests using coverage data per test (or import graph analysis). Select tests whose covered files intersect the changed files, plus tests in the same package and the tests that changed.", "If the map is stale, fall back to the full suite: a missed regression costs more than extra minutes."],
            ["Always run", "*{always_run}", "Also run the full suite when changing shared config, lockfiles, build scripts, schema migrations or test infrastructure."],
            ["Risk controls", "Run the full suite nightly and before release; compare what selection missed against what the full run found, and track the miss rate (target below 1 percent).", "Add integration tests for each interface between modules, since import graphs miss runtime wiring."],
            ["Reporting", "Report selected versus skipped counts with a reason per skipped group so reviewers can challenge the selection.", "Rebuild the coverage map weekly."],
        ],
        "metrics": ["Full suite time (minutes)|total_tests * avg_test_sec / shards / 60|{:.1f}", "Selected tests|total_tests * impacted_pct / 100|{:,.0f}", "Selected run time (minutes)|total_tests * impacted_pct / 100 * avg_test_sec / shards / 60|{:.1f}"],
    },
    "04-qa-test-automation/08-accessibility-auditor": {
        "fields": ["wcag_target|Conformance target|text|WCAG 2.2 level AA", "contrast_ratio|Measured text contrast ratio|number|3.2", "text_px|Text size (px)|number|14", "assistive_tech|Assistive tech to test|list|NVDA with Firefox, VoiceOver with Safari, Keyboard only"],
        "sections": [
            ["Markup under review", "HTML: {input}", "Target: {wcag_target}"],
            ["Semantics and ARIA", "Use native elements first: button for actions, a for navigation, not div with onclick. A clickable div has no role, no keyboard focus and no Enter or Space activation (WCAG 4.1.2 and 2.1.1).", "First rule of ARIA: do not use ARIA if a native element exists. Every control needs an accessible name."],
            ["Keyboard and focus", "All functions must work with the keyboard alone; focus order follows reading order; focus is visible (2.4.7, and 2.4.11 in WCAG 2.2); dialogs trap focus and return it on close; no keyboard traps.", "Target size at least 24 by 24 CSS pixels (2.5.8)."],
            ["Landmarks and structure", "One main, a nav, header and footer landmarks, one h1, headings in order, labels bound to inputs, and a skip link.", "Announce dynamic changes with aria-live regions (polite for status, assertive for errors)."],
            ["Contrast", "Normal text needs 4.5:1; large text (24 px, or 19 px bold) needs 3:1; UI components and focus indicators 3:1. Measured: {contrast_ratio}:1 at {text_px} px.", "Do not rely on color alone for meaning; add text or icons."],
            ["Verification", "Run axe or Lighthouse, then test manually with: {assistive_tech}. Automated tools find about a third of issues.", "Block merges on new serious or critical violations."],
        ],
        "metrics": ["Contrast shortfall to 4.5:1|max(0, 4.5 - contrast_ratio)|{:.1f}", "Contrast margin versus 4.5:1|contrast_ratio / 4.5|{:.0%}"],
    },
    "04-qa-test-automation/09-load-test-modeler": {
        "fields": ["target_rps|Target requests per second|number|1200", "latency_ms|Expected average latency (ms)|number|80", "think_s|User think time (seconds)|number|1", "ramp_min|Ramp up (minutes)|number|5", "soak_min|Steady state (minutes)|number|30"],
        "sections": [
            ["SLA", "Target: {input}", "Aim for {target_rps} requests per second at an average latency of {latency_ms} ms."],
            ["Workload model", "Model users, not just requests: virtual users = rps x (response time + think time) (Little's law). Mix endpoints by real traffic share from production logs.", "Use an open model (constant arrival rate, executor constant-arrival-rate in k6) so a slow server cannot throttle the offered load."],
            ["Stages", "Ramp for {ramp_min} minutes, hold for {soak_min} minutes, then ramp down. Run a spike at 2x, a stress test to the breaking point and a 4 to 8 hour soak for leaks.", "Warm caches and connection pools before measuring."],
            ["Thresholds", "Encode the SLA in k6 thresholds: http_req_duration p(95) below the target, http_req_failed rate below 0.1 percent, and checks above 99.9 percent.", "Abort on threshold breach (abortOnFail) to protect shared environments."],
            ["Interpretation", "Look for the knee where latency rises faster than throughput. Correlate with CPU, connection pool waits, GC and database locks.", "Generate load from separate machines; monitor the generator's own CPU to avoid measuring the generator."],
        ],
        "metrics": ["Concurrent virtual users (Little's law)|target_rps * (latency_ms / 1000 + think_s)|{:,.0f}", "Requests at steady state|target_rps * soak_min * 60|{:,.0f}", "Total test duration (minutes)|2 * ramp_min + soak_min|{:.0f}"],
    },
    "04-qa-test-automation/10-bug-repro-distiller": {
        "fields": ["app_version|App version|text|2.4.1", "environment|Environment|text|Ubuntu 24.04, Electron app, Wayland", "attempts|Repro attempts|number|10", "reproduced|Times reproduced|number|7", "expected|Expected behaviour|text|Dialog stays open and the theme changes without a crash"],
        "sections": [
            ["Report", "Thread: {input}", "Version {app_version} on {environment}."],
            ["Minimal reproduction", "Strip the thread to: preconditions, numbered steps from a clean start, actual result, expected result ({expected}). Remove every step that can be dropped without changing the failure.", "Use delta debugging: remove half of the steps, test, and keep the half that still fails."],
            ["Determinism", "Reproduced {reproduced} of {attempts} attempts. A rate below 100 percent points to a race, timing, or data-dependent condition.", "Record the exact build, locale, time zone, feature flags, data and window state."],
            ["Evidence to attach", "Console log, stack trace, screen recording, HAR or request log, and the smallest dataset or config that triggers it.", "Add a failing automated test as soon as the repro is stable."],
            ["Severity", "S1: crash or data loss with no workaround. S2: major function broken with a workaround. S3: minor. Raise severity for regressions and for issues affecting enterprise accounts.", "Ask the reporter only for what is missing, not for the whole template again."],
        ],
        "metrics": ["Reproduction rate|reproduced / attempts|{:.0%}", "Attempts needed for 95% confidence of seeing it|3 / (reproduced / attempts)|{:.0f}"],
    },
}
