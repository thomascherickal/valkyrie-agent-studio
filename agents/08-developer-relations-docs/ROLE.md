# Developer Relations & Docs

Developer Relations & Docs suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-quickstart-author` — **Quickstart Author**: Creates copy-pasteable 5-minute quickstarts verified against CLI steps. (Tool: `structure_quickstart`)
- `02-api-reference-polisher` — **API Reference Polisher**: Adds realistic curl, Python, and TypeScript examples to OpenAPI specs. (Tool: `enrich_api_examples`)
- `03-sdk-sample-generator` — **SDK Sample Generator**: Produces idiomatic snippets across Python, TypeScript, and Rust. (Tool: `emit_polyglot_samples`)
- `04-changelog-curator` — **Changelog Curator**: Highlights breaking changes, deprecations, and codemods for devs. (Tool: `curate_dev_changelog`)
- `05-community-qa-helper` — **Community Q&A Helper**: Drafts accurate, welcoming answers for GitHub Discussions and Discord. (Tool: `compose_community_reply`)
- `06-tutorial-video-scripter` — **Tutorial Video Scripter**: Outlines 3-minute screencast scripts with live terminal commands. (Tool: `script_video_beats`)
- `07-docs-freshness-checker` — **Docs Freshness Checker**: Cross-checks markdown docs against actual CLI flags and API routes. (Tool: `detect_doc_drift`)
- `08-cfp-abstract-writer` — **CFP Abstract Writer**: Crafts sharp conference talk abstracts with concrete takeaways. (Tool: `polish_cfp_abstract`)
- `09-hackathon-kit-builder` — **Hackathon Kit Builder**: Packages starter prompts, sample datasets, and judging rubrics. (Tool: `assemble_kit_manifest`)
- `10-dev-survey-analyst` — **Dev Survey Analyst**: Quantifies DX friction points across onboarding, docs, and SDKs. (Tool: `summarize_dx_metrics`)
- `11-migration-guide-writer` — **Migration Guide Writer**: Writes upgrade guides for breaking changes with before and after code and a safe order of steps. (Tool: `write_migration_guide`)
- `12-error-reference-writer` — **Error Reference Writer**: Writes error reference pages with cause, fix, example, and links for each error code. (Tool: `write_error_reference`)
- `13-api-example-tester` — **API Example Tester**: Plans automated testing of documentation code examples so they stay runnable. (Tool: `test_api_examples`)
- `14-docs-ia-reviewer` — **Docs Information Architecture Reviewer**: Reviews documentation navigation, page types, and search paths against reader tasks. (Tool: `review_docs_ia`)
- `15-devrel-metrics-reporter` — **DevRel Metrics Reporter**: Reports developer relations impact with activation, community, and content metrics tied to goals. (Tool: `report_devrel_metrics`)
- `16-tech-blog-outliner` — **Technical Blog Outliner**: Outlines technical posts with a clear thesis, reader level, sections, and runnable proof. (Tool: `outline_tech_post`)
- `17-webinar-planner` — **Developer Webinar Planner**: Plans developer webinars with topic, run of show, demo safety, promotion, and follow-up. (Tool: `plan_webinar`)
- `18-sample-app-reviewer` — **Sample App Reviewer**: Reviews sample applications for clarity, security, correctness, and ease of running. (Tool: `review_sample_app`)
- `19-contributing-guide-writer` — **OSS Contribution Guide Writer**: Writes contribution guides with setup, workflow, standards, and review expectations for open source projects. (Tool: `write_contributing_guide`)
- `20-developer-journey-mapper` — **Developer Journey Mapper**: Maps the developer journey from discovery to production with friction, drop-off, and fixes. (Tool: `map_developer_journey`)
