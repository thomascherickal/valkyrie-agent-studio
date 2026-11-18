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
    }
  ]
};
