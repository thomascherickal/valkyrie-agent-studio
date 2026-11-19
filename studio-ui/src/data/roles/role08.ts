import type { RoleCatalog } from "../types";

export const ROLE_08: RoleCatalog = {
  "id": "08-developer-relations-docs",
  "name": "Developer Relations & Docs",
  "agents": [
    {
      "id": "01-quickstart-author",
      "name": "Quickstart Author",
      "description": "Creates copy-pasteable 5-minute quickstarts verified against CLI steps.",
      "tool": "structure_quickstart",
      "inputKey": "feature_name",
      "outputKey": "quickstart_md",
      "sampleInput": "Deploying your first Rust agent from Valkyrie Studio"
    },
    {
      "id": "02-api-reference-polisher",
      "name": "API Reference Polisher",
      "description": "Adds realistic curl, Python, and TypeScript examples to OpenAPI specs.",
      "tool": "enrich_api_examples",
      "inputKey": "endpoint_def",
      "outputKey": "reference_md",
      "sampleInput": "POST /api/agents/deploy-rust"
    },
    {
      "id": "03-sdk-sample-generator",
      "name": "SDK Sample Generator",
      "description": "Produces idiomatic snippets across Python, TypeScript, and Rust.",
      "tool": "emit_polyglot_samples",
      "inputKey": "operation",
      "outputKey": "code_samples",
      "sampleInput": "Invoke gemini-4-hydrogen in low thinking mode"
    },
    {
      "id": "04-changelog-curator",
      "name": "Changelog Curator",
      "description": "Highlights breaking changes, deprecations, and codemods for devs.",
      "tool": "curate_dev_changelog",
      "inputKey": "release_diff",
      "outputKey": "changelog_md",
      "sampleInput": "Moved from web-only UI to standalone Electron + Vite GUI"
    },
    {
      "id": "05-community-qa-helper",
      "name": "Community Q&A Helper",
      "description": "Drafts accurate, welcoming answers for GitHub Discussions and Discord.",
      "tool": "compose_community_reply",
      "inputKey": "question_text",
      "outputKey": "reply_md",
      "sampleInput": "How do I switch between OpenRouter free models and Ollama?"
    },
    {
      "id": "06-tutorial-video-scripter",
      "name": "Tutorial Video Scripter",
      "description": "Outlines 3-minute screencast scripts with live terminal commands.",
      "tool": "script_video_beats",
      "inputKey": "topic",
      "outputKey": "video_script",
      "sampleInput": "Metaheuristic pymoo agent tuning every 3 runs"
    },
    {
      "id": "07-docs-freshness-checker",
      "name": "Docs Freshness Checker",
      "description": "Cross-checks markdown docs against actual CLI flags and API routes.",
      "tool": "detect_doc_drift",
      "inputKey": "docs_vs_code",
      "outputKey": "drift_report",
      "sampleInput": "Docs say /run-agent; api_server.py exposes /api/agents/run"
    },
    {
      "id": "08-cfp-abstract-writer",
      "name": "CFP Abstract Writer",
      "description": "Crafts sharp conference talk abstracts with concrete takeaways.",
      "tool": "polish_cfp_abstract",
      "inputKey": "talk_idea",
      "outputKey": "cfp_submission",
      "sampleInput": "Zero-GIL AI Agents: Compiling Python Prototypes to Tokio Rust"
    },
    {
      "id": "09-hackathon-kit-builder",
      "name": "Hackathon Kit Builder",
      "description": "Packages starter prompts, sample datasets, and judging rubrics.",
      "tool": "assemble_kit_manifest",
      "inputKey": "theme",
      "outputKey": "hackathon_kit",
      "sampleInput": "Build an automated FinOps agent in 4 hours"
    },
    {
      "id": "10-dev-survey-analyst",
      "name": "Dev Survey Analyst",
      "description": "Quantifies DX friction points across onboarding, docs, and SDKs.",
      "tool": "summarize_dx_metrics",
      "inputKey": "survey_responses",
      "outputKey": "dx_report",
      "sampleInput": "Top pain: setting up Rust toolchain; Top delight: 1-click deploy"
    },
    {
      "id": "11-migration-guide-writer",
      "name": "Migration Guide Writer",
      "description": "Writes upgrade guides for breaking changes with before and after code and a safe order of steps.",
      "tool": "write_migration_guide",
      "inputKey": "breaking_changes",
      "outputKey": "migration_guide",
      "sampleInput": "v3 renames client.send() to client.request(), drops Python 3.8, and changes retries to opt-in"
    },
    {
      "id": "12-error-reference-writer",
      "name": "Error Reference Writer",
      "description": "Writes error reference pages with cause, fix, example, and links for each error code.",
      "tool": "write_error_reference",
      "inputKey": "error_catalog",
      "outputKey": "error_reference",
      "sampleInput": "E1042 rate_limit_exceeded: 429 when more than 600 requests per minute; E2001 invalid_signature: webhook hash mismatch"
    },
    {
      "id": "13-api-example-tester",
      "name": "API Example Tester",
      "description": "Plans automated testing of documentation code examples so they stay runnable.",
      "tool": "test_api_examples",
      "inputKey": "code_examples",
      "outputKey": "example_report",
      "sampleInput": "140 examples in 6 languages, 31 reported broken last quarter, SDK v4 released with renamed methods"
    },
    {
      "id": "14-docs-ia-reviewer",
      "name": "Docs Information Architecture Reviewer",
      "description": "Reviews documentation navigation, page types, and search paths against reader tasks.",
      "tool": "review_docs_ia",
      "inputKey": "site_map",
      "outputKey": "ia_review",
      "sampleInput": "410 pages, 9 top-level sections, 3 pages named Overview, quickstart is 4 clicks from the home page"
    },
    {
      "id": "15-devrel-metrics-reporter",
      "name": "DevRel Metrics Reporter",
      "description": "Reports developer relations impact with activation, community, and content metrics tied to goals.",
      "tool": "report_devrel_metrics",
      "inputKey": "community_stats",
      "outputKey": "devrel_report",
      "sampleInput": "Docs visits 180k, new API keys 2.1k, 38% reach first call, Discord 6.4k members, 14 talks given"
    },
    {
      "id": "16-tech-blog-outliner",
      "name": "Technical Blog Outliner",
      "description": "Outlines technical posts with a clear thesis, reader level, sections, and runnable proof.",
      "tool": "outline_tech_post",
      "inputKey": "topic_brief",
      "outputKey": "post_outline",
      "sampleInput": "How we cut p99 latency 40% by moving session lookups from Postgres to a read-through cache"
    },
    {
      "id": "17-webinar-planner",
      "name": "Developer Webinar Planner",
      "description": "Plans developer webinars with topic, run of show, demo safety, promotion, and follow-up.",
      "tool": "plan_webinar",
      "inputKey": "webinar_brief",
      "outputKey": "webinar_plan",
      "sampleInput": "Live build of a webhook-driven workflow, 45 minutes, target 400 registrants, 2 speakers, recording afterwards"
    },
    {
      "id": "18-sample-app-reviewer",
      "name": "Sample App Reviewer",
      "description": "Reviews sample applications for clarity, security, correctness, and ease of running.",
      "tool": "review_sample_app",
      "inputKey": "sample_readme",
      "outputKey": "sample_review",
      "sampleInput": "README: clone, npm install, add .env with API key, npm start; hard-coded test key in config.js; no tests"
    },
    {
      "id": "19-contributing-guide-writer",
      "name": "OSS Contribution Guide Writer",
      "description": "Writes contribution guides with setup, workflow, standards, and review expectations for open source projects.",
      "tool": "write_contributing_guide",
      "inputKey": "project_facts",
      "outputKey": "contributing_guide",
      "sampleInput": "Rust CLI, 40 contributors, tests run with cargo test, PRs reviewed by 3 maintainers, weekly triage"
    },
    {
      "id": "20-developer-journey-mapper",
      "name": "Developer Journey Mapper",
      "description": "Maps the developer journey from discovery to production with friction, drop-off, and fixes.",
      "tool": "map_developer_journey",
      "inputKey": "journey_notes",
      "outputKey": "journey_map",
      "sampleInput": "Finds us via search, 4 doc pages to first call, key approval takes a day, production needs a security review"
    }
  ]
};
