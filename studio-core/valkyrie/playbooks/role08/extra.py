"""Playbooks for the Developer Relations & Docs agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "08-developer-relations-docs/11-migration-guide-writer": {
        "fields": ["from_version|Old version|text|2.9", "to_version|New version|text|3.0", "breaking|Breaking changes|number|7", "minutes_each|Average minutes for a user to fix one change|number|20", "users|Estimated active users of the library|number|8000", "upgrade_share|Share of users who upgrade in the first year (0 to 1)|number|0.2"],
        "sections": [
            ["Scope", "Changes: {input}", "Upgrade from {from_version} to {to_version}. {breaking} breaking changes.", "A migration guide gets a reader from the old version to the new one with the least risk and the fewest surprises."],
            ["Before you start", "State who needs to act, the supported upgrade path (go to the last minor release of the old major first), the end of support date for the old version and how long the upgrade usually takes.", "Show the deprecation warnings that the last release already printed."],
            ["Change by change", "For each breaking change give a heading, why it changed, a before snippet, an after snippet and how to find affected code with a search or a codemod.", "Order from most to least common so most readers finish early."],
            ["Safe order of steps", "Upgrade in a branch, fix compiler or lint errors, run tests, deploy to staging, then production behind a flag where you can. Give a rollback step.", "Pin the version in your lock file so nobody upgrades by accident."],
            ["Help and tooling", "Link a codemod or script, a checklist, a list of known issues and a place to ask questions. Collect questions in the first month and add them to the guide.", "Estimated effort is {minutes_each} minutes per change, per codebase."],
        ],
        "metrics": ["Estimated minutes to migrate one codebase|breaking * minutes_each|{:,.0f}", "Total hours the community will spend|breaking * minutes_each * users * upgrade_share / 60|{:,.0f}"],
    },
    "08-developer-relations-docs/12-error-reference-writer": {
        "fields": ["codes|Error codes to document|number|64", "documented|Codes already documented|number|22", "tickets_month|Support tickets a month about errors|number|420", "error_share|Share of tickets caused by the top 10 errors (0 to 1)|number|0.6", "deflect|Tickets a good page can deflect (0 to 1)|number|0.3"],
        "sections": [
            ["Catalog", "Errors: {input}", "{codes} codes, {documented} documented. {tickets_month} tickets a month mention errors.", "An error page is read by someone who is stuck. Put the fix first and keep the page short."],
            ["Page structure", "Title with the code and name, a one-sentence meaning, the likely causes in order of frequency, how to fix each, an example request and response and a link to related errors.", "Make the code searchable and keep the same URL for each code forever."],
            ["Writing causes and fixes", "Write the cause as a condition the reader can check: for example, more than 600 requests a minute. Give the exact header or field to inspect and the fix as a step.", "Say when it is not the reader's fault and they should contact support."],
            ["Where to show it", "Return the documentation URL in the error response itself and in the SDK exception message so the answer is one click away.", "Group codes by area in the navigation and add them to the site search."],
            ["Priorities", "Start with the top 10 errors by ticket volume, which cause {error_share} of tickets. Measure tickets per code before and after each page.", "Review quarterly and add pages for new codes in the same release that adds them."],
        ],
        "metrics": ["Codes still to document|codes - documented|{:,.0f}", "Tickets a month from the top 10 errors|tickets_month * error_share|{:,.0f}", "Tickets a month the pages could deflect|tickets_month * error_share * deflect|{:,.0f}"],
    },
    "08-developer-relations-docs/13-api-example-tester": {
        "fields": ["examples|Examples in the docs|number|140", "broken|Examples found broken|number|31", "languages|Languages covered|number|6", "run_minutes|Minutes to run one example in CI|number|0.5", "releases_year|SDK releases per year|number|12"],
        "sections": [
            ["Examples", "Inventory: {input}", "{examples} examples in {languages} languages, {broken} broken.", "A broken example is a broken promise. New users copy the first example they see."],
            ["Extract and run", "Keep examples as real source files that the docs pull in, never as text pasted into pages. Run every file in CI against a sandbox account or a mock server.", "Check output as well as exit codes: print the expected result and compare it."],
            ["When to run", "Run on every docs change, on every SDK release and on a nightly schedule against the live API so you notice server-side changes.", "Per run this takes about the number of minutes below."],
            ["Ownership", "Give each language a owner. A failing example opens an issue with the file, the error and the commit that broke it.", "Block the SDK release when an example for that SDK fails."],
            ["Quality of the examples", "Use realistic names, show error handling, avoid secrets in the code and state the version used. Prefer short examples that do one thing.", "Add a test that finds docs code blocks that are not covered by a runnable file."],
        ],
        "metrics": ["Share of examples that are broken|broken / examples|{:.0%}", "CI minutes for a full run|examples * run_minutes|{:,.0f}", "CI minutes a year from release runs|examples * run_minutes * releases_year|{:,.0f}"],
    },
    "08-developer-relations-docs/14-docs-ia-reviewer": {
        "fields": ["pages|Pages|number|410", "sections|Top-level sections|number|9", "quickstart_clicks|Clicks from the home page to the quickstart|number|4", "search_share|Visits that start with search (0 to 1)|number|0.55", "orphans|Pages with no inbound links|number|37"],
        "sections": [
            ["Site", "Map: {input}", "{pages} pages, {sections} sections. Quickstart is {quickstart_clicks} clicks away. {orphans} pages have no inbound links.", "Organise docs around what readers are trying to do. Do not mirror your org chart or your code folders."],
            ["Four kinds of page", "Tutorials teach by doing, how-to guides solve a task, reference lists facts, explanations give background. Mixing them makes pages long and hard to scan.", "Label each page with its type and keep to it."],
            ["Navigation", "Aim for at most two or three levels. Keep {sections} top-level sections to about 7 and name them by task. Put the quickstart one click from the home page.", "Avoid titles such as Overview that mean nothing in search results."],
            ["Search and links", "Over {search_share} of visits start with search, so write titles and first sentences for search and test the top 20 queries weekly. Link pages that readers visit in sequence.", "Fix or remove the {orphans} orphan pages."],
            ["Review loop", "Watch search terms with no results, pages with high exits and support questions that cite the docs. Run a task-based test: can five new users find the answer in two minutes.", "Redirect every moved page to avoid broken links."],
        ],
        "metrics": ["Share of pages that are orphans|orphans / pages|{:.1%}", "Pages per section on average|pages / sections|{:,.0f}", "Clicks over the one-click goal|quickstart_clicks - 1|{:,.0f}"],
    },
    "08-developer-relations-docs/15-devrel-metrics-reporter": {
        "fields": ["visits|Docs visits|number|180000", "new_keys|New API keys|number|2100", "first_call|Keys that make a first call|number|798", "community|Community members|number|6400", "answered|Community questions answered in 24 hours (0 to 1)|number|0.72"],
        "sections": [
            ["Period", "Stats: {input}", "{visits} docs visits, {new_keys} new keys, {first_call} reached a first call. Community: {community}.", "Report outcomes tied to business goals: activation and retention, not only reach and likes."],
            ["Funnel", "Track the path: visit, sign up, create a key, first successful call, a working integration. Find the step where most developers drop out.", "Share the funnel with the product team every month."],
            ["Community health", "Measure questions answered within 24 hours ({answered}), the share answered by other members, new contributors and returning members.", "A community that only you answer is a support channel."],
            ["Content", "Rank content by activation it leads to, not by page views. Retire pages with high traffic and low conversion, and double down on the ones that bring developers to a first call.", "Attribute with a simple tag on links from talks and posts."],
            ["Reporting", "Write one page: goals, results against targets, what you learned, what you will change. Keep vanity numbers in an appendix.", "Agree the targets with the product and sales leaders at the start of the quarter."],
        ],
        "metrics": ["Visit to key conversion|new_keys / visits|{:.2%}", "Share of keys that reach a first call|first_call / new_keys|{:.0%}", "Keys that never make a call|new_keys - first_call|{:,.0f}"],
    },
    "08-developer-relations-docs/16-tech-blog-outliner": {
        "fields": ["thesis|Main claim|text|A read-through cache cut p99 session lookups by 40 percent", "audience|Reader|text|Backend engineers running Postgres at scale", "words|Target length (words)|number|1800", "wpm|Reading speed (words per minute)|number|230", "evidence|Evidence you have|list|Before and after latency graphs; load test script; cache hit rate over a week"],
        "sections": [
            ["Topic", "Brief: {input}", "Claim: {thesis}. Reader: {audience}.", "A technical post earns attention with a specific claim and proof the reader can check."],
            ["Opening", "State the problem and the result in the first paragraph, with the number. Say who the post is for and what they will be able to do after reading it.", "Cut the story of the project. Start where the reader's problem starts."],
            ["Body", "Context and constraints, the options you considered and why you rejected them, the design with a diagram, the implementation with trimmed code, then the results.", "One idea per section, and a heading that says the point."],
            ["Evidence", "*{evidence}", "Show the method, the numbers and the limits, including what did not work. Publish the code so others can run it."],
            ["Ending", "Summarise the lesson in three bullets, state when the approach does not fit and link to the code and a discussion place.", "Reading time is about {words} words at {wpm} words a minute. Cut sections that do not support the claim."],
        ],
        "metrics": ["Reading time (minutes)|words / wpm|{:.1f}"],
    },
    "08-developer-relations-docs/17-webinar-planner": {
        "fields": ["registrants|Target registrants|number|400", "attend_rate|Expected attendance rate (0 to 1)|number|0.35", "minutes|Length (minutes)|number|45", "demo_minutes|Minutes of live demo|number|25", "speakers|Speakers|number|2"],
        "sections": [
            ["Brief", "Brief: {input}", "{minutes} minutes, {speakers} speakers, {registrants} registrants targeted.", "Developers come for something they can use tomorrow. Keep slides to the minimum and show working code."],
            ["Run of show", "5 minutes of problem and what you will build, {demo_minutes} minutes of live build with checkpoints, 10 minutes of questions. Share a repository link at the start.", "Rehearse twice, and agree who watches chat and who speaks."],
            ["Demo safety", "Record a backup video, keep a working branch you can switch to, test the network and credentials 30 minutes before and hide secrets in the terminal and the browser.", "If the live build fails, say so, switch to the backup and carry on."],
            ["Promotion", "Open registration four weeks ahead. Send three emails (announce, reminder, last call), post in the places your developers already are and ask partners to share. Make the title specific.", "Registration copy should say what the viewer will build."],
            ["Follow-up", "Send the recording, the code and a short survey within 24 hours. Answer unanswered questions in writing and invite the audience to the next step.", "Judge success by attendees who try the code, not by registrations."],
        ],
        "metrics": ["Expected live attendees|registrants * attend_rate|{:,.0f}", "Minutes left for questions and setup|minutes - demo_minutes|{:,.0f}", "Registrants who will watch the recording instead|registrants * (1 - attend_rate)|{:,.0f}"],
    },
    "08-developer-relations-docs/18-sample-app-reviewer": {
        "fields": ["setup_steps|Steps in the README to get it running|number|7", "target_steps|Target number of steps|number|3", "secrets|Hard-coded secrets found|number|1", "dep_age_months|Age of the oldest dependency (months)|number|26", "has_tests|Has automated tests (yes or no)|text|No"],
        "sections": [
            ["Sample", "README: {input}", "{setup_steps} setup steps against a target of {target_steps}. Secrets found: {secrets}. Tests: {has_tests}.", "A sample app teaches by example. Developers copy it into production code, so it must be safe and correct."],
            ["First run", "Aim for a working app in {target_steps} steps and under five minutes: clone, copy the example env file, run. Provide a one-command start and a clear message if something is missing.", "Test the instructions on a clean machine every release."],
            ["Security", "Remove hard-coded keys and rotate any that were committed. Load secrets from the environment, ship a .env.example with placeholders and add a secret scanner to CI.", "Show safe patterns: input validation, output encoding and least privilege."],
            ["Code quality", "Keep it small and well named, with comments that explain why. Show error handling and the happy path. Add tests that run in CI, since tests double as documentation.", "Pin dependency versions and update them regularly: the oldest is {dep_age_months} months."],
            ["Maintenance", "Name an owner, add a CI build against the current SDK, and archive the sample when it stops matching the API.", "List the sample in the docs next to the feature it demonstrates."],
        ],
        "metrics": ["Setup steps over target|setup_steps - target_steps|{:+.0f}", "Age of the oldest dependency in years|dep_age_months / 12|{:.1f}"],
    },
    "08-developer-relations-docs/19-contributing-guide-writer": {
        "fields": ["project|Project|text|A Rust command-line tool", "maintainers|Active maintainers|number|3", "open_prs|Open pull requests|number|46", "review_days|Median days to the first review|number|9", "target_days|Target days to the first review|number|3"],
        "sections": [
            ["Project", "Facts: {input}", "Project: {project}. {maintainers} maintainers, {open_prs} open pull requests.", "A contributing guide lowers the cost of a first contribution and the cost of reviewing it."],
            ["Getting started", "Setup in a few commands, how to run the tests and how to find a good first issue. Label beginner issues and keep them current.", "Say which kinds of change are welcome and which need discussion first."],
            ["Workflow", "Open an issue for big changes, fork, branch, make small focused commits and open a pull request with a clear description. Describe the commit message format and sign-off requirement.", "Smaller pull requests are reviewed faster."],
            ["Standards", "State the format and lint commands, the test expectations and the documentation rule. Automate them in CI so reviewers talk about design, not style.", "Include a code of conduct and how to report problems."],
            ["Review expectations", "Median wait for a first review is {review_days} days. The target is {target_days}. Describe the triage rota, how to ask for a review politely and when a stale pull request is closed.", "Thank contributors in release notes."],
        ],
        "metrics": ["Open pull requests per maintainer|open_prs / maintainers|{:.0f}", "Days over the review target|review_days - target_days|{:+.0f}"],
    },
    "08-developer-relations-docs/20-developer-journey-mapper": {
        "fields": ["visitors|Developers who reach the docs|number|10000", "signups|Developers who create an account|number|1800", "first_call|Developers who make a first API call|number|760", "production|Developers who go to production|number|190", "wait_days|Days between signup and production access|number|9"],
        "sections": [
            ["Journey", "Notes: {input}", "Funnel: {visitors} reach docs, {signups} sign up, {first_call} make a first call, {production} reach production.", "Map what the developer does, thinks and feels at each stage, and where time or confidence is lost."],
            ["Stages", "Discover, evaluate (can it do what I need), start (account and first call), build (integration) and run in production (limits, support, billing). Each stage has a different job for your docs.", "Interview five developers who dropped out, not only those who succeeded."],
            ["Where they drop", "Compare each step's conversion. The largest relative loss is the first fix to try, and waiting steps (approvals, reviews) cost more than they look.", "Wait between signup and production access is {wait_days} days."],
            ["Fixes", "Instant sandbox keys, a working first call in one page, clear limits, a preview of the production checklist and a named contact for security reviews.", "Remove steps before adding explanations."],
            ["Measure", "Track time to first call, time to production and the conversion of each stage weekly. Re-run the journey with a new developer every quarter.", "Share the map with product, support and sales."],
        ],
        "metrics": ["Visit to signup rate|signups / visitors|{:.1%}", "Signup to first call rate|first_call / signups|{:.0%}", "First call to production rate|production / first_call|{:.0%}"],
    },
}
