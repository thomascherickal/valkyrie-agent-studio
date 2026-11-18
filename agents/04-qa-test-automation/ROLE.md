# QA & Test Automation

QA & Test Automation suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-test-plan-architect` — **Test Plan Architect**: Maps PRD acceptance criteria into risk-weighted test matrices. (Tool: `derive_test_matrix`)
- `02-edge-case-hunter` — **Edge Case Hunter**: Generates boundary, empty, unicode, and timezone DST test vectors. (Tool: `enumerate_boundaries`)
- `03-playwright-scripter` — **Playwright E2E Scripter**: Writes resilient locator-first Playwright tests avoiding flaky sleeps. (Tool: `emit_playwright_spec`)
- `04-flaky-test-triager` — **Flaky Test Triager**: Clusters intermittent test failures by race condition, clock, or I/O. (Tool: `classify_flakiness`)
- `05-api-fuzz-generator` — **API Fuzz Generator**: Produces malformed JSON, type-confusion, and oversized payload cases. (Tool: `generate_fuzz_corpus`)
- `06-coverage-gap-finder` — **Coverage Gap Finder**: Parses uncovered branch lines and drafts targeted unit tests. (Tool: `propose_branch_tests`)
- `07-regression-selector` — **Regression Selector**: Selects the minimal impacted test subset from changed file paths. (Tool: `map_impacted_tests`)
- `08-accessibility-auditor` — **Accessibility Auditor**: Audits DOM markup for landmarks, contrast, focus order, and ARIA. (Tool: `audit_wcag_aa`)
- `09-load-test-modeler` — **Load Test Modeler**: Generates ramped virtual-user profiles and p95 latency thresholds. (Tool: `build_k6_profile`)
- `10-bug-repro-distiller` — **Bug Repro Distiller**: Condenses verbose customer bug threads into minimal deterministic repros. (Tool: `distill_min_repro`)
