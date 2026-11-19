# QA & Test Automation

QA & Test Automation suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

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
- `11-contract-test-designer` — **Contract Test Designer**: Designs consumer-driven contract tests between services from their API contracts. (Tool: `design_contract_tests`)
- `12-test-data-synthesizer` — **Test Data Synthesizer**: Plans realistic, privacy-safe test data from schema rules, distributions, and edge profiles. (Tool: `synthesize_test_data`)
- `13-mutation-test-reviewer` — **Mutation Test Reviewer**: Reviews mutation testing results and turns surviving mutants into targeted tests. (Tool: `review_mutation_survivors`)
- `14-visual-regression-triager` — **Visual Regression Triager**: Triages screenshot diffs into real regressions, intended changes, and flaky rendering. (Tool: `triage_visual_diffs`)
- `15-device-matrix-planner` — **Mobile Device Matrix Planner**: Builds a mobile test matrix from usage analytics, risk, and testing capacity. (Tool: `build_device_matrix`)
- `16-test-pyramid-auditor` — **Test Pyramid Auditor**: Audits the balance of unit, integration, and end-to-end tests against speed and reliability. (Tool: `audit_test_pyramid`)
- `17-exploratory-charter-writer` — **Exploratory Charter Writer**: Writes exploratory testing charters with missions, risks, time boxes, and note templates. (Tool: `write_charters`)
- `18-qa-release-checklist-builder` — **QA Release Checklist Builder**: Builds release checklists from scope, risk, and past escapes with clear sign-off gates. (Tool: `build_release_checklist`)
- `19-l10n-test-planner` — **Localization Test Planner**: Plans localization and internationalization tests for locales, text expansion, and formats. (Tool: `plan_locale_tests`)
- `20-security-test-case-writer` — **Security Test Case Writer**: Writes security test cases for authentication, authorization, input handling, and abuse paths. (Tool: `write_security_tests`)
