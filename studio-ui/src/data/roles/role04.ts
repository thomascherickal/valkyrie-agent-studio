import type { RoleCatalog } from "../types";

export const ROLE_04: RoleCatalog = {
  "id": "04-qa-test-automation",
  "name": "QA & Test Automation",
  "agents": [
    {
      "id": "01-test-plan-architect",
      "name": "Test Plan Architect",
      "description": "Maps PRD acceptance criteria into risk-weighted test matrices.",
      "tool": "derive_test_matrix",
      "inputKey": "spec_summary",
      "outputKey": "test_plan",
      "sampleInput": "Passwordless magic link auth with 15-minute TTL"
    },
    {
      "id": "02-edge-case-hunter",
      "name": "Edge Case Hunter",
      "description": "Generates boundary, empty, unicode, and timezone DST test vectors.",
      "tool": "enumerate_boundaries",
      "inputKey": "field_schema",
      "outputKey": "edge_cases",
      "sampleInput": "amount: decimal(>0), currency: ISO-4217, scheduled_at: ISO8601"
    },
    {
      "id": "03-playwright-scripter",
      "name": "Playwright E2E Scripter",
      "description": "Writes resilient locator-first Playwright tests avoiding flaky sleeps.",
      "tool": "emit_playwright_spec",
      "inputKey": "user_flow",
      "outputKey": "test_code",
      "sampleInput": "Sign in -> Create Agent -> Toggle Theme -> Deploy Rust"
    },
    {
      "id": "04-flaky-test-triager",
      "name": "Flaky Test Triager",
      "description": "Clusters intermittent test failures by race condition, clock, or I/O.",
      "tool": "classify_flakiness",
      "inputKey": "failure_logs",
      "outputKey": "triage_report",
      "sampleInput": "Timeout waiting for modal backdrop; failed 3/20 runs"
    },
    {
      "id": "05-api-fuzz-generator",
      "name": "API Fuzz Generator",
      "description": "Produces malformed JSON, type-confusion, and oversized payload cases.",
      "tool": "generate_fuzz_corpus",
      "inputKey": "endpoint_schema",
      "outputKey": "fuzz_cases",
      "sampleInput": "POST /api/agents/run { ir_yaml: string, prompt: string }"
    },
    {
      "id": "06-coverage-gap-finder",
      "name": "Coverage Gap Finder",
      "description": "Parses uncovered branch lines and drafts targeted unit tests.",
      "tool": "propose_branch_tests",
      "inputKey": "coverage_report",
      "outputKey": "missing_tests",
      "sampleInput": "llm_router.py line 88 branch else uncovered"
    },
    {
      "id": "07-regression-selector",
      "name": "Regression Selector",
      "description": "Selects the minimal impacted test subset from changed file paths.",
      "tool": "map_impacted_tests",
      "inputKey": "changed_files",
      "outputKey": "selected_tests",
      "sampleInput": "studio-core/valkyrie/subscription_manager.py"
    },
    {
      "id": "08-accessibility-auditor",
      "name": "Accessibility Auditor",
      "description": "Audits DOM markup for landmarks, contrast, focus order, and ARIA.",
      "tool": "audit_wcag_aa",
      "inputKey": "html_snippet",
      "outputKey": "a11y_issues",
      "sampleInput": "<div onclick='open()'>Deploy</div> without button/role"
    },
    {
      "id": "09-load-test-modeler",
      "name": "Load Test Modeler",
      "description": "Generates ramped virtual-user profiles and p95 latency thresholds.",
      "tool": "build_k6_profile",
      "inputKey": "target_sla",
      "outputKey": "load_script",
      "sampleInput": "Target 1,200 RPS, p95 < 120ms, error rate < 0.1%"
    },
    {
      "id": "10-bug-repro-distiller",
      "name": "Bug Repro Distiller",
      "description": "Condenses verbose customer bug threads into minimal deterministic repros.",
      "tool": "distill_min_repro",
      "inputKey": "bug_thread",
      "outputKey": "repro_steps",
      "sampleInput": "App crashes when switching from dark mode while dialog open"
    },
    {
      "id": "11-contract-test-designer",
      "name": "Contract Test Designer",
      "description": "Designs consumer-driven contract tests between services from their API contracts.",
      "tool": "design_contract_tests",
      "inputKey": "api_contract",
      "outputKey": "contract_suite",
      "sampleInput": "Orders service consumes GET /customers/{id} (fields id, email, tier) from Customers; 3 other consumers"
    },
    {
      "id": "12-test-data-synthesizer",
      "name": "Test Data Synthesizer",
      "description": "Plans realistic, privacy-safe test data from schema rules, distributions, and edge profiles.",
      "tool": "synthesize_test_data",
      "inputKey": "schema_rules",
      "outputKey": "data_plan",
      "sampleInput": "users(id, email unique, country, plan), orders(user_id FK, amount > 0); production has 2M users, 9M orders"
    },
    {
      "id": "13-mutation-test-reviewer",
      "name": "Mutation Test Reviewer",
      "description": "Reviews mutation testing results and turns surviving mutants into targeted tests.",
      "tool": "review_mutation_survivors",
      "inputKey": "mutation_report",
      "outputKey": "survivor_actions",
      "sampleInput": "pricing.py: 240 mutants, 168 killed, 72 survived; survivors mostly in boundary checks and rounding"
    },
    {
      "id": "14-visual-regression-triager",
      "name": "Visual Regression Triager",
      "description": "Triages screenshot diffs into real regressions, intended changes, and flaky rendering.",
      "tool": "triage_visual_diffs",
      "inputKey": "screenshot_diffs",
      "outputKey": "visual_triage",
      "sampleInput": "48 diffs on checkout: 30 are 1px font anti-aliasing, 12 show the new button colour, 6 show a missing icon"
    },
    {
      "id": "15-device-matrix-planner",
      "name": "Mobile Device Matrix Planner",
      "description": "Builds a mobile test matrix from usage analytics, risk, and testing capacity.",
      "tool": "build_device_matrix",
      "inputKey": "usage_analytics",
      "outputKey": "device_matrix",
      "sampleInput": "iOS 62% (17, 16), Android 38% (14, 13, 12); top 5 devices cover 41%; 4 devices in the lab"
    },
    {
      "id": "16-test-pyramid-auditor",
      "name": "Test Pyramid Auditor",
      "description": "Audits the balance of unit, integration, and end-to-end tests against speed and reliability.",
      "tool": "audit_test_pyramid",
      "inputKey": "test_counts",
      "outputKey": "pyramid_report",
      "sampleInput": "Unit 1,800 (3 min), integration 240 (14 min), end-to-end 160 (52 min, 9% flaky)"
    },
    {
      "id": "17-exploratory-charter-writer",
      "name": "Exploratory Charter Writer",
      "description": "Writes exploratory testing charters with missions, risks, time boxes, and note templates.",
      "tool": "write_charters",
      "inputKey": "feature_summary",
      "outputKey": "session_charters",
      "sampleInput": "New bulk-import feature: CSV up to 50k rows, duplicate detection, email report on completion"
    },
    {
      "id": "18-qa-release-checklist-builder",
      "name": "QA Release Checklist Builder",
      "description": "Builds release checklists from scope, risk, and past escapes with clear sign-off gates.",
      "tool": "build_release_checklist",
      "inputKey": "release_scope",
      "outputKey": "qa_checklist",
      "sampleInput": "Release 4.12: new payment provider, 14 tickets, database migration, mobile app update on the same day"
    },
    {
      "id": "19-l10n-test-planner",
      "name": "Localization Test Planner",
      "description": "Plans localization and internationalization tests for locales, text expansion, and formats.",
      "tool": "plan_locale_tests",
      "inputKey": "locale_list",
      "outputKey": "l10n_plan",
      "sampleInput": "Launching in German, Japanese, Arabic and Brazilian Portuguese; currency, dates and addresses vary"
    },
    {
      "id": "20-security-test-case-writer",
      "name": "Security Test Case Writer",
      "description": "Writes security test cases for authentication, authorization, input handling, and abuse paths.",
      "tool": "write_security_tests",
      "inputKey": "feature_flow",
      "outputKey": "security_cases",
      "sampleInput": "Password reset by email link; link valid 1 hour; any user can request unlimited resets"
    }
  ]
};
