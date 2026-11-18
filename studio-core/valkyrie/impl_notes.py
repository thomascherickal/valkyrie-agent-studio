"""What a user has to add, by role: the systems, data and rules the generated implementations cannot know."""

ROLE_NOTES: dict[str, list[str]] = {
    "01-product-management": [
        "Connect your product sources: the backlog or issue tracker, analytics events, customer research notes and release calendar.",
        "Write down your prioritisation and scoring rules (weights, tiers, thresholds) so the agent applies your framework, not a generic one.",
        "Decide who owns the decision the output feeds, and add the template your team uses for that document.",
    ],
    "02-software-engineering": [
        "Point the agent at your code and design sources: repository hosting, pull requests, architecture docs and the coding standards you enforce.",
        "Add your real conventions (language, framework, naming, review checklist) as rules or prompt text.",
        "Define what counts as a blocker versus a suggestion, and the format your reviewers expect.",
    ],
    "03-devops-sre": [
        "Connect telemetry: metrics, logs, traces, alert payloads and your incident or paging tool.",
        "Add your service-level targets, error budgets, severity definitions and escalation paths.",
        "Encode the safe actions for your platform (rollbacks, scaling, runbooks), and which ones need a human to approve.",
    ],
    "04-qa-test-automation": [
        "Connect your test assets: the test runner, CI results, requirements or acceptance criteria, and the bug tracker.",
        "Add your risk model: which areas, devices and data states matter most, and your coverage thresholds.",
        "Decide what makes a test flaky or a release blocking, and where the agent should file or update results.",
    ],
    "05-data-engineering": [
        "Connect your data platform: warehouse, orchestrator, catalog, lineage and data-quality tooling.",
        "Add your schemas, freshness and volume expectations, and the owners to notify when a check fails.",
        "Define the idempotency, retry and backfill rules your pipelines must follow.",
    ],
    "06-security-appsec": [
        "Connect your security sources: scanners, dependency and image inventories, cloud configuration and identity logs.",
        "Add your policy: severity scale, SLAs for fixes, approved exceptions and the frameworks you are measured against.",
        "Decide which findings may be auto-triaged and which need a person. Never let the agent change access by itself.",
    ],
    "07-technical-support": [
        "Connect the support desk, knowledge base, customer account data and product telemetry.",
        "Add your SLAs, priority matrix, escalation tiers and the wording standards for customer replies.",
        "Decide what the agent may say to customers on its own and what must be reviewed first.",
    ],
    "08-developer-relations-docs": [
        "Connect your docs repository, API reference, changelog, community channels and sample projects.",
        "Add your style guide, terminology list, supported versions and the audiences you write for.",
        "Define how examples are tested, so published code is run before it is shared.",
    ],
    "09-growth-product-analytics": [
        "Connect your analytics warehouse or event pipeline, experiment platform and CRM or marketing tools.",
        "Add your metric definitions (what counts as active, converted, retained) and the segments you track.",
        "Set statistical thresholds, minimum sample sizes and guardrail metrics before the agent reports a result as significant.",
    ],
    "10-finops-cloud-cost": [
        "Connect billing exports, usage data, tagging or cost-allocation sources and your commitment contracts.",
        "Add your budgets, unit-cost targets, anomaly thresholds and the owners for each account or team.",
        "Decide which savings the agent may recommend versus apply, and how savings are verified after the change.",
    ],
    "11-management": [
        "Connect the people and planning sources you use: HRIS, calendars, goal tracking and survey tools.",
        "Add your policies (leave, leveling, review cycles) and the fairness and privacy rules that apply.",
        "Keep a person in the loop for any decision about an individual, and record why each recommendation was made.",
    ],
    "12-cxos": [
        "Connect the executive data you report on: finance, board materials, strategy documents and key metrics.",
        "Add your definitions, targets and the confidentiality rules for who may see which figures.",
        "Have an owner review every output before it leaves the company, and keep the sources next to each claim.",
    ],
}

# Used when an agent has no authored profile (for example an agent you created yourself).
GENERIC_NOTES = [
    "Connect the systems and data this agent should read, and decide who owns its output.",
    "Write down your real rules, thresholds and terminology so the output follows your standards.",
    "Decide which actions need a person to approve before they happen.",
]
