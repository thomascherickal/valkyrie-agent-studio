"""Playbooks for the Developer Relations and Docs agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "08-developer-relations-docs/01-quickstart-author": {
        "fields": ["prereqs|Prerequisites|list|Python 3.11 or newer, Rust toolchain installed with rustup, Valkyrie Studio installed", "commands|Exact commands, one per line|longtext|valkyrie login\nvalkyrie agent new hello --template rust\nvalkyrie deploy hello --target rust\ncurl http://localhost:8080/health", "success_check|What the reader should see at the end|text|The health endpoint returns status ok", "budget_min|Time budget (minutes)|number|5", "step_count|Number of steps|number|6"],
        "sections": [
            ["Goal", "Quickstart for: {input}", "Promise: working in {budget_min} minutes. Success looks like: {success_check}", "Open with the outcome in one sentence and a time estimate."],
            ["Prerequisites", "*{prereqs}", "State exact versions and how to check them (for example python --version). List accounts or keys needed before step 1."],
            ["Steps", "*{commands}", "One action per step, each in a copy-pasteable block with the expected output below it. Never ask the reader to edit a file by hand if a command can do it."],
            ["Verify and troubleshoot", "Finish with a check that proves it works: {success_check}", "Add the three most common failures with the exact error text and the fix (PATH not set, port in use, missing API key)."],
            ["Next steps", "Link to three follow-ups only: a concept page, a how-to and the API reference.", "Test the quickstart on a clean machine or container in CI and on every release; a broken quickstart is the most expensive docs bug."],
        ],
        "metrics": ["Seconds per step|budget_min * 60 / step_count|{:.0f}"],
    },
    "08-developer-relations-docs/02-api-reference-polisher": {
        "fields": ["base_url|Base URL|text|http://localhost:8000", "auth|Authentication header|text|Authorization: Bearer YOUR_API_KEY", "request_body|Example request body|longtext|agent_id: hello-agent\ntarget: rust\nrelease: true", "response_example|Example response|text|status queued, job_id job_8f2a, crate_url /bundles/hello-agent.tar.gz", "rate_limit|Rate limit (requests per minute)|number|60"],
        "sections": [
            ["Endpoint", "Operation: {input}", "Base URL {base_url}. Auth header: {auth}."],
            ["Description", "Start with what the call does and when to use it, then required versus optional parameters with types, limits and defaults. State if it is asynchronous and how to poll.", "Document idempotency and side effects in one line each."],
            ["Request example", "Fields in the example body:", "*{request_body}", "Show the same call in curl, Python (requests or httpx) and TypeScript (fetch), each runnable after setting one environment variable."],
            ["Response and errors", "Success response: {response_example}", "List each status code (200, 202, 400, 401, 404, 409, 429) with a sample error body and the fix. Limit: {rate_limit} requests per minute, plus the Retry-After behaviour."],
            ["Polish checklist", "Realistic values not foo or string, consistent field names, units on every number, copy button friendly code, and an example for each enum value.", "Generate examples from the OpenAPI file in CI so they cannot drift."],
        ],
        "metrics": ["Minimum seconds between calls at the rate limit|60 / rate_limit|{:.1f}"],
    },
    "08-developer-relations-docs/03-sdk-sample-generator": {
        "fields": ["languages|Languages|list|Python, TypeScript, Rust", "model|Model name|text|gemini-4-hydrogen", "env_var|API key environment variable|text|GEMINI_API_KEY", "sdk_versions|SDK versions|text|valkyrie-py 1.2, valkyrie-js 1.2, valkyrie crate 0.9"],
        "sections": [
            ["Operation", "Task: {input}", "Model {model}; key from {env_var}. SDKs: {sdk_versions}."],
            ["Languages", "*{languages}", "Each sample must be complete: imports, client creation, one call, result handling and error handling, and must run unchanged after the key is set."],
            ["Idiomatic style", "Python: type hints, context managers, async variant with asyncio. TypeScript: ES modules, async and await, typed response, no any. Rust: Result and the question mark operator, tokio main, builder pattern, no unwrap in examples.", "Read the key from the environment, never inline it."],
            ["Error handling", "Show handling for authentication errors, rate limits (retry with backoff) and timeouts. Set an explicit timeout on every client.", "Print a short, deterministic result so readers can check it."],
            ["Maintenance", "Pin SDK versions in the snippet header, run all samples in CI against a mock server on every release, and keep the same variable names across languages so the samples read as a set.", "Use the same prompt and expected output in every language."],
        ],
        "metrics": [],
    },
    "08-developer-relations-docs/04-changelog-curator": {
        "fields": ["version|Release version|text|v2.0.0", "breaking|Breaking changes|list|Web-only UI removed in favor of the desktop app, Config moved from .env to studio.toml", "deprecations|Deprecations|list|The /run-agent route, Python 3.9 support", "codemod|Migration command|text|npx valkyrie-codemod migrate-ui ./src", "removal_version|Removal version for deprecated items|text|v3.0.0"],
        "sections": [
            ["Release", "Diff: {input}", "Version {version}.", "Lead with the biggest change for developers and who needs to act."],
            ["Breaking changes", "*{breaking}", "For each: what changed, why, who is affected, the before and after code, and the exact migration steps."],
            ["Migration", "Automated migration: {codemod}", "Provide a codemod or script when more than three call sites typically change, run it on a sample project, and document what it does not cover."],
            ["Deprecations", "*{deprecations}", "Each deprecation states the replacement and the removal version ({removal_version}). Emit a runtime warning and link to the docs."],
            ["Format", "Follow Keep a Changelog sections: Added, Changed, Deprecated, Removed, Fixed, Security. Semantic Versioning: breaking means a major bump.", "Link the pull request for each item and publish the changelog as RSS."],
        ],
        "metrics": [],
    },
    "08-developer-relations-docs/05-community-qa-helper": {
        "fields": ["asker_level|Asker experience|text|New user, unclear about local versus hosted models", "version|Version in use|text|v2.4.1", "doc_links|Docs links to cite|list|docs/providers.md, docs/ollama-setup.md", "next_step|Follow-up if unresolved|text|Ask for the output of valkyrie doctor and the exact error text"],
        "sections": [
            ["Question", "Question: {input}", "Asker: {asker_level}. Version: {version}."],
            ["Answer structure", "Thank the asker, restate the question in one line to confirm understanding, give the direct answer first, then the steps, then a short explanation of why.", "Use a code block for commands and say where to run them. Keep it under 200 words when possible."],
            ["Accuracy", "Verify every command and flag against the current docs or by running it. If unsure, say so and point to the source rather than guessing.", "References:", "*{doc_links}"],
            ["Tone", "Welcoming and specific. Do not assume the reader's mistake, avoid 'just' and 'simply', and never close with 'RTFM'.", "If the question reveals a docs gap, thank them and open a docs issue."],
            ["If unresolved", "{next_step}", "Mark the thread as answered only when the asker confirms; convert repeated questions into FAQ entries."],
        ],
        "metrics": [],
    },
    "08-developer-relations-docs/06-tutorial-video-scripter": {
        "fields": ["runtime_sec|Target runtime (seconds)|number|180", "words_per_min|Narration speed (words per minute)|number|150", "terminal_commands|Commands shown on screen|longtext|valkyrie optimize my-agent --every 3\nvalkyrie runs list\nvalkyrie optimize status", "audience|Audience|text|Developers who already ran their first agent", "cta|Call to action|text|Star the repo and try the optimizer on your own agent"],
        "sections": [
            ["Hook", "Topic: {input}", "Audience: {audience}.", "First 10 seconds: show the result or the pain, not a logo or an introduction."],
            ["Beats", "Outline in about 20 second beats: problem, setup, first command, result, one gotcha, recap.", "Terminal commands on screen:", "*{terminal_commands}"],
            ["Recording tips", "Use a 16 point or larger font, a clean prompt, pre-typed commands that run in under 5 seconds, a zoom on key output, and cuts rather than waiting.", "Rehearse once off camera and record in a fresh directory so the path matches the voice-over."],
            ["Narration budget", "Target {runtime_sec} seconds at {words_per_min} words per minute.", "Write short sentences, say commands out loud as they appear, and leave 1 second of silence after each result."],
            ["Ending", "Recap in one sentence, then the call to action: {cta}", "Add chapters, a pinned comment with copyable commands, and captions."],
        ],
        "metrics": ["Narration word budget|runtime_sec / 60 * words_per_min|{:,.0f} words", "Number of 20 second beats|runtime_sec / 20|{:.0f}"],
    },
    "08-developer-relations-docs/07-docs-freshness-checker": {
        "fields": ["checked|Items checked (flags, routes, commands)|number|120", "drifted|Items that disagree with the code|number|7", "docs_files|Doc files in scope|number|40", "source_of_truth|Source of truth|text|CLI help output and the generated OpenAPI file", "owner|Docs owner|text|Developer Relations"],
        "sections": [
            ["Drift found", "Comparison: {input}", "Source of truth: {source_of_truth}. Scope: {docs_files} files."],
            ["Check method", "Extract commands, flags, routes, environment variables and config keys from docs by regex and compare with the generated CLI help, OpenAPI paths and config schema. Report items only in docs (stale) and only in code (undocumented).", "Include version numbers, default values and sample output in the comparison."],
            ["Classification", "Critical: documented command or route does not exist, as in a docs route that differs from the real one. Major: wrong default or flag name. Minor: wording or an outdated screenshot.", "Fix criticals in the same pull request that changed the code."],
            ["Fix process", "Assign each item to {owner} with a due date. Prefer generating reference docs from code so they cannot drift, and run the checker in CI on every pull request.", "Add a docs-impact checkbox to the pull request template."],
            ["Cadence", "Full audit each release, a link checker weekly, and a last-reviewed date on every page; flag pages older than 6 months.", "Track the drift rate release over release."],
        ],
        "metrics": ["Drift rate|drifted / checked|{:.1%}", "Items accurate|(checked - drifted) / checked|{:.1%}"],
    },
    "08-developer-relations-docs/08-cfp-abstract-writer": {
        "fields": ["conference|Conference and track|text|PyCon track on performance and systems", "talk_min|Talk length (minutes)|number|30", "level|Audience level|text|Intermediate Python developers", "takeaways|Concrete takeaways|list|How to find GIL-bound hotspots, A PyO3 port pattern with benchmarks, When not to port", "demo_pct|Share of the talk that is live demo (percent)|number|30"],
        "sections": [
            ["Talk", "Idea: {input}", "Event: {conference}. Level: {level}."],
            ["Title and hook", "Title: specific, promises an outcome, under 70 characters. Open the abstract with a problem the audience recognises in one sentence.", "Avoid titles like 'Introduction to' or 'Thoughts on'."],
            ["Abstract body", "Three short paragraphs: the problem and why it matters now, what the talk shows (the approach and the demo), and who it is for with prerequisites.", "Takeaways attendees will leave with:", "*{takeaways}"],
            ["Outline", "Give a timed outline for {talk_min} minutes: problem 5, approach 10, demo 10, lessons 3, questions 2. Reviewers reward a visible structure and evidence the speaker has done the thing.", "Mention that the demo is rehearsed and has an offline fallback."],
            ["Reviewer notes", "Keep within the word limit, name the novel part, include speaker bio with relevant experience, link a previous talk or repository, and avoid vendor pitches.", "Submit early; do not leave it to the last hour of the deadline."],
        ],
        "metrics": ["Demo minutes|talk_min * demo_pct / 100|{:.0f}", "Minutes of explanation|talk_min * (1 - demo_pct / 100)|{:.0f}"],
    },
    "08-developer-relations-docs/09-hackathon-kit-builder": {
        "fields": ["hours|Event length (hours)|number|4", "teams|Expected teams|number|20", "mentors|Mentors available|number|5", "prize_pool|Prize pool (USD)|number|3000", "dataset|Sample dataset|text|12 months of anonymised cloud billing CSV files, 200 MB"],
        "sections": [
            ["Theme", "Theme: {input}", "{hours} hours, {teams} teams, {mentors} mentors."],
            ["Starter kit", "Repository with a working hello-world agent, a .env.example, a one-command setup script, three starter prompts and a README that gets a team building within 15 minutes. Dataset: {dataset}.", "Provide fallback options if the network or a provider fails: a local model and cached responses."],
            ["Timeline", "Hour 0: kickoff, 15 minutes. Build blocks with a mentor check-in each hour. Final 30 minutes: submissions freeze, 3 minute demos. Put the deadline for submission first on every slide.", "Mentors cover the common blockers: setup, auth, rate limits."],
            ["Judging rubric", "Score 1 to 5 on: working demo (30 percent), usefulness of the problem (25), technical depth (20), use of the platform (15), presentation (10).", "Use at least 3 judges, score independently before discussion, and announce tie-break rules."],
            ["Prizes and follow up", "Prize pool {prize_pool} USD: first, second, third and a best-use-of-platform award. Collect team emails with consent and send a follow-up with resources within 48 hours.", "Track how many projects are still active after 30 days."],
        ],
        "metrics": ["Teams per mentor|teams / mentors|{:.1f}", "Average prize per team|prize_pool / teams|${:,.0f}", "Demo time needed at 5 minutes per team (minutes)|teams * 5|{:,.0f}"],
    },
    "08-developer-relations-docs/10-dev-survey-analyst": {
        "fields": ["responses|Number of responses|number|240", "top_pain|Top pain point|text|Setting up the Rust toolchain", "pain_mentions|Mentions of the top pain point|number|96", "promoters_pct|Promoters (percent scoring 9 or 10)|number|52", "detractors_pct|Detractors (percent scoring 0 to 6)|number|14"],
        "sections": [
            ["Survey results", "Responses: {input}", "{responses} responses. Top pain point: {top_pain} ({pain_mentions} mentions)."],
            ["Friction map", "Group pain points by journey stage: discover, install, first success, build, deploy, debug. Rank by frequency and by severity (blocked versus annoyed).", "A pain mentioned by newcomers matters more for growth than one mentioned only by power users; split by tenure."],
            ["Scores", "NPS = promoters percent minus detractors percent. Above 30 is good for developer tools, above 50 excellent. Report time to first success as a median, not an average.", "With under 100 responses treat differences below 10 points as noise."],
            ["Coding open text", "Code each comment with one or two tags, check agreement on a sample of 30, and quote at least one verbatim for each top theme.", "Report delight points too, so teams know what to protect."],
            ["Recommendations", "Fix the top pain first, name an owner and a metric (for example, toolchain setup time down from 25 to 10 minutes), and re-survey after 90 days.", "Share results with respondents: it raises the next response rate."],
        ],
        "metrics": ["Share naming the top pain|pain_mentions / responses|{:.0%}", "Net promoter score|promoters_pct - detractors_pct|{:.0f}", "Passives (percent)|100 - promoters_pct - detractors_pct|{:.0f}"],
    },
}
