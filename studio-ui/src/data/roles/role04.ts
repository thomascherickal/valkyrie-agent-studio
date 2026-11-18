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
    }
  ]
};
