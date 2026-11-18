# Developer Relations & Docs

Developer Relations & Docs suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
