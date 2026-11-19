"""Playbooks for the QA & Test Automation agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "04-qa-test-automation/11-contract-test-designer": {
        "fields": ["consumer|Consumer service|text|Orders", "provider|Provider service|text|Customers", "consumers|Number of consumers of the provider|number|4", "interactions|Interactions to cover|number|7", "minutes_each|Minutes to write one contract test|number|25"],
        "sections": [
            ["Contract under test", "Contract: {input}", "Consumer: {consumer}. Provider: {provider}. {consumers} consumers depend on the provider.", "A contract test checks the part of an API a consumer actually uses, so the provider can change anything else."],
            ["What to put in the contract", "Request shape, the fields the consumer reads, their types and the error responses the consumer handles. Do not assert on fields the consumer ignores.", "Use matching rules (type, regex) instead of exact values, so tests do not break on data changes."],
            ["Provider verification", "Replay every consumer contract against the real provider in the provider's CI. A failing contract blocks the change or starts a conversation.", "Publish contracts and verification results to a broker so each team sees who depends on what."],
            ["Breaking changes", "Adding an optional field is safe. Removing a field, renaming it, changing a type or making an optional field required breaks consumers.", "Use the broker's can-i-deploy check before releasing either side."],
            ["Rollout", "Start with the consumer that breaks most often, cover its {interactions} interactions, then add the other consumers.", "Keep a few end-to-end tests for the full flow, but let contracts catch interface drift."],
        ],
        "metrics": ["Hours to write the first contract suite|interactions * minutes_each / 60|{:.1f}", "Contracts to verify per provider release|interactions * consumers|{:,.0f}"],
    },
    "04-qa-test-automation/12-test-data-synthesizer": {
        "fields": ["tables|Tables to fill|number|12", "prod_rows|Production rows in the biggest table|number|9000000", "test_rows|Rows you want in tests|number|50000", "pii_columns|Columns holding personal data|number|9", "edge_share|Share of rows that are edge cases (0 to 1)|number|0.05"],
        "sections": [
            ["Schema", "Schema: {input}", "{tables} tables, the biggest with {prod_rows} rows in production. Target: {test_rows} test rows.", "Good test data keeps the shape of production (relationships, skew, nulls) without containing production people."],
            ["Generate, do not copy", "Generate rows from the schema with a seeded generator, so every run gives the same data. If you must copy production, mask the {pii_columns} personal columns first.", "Keep foreign keys valid, and generate parents before children."],
            ["Distributions", "Production data is skewed: a few customers own most orders. Draw sizes and counts from a long-tailed distribution, not a uniform one.", "Include realistic nulls, empty strings, long text and non-English characters."],
            ["Edge cases", "Add a set of rows for each constraint boundary: zero, maximum, leap day, duplicate-looking names, time zone changes and deleted parents.", "Keep these in a small fixed fixture so a failure is easy to read."],
            ["Privacy and refresh", "Never put real emails or phone numbers in test environments. Use reserved domains such as example.com, and rebuild the data on every schema change.", "Version the generator with the schema and run it in CI."],
        ],
        "metrics": ["Test data as a share of production|test_rows / prod_rows|{:.2%}", "Edge-case rows in the test set|test_rows * edge_share|{:,.0f}"],
    },
    "04-qa-test-automation/13-mutation-test-reviewer": {
        "fields": ["module|Module|text|pricing.py", "mutants|Mutants generated|number|240", "killed|Mutants killed by tests|number|168", "equivalent|Survivors judged equivalent (no behaviour change)|number|8", "minutes_each|Minutes to write a test per survivor|number|10"],
        "sections": [
            ["Report", "Report: {input}", "Module: {module}. {killed} of {mutants} mutants were killed.", "A mutant is a small deliberate bug. If the tests still pass, they would also pass for a real bug of that kind."],
            ["Reading the score", "Coverage shows which lines ran, the mutation score shows whether the tests would notice a change. High coverage with a low score means tests that execute code but assert little.", "Aim for 80 percent on critical logic such as pricing, permissions and money."],
            ["Survivors to act on", "Group survivors by type: changed comparison operators (boundary tests), changed arithmetic (missing exact assertions), removed calls (side effects not checked).", "For each survivor write the smallest test that fails with the mutant and passes with the real code."],
            ["Equivalent mutants", "Some survivors change nothing observable, such as reordering equal operations. Mark {equivalent} of them as equivalent and exclude them from the score.", "Do not chase 100 percent. Cost per survivor rises quickly."],
            ["Process", "Run mutation tests on changed files in CI and the full suite weekly, and review new survivors in the pull request.", "Focus the effort on the modules where a bug costs money."],
        ],
        "metrics": ["Mutation score|killed / mutants|{:.0%}", "Survivors left to review|mutants - killed - equivalent|{:,.0f}", "Hours to write tests for the survivors|(mutants - killed - equivalent) * minutes_each / 60|{:.1f}"],
    },
    "04-qa-test-automation/14-visual-regression-triager": {
        "fields": ["page|Page or flow|text|Checkout", "diffs|Screenshot diffs|number|48", "noise|Diffs caused by rendering noise|number|30", "intended|Diffs from an approved design change|number|12", "minutes_each|Minutes to review one diff|number|2"],
        "sections": [
            ["Diffs under review", "Diffs: {input}", "Page: {page}. {diffs} diffs: {noise} noise, {intended} intended.", "A visual test is only useful if a failure usually means a real problem. Noise trains people to approve everything."],
            ["Triage order", "First separate noise (anti-aliasing, font loading, animation frames, dates), then intended changes, then real regressions. Fix the real ones before approving anything.", "Real regressions look like missing elements, overlap, cut-off text or layout shifts."],
            ["Remove the noise", "Pin the browser and font versions, disable animations, freeze the clock and mask dynamic regions. Set a small tolerance for anti-aliasing, not a large one.", "Run the screenshots in the same container image everywhere."],
            ["Approving changes", "Approve intended changes in the pull request that makes them, with the designer or product owner looking at the diff.", "Never bulk-approve. Review each baseline update and keep the previous baseline in version control."],
            ["Coverage", "Capture the key states, not every page: empty, loading, error, long text, right-to-left and small screen.", "Track the noise rate per week and fix it when it passes 5 percent."],
        ],
        "metrics": ["Diffs that need a real decision|diffs - noise - intended|{:,.0f}", "Noise rate|noise / diffs|{:.0%}", "Review time wasted on noise (minutes)|noise * minutes_each|{:,.0f}"],
    },
    "04-qa-test-automation/15-device-matrix-planner": {
        "fields": ["ios_share|iOS share of users (percent)|number|62", "top_devices|Devices in the proposed matrix|number|12", "coverage|Share of users the matrix covers (percent)|number|85", "run_minutes|Minutes per device per run|number|40", "runs_week|Full runs per week|number|10"],
        "sections": [
            ["Usage", "Analytics: {input}", "iOS share: {ios_share} percent. Proposed matrix: {top_devices} devices covering {coverage} percent of users.", "Choose devices by the users you would hurt, not by what is on the shelf."],
            ["Building the matrix", "Take devices and OS versions from your own analytics until you cover about 85 to 90 percent of sessions. Add the oldest supported OS, the smallest screen and the largest screen.", "Include at least one low-memory Android device. Performance bugs hide on slow hardware."],
            ["Risk-based additions", "Add devices with known problems (notches, foldables, custom Android skins) and the models of your biggest customers.", "Drop a device when its share falls under 1 percent and nobody has reported a device-specific bug."],
            ["Where to run", "Automate smoke tests on a cloud device farm for the whole matrix and keep a few physical devices for manual checks of camera, push and biometrics.", "Run the full matrix before release and a small subset on every pull request."],
            ["Review", "Update the matrix every quarter from fresh analytics and after each major OS release.", "Record which bugs were device-specific to justify each entry."],
        ],
        "metrics": ["Android share of users (percent)|100 - ios_share|{:.0f}", "Device hours per week|top_devices * run_minutes * runs_week / 60|{:,.0f}"],
    },
    "04-qa-test-automation/16-test-pyramid-auditor": {
        "fields": ["unit|Unit tests|number|1800", "integration|Integration tests|number|240", "e2e|End-to-end tests|number|160", "e2e_minutes|End-to-end suite time (minutes)|number|52", "e2e_flaky|End-to-end flaky rate (0 to 1)|number|0.09"],
        "sections": [
            ["Test mix", "Counts: {input}", "Unit {unit}, integration {integration}, end-to-end {e2e}.", "The pyramid is a guide to cost: many fast unit tests, fewer integration tests and a few end-to-end tests of the key journeys."],
            ["Shape", "Unit should be most of the suite (about 70 percent), integration about 20 and end-to-end about 10. An hourglass or ice cream cone shape means slow feedback and fragile tests.", "Compare cost: one end-to-end test usually costs as much to run and maintain as a hundred unit tests."],
            ["Speed", "End-to-end takes {e2e_minutes} minutes. Developers stop waiting above about 10 minutes. Run end-to-end tests in parallel shards and only the critical ones on every pull request.", "Move checks down: test business rules at unit level, and test the browser only for what the browser does."],
            ["Reliability", "A flaky rate of {e2e_flaky} means one run in several fails for no reason. Quarantine flaky tests, fix them within a set time or delete them.", "Never retry silently. A retry hides the signal."],
            ["Plan", "For each end-to-end test, ask what it covers that a lower-level test could cover and move it down. Keep the test for the journey itself.", "Track suite time, flaky rate and escaped bugs together."],
        ],
        "metrics": ["Unit share of all tests|unit / (unit + integration + e2e)|{:.0%}", "End-to-end share of all tests|e2e / (unit + integration + e2e)|{:.0%}", "Flaky end-to-end tests|e2e * e2e_flaky|{:,.0f}"],
    },
    "04-qa-test-automation/17-exploratory-charter-writer": {
        "fields": ["feature|Feature|text|Bulk CSV import", "sessions|Sessions planned|number|6", "session_minutes|Minutes per session|number|90", "testers|Testers|number|2", "top_risk|Biggest risk|text|Partial import leaves duplicate or half-written records"],
        "sections": [
            ["Feature", "Feature: {input}", "{feature}: {sessions} sessions of {session_minutes} minutes. Biggest risk: {top_risk}.", "Exploratory testing is learning, designing and running tests at the same time, guided by a short mission."],
            ["Charter format", "Explore [area] with [resources or technique] to discover [information]. For example: explore the import of malformed files with large and small CSVs to discover how errors are reported and whether partial data is saved.", "Keep a charter to one idea so a session can finish in its time box."],
            ["Session ideas", "Limits (empty file, one row, maximum rows, wide rows), encodings and delimiters, duplicates, cancel midway, run two imports at once, permissions and the email content.", "Use tours: the money tour, the back-alley tour and the interruption tour."],
            ["Notes and debrief", "Record what you tried, what you saw, bugs, questions and ideas for later. Hold a 10-minute debrief after each session with a lead.", "Track the split between setup, testing and bug writing."],
            ["Coverage", "Cover the top risk first: {top_risk}. Then fill the gaps shown by the session notes.", "Turn every confirmed bug into an automated test where it is cheap."],
        ],
        "metrics": ["Total exploratory hours|sessions * session_minutes / 60|{:.1f}", "Hours per tester|sessions * session_minutes / 60 / testers|{:.1f}"],
    },
    "04-qa-test-automation/18-qa-release-checklist-builder": {
        "fields": ["release|Release|text|4.12", "tickets|Tickets in the release|number|14", "high_risk|High-risk tickets|number|3", "open_bugs|Open bugs at code freeze|number|5", "escapes|Bugs that escaped the last release|number|4"],
        "sections": [
            ["Release", "Scope: {input}", "Release {release}: {tickets} tickets, {high_risk} high risk, {open_bugs} open bugs, {escapes} escapes from the last release.", "A checklist is a memory aid for the things that were forgotten before. Build it from your own past escapes."],
            ["Entry criteria", "Code freeze reached, builds green, test environment matches production, test data ready and release notes drafted.", "Do not start the final test pass on an unstable build."],
            ["Test pass", "Run the automated regression, the smoke tests on every platform, and manual checks for the {high_risk} high-risk tickets, including upgrade and migration from the previous version.", "Check what was missed last time: {escapes} escapes means those areas get an extra look."],
            ["Exit gates", "No open severity-1 or severity-2 bugs, known issues documented, performance within 5 percent of the last release, security scan clear and rollback tested.", "A named person signs off for QA, product and operations."],
            ["After release", "Watch error rates, support tickets and key business metrics for 24 hours, with a named owner and a rollback trigger.", "Hold a short review of escapes and add a checklist item for each."],
        ],
        "metrics": ["High-risk share of the release|high_risk / tickets|{:.0%}", "Bugs still to resolve or accept|open_bugs|{:,.0f}"],
    },
    "04-qa-test-automation/19-l10n-test-planner": {
        "fields": ["locales|Locales to launch|number|4", "strings|Translatable strings|number|3200", "rtl|Right-to-left locales|number|1", "expansion|Expected text growth in the longest language (0 to 1)|number|0.35", "tester_minutes|Minutes to review one screen per locale|number|6", "screens|Screens to review per locale|number|40"],
        "sections": [
            ["Scope", "Locales: {input}", "{locales} locales and {strings} strings, {rtl} right-to-left.", "Internationalization (the code can handle any locale) comes before localization (the translation for one locale). Test both."],
            ["Formats", "Check dates, times, time zones, numbers, currency symbols and placement, phone numbers, addresses, names and sort order for each locale.", "Test with the locale of the user, not of the server."],
            ["Layout", "Text grows by up to {expansion} in some languages, so check buttons, tables and menus for truncation. Check right-to-left mirroring of layout and icons, and fonts that cover every script.", "Use pseudo-localization (accented, stretched text) in development to find hard-coded text early."],
            ["Content", "Check plural rules, gender and context for each string, strings built by joining parts, untranslated leftovers and screenshots of the translated UI in context.", "Send translators context and a glossary, and review the first batch with a native speaker."],
            ["Automation", "Run screenshot tests per locale and a check that every string has a translation. Add locales to the release checklist.", "Block hard-coded strings with a lint rule."],
        ],
        "metrics": ["Review hours per locale|screens * tester_minutes / 60|{:.1f}", "Review hours for all locales|screens * locales * tester_minutes / 60|{:.1f}"],
    },
    "04-qa-test-automation/20-security-test-case-writer": {
        "fields": ["flow|Flow under test|text|Password reset by email link", "token_minutes|Token lifetime (minutes)|number|60", "requests_hour|Reset requests per hour you allow per account|number|20", "limit_target|Limit you want per hour|number|3", "cases|Test cases you plan|number|14"],
        "sections": [
            ["Flow", "Flow: {input}", "Under test: {flow}. Token lifetime: {token_minutes} minutes.", "Security tests ask what a hostile user could do with each step, in addition to checking that a good user succeeds."],
            ["Authentication cases", "Reuse of a used token, an expired token, a token for another account, a guessed or modified token, and a reset that does not end other sessions.", "Check the token is long, random, single-use and stored hashed."],
            ["Authorization cases", "Change the user id or email in each request (insecure direct object reference), call the endpoint without a session and with a lower role, and check admin paths.", "Responses must not reveal whether an email exists."],
            ["Abuse cases", "Today {requests_hour} requests an hour are allowed. Test rate limits per account, per address and per device, and check that your target of {limit_target} per hour holds.", "Test email flooding of a victim and brute force of the token."],
            ["Input cases", "Long values, unicode, injection strings in every field, header injection in the email, open redirects in return links and malformed JSON.", "Automate these as regression tests and run a dynamic scan on every release."],
        ],
        "metrics": ["Requests allowed per day above the target|(requests_hour - limit_target) * 24|{:,.0f}", "Token lifetime in hours|token_minutes / 60|{:.1f}"],
    },
}
