import type { RoleCatalog } from "../types";

export const ROLE_02: RoleCatalog = {
  "id": "02-software-engineering",
  "name": "Software Engineering",
  "agents": [
    {
      "id": "01-architecture-reviewer",
      "name": "Architecture Reviewer",
      "description": "Audits RFCs for single points of failure, coupling, and backpressure gaps.",
      "tool": "check_failure_modes",
      "inputKey": "rfc_summary",
      "outputKey": "review_findings",
      "sampleInput": "Event-driven billing worker consuming Kafka with Postgres outbox"
    },
    {
      "id": "02-pr-code-reviewer",
      "name": "PR Code Reviewer",
      "description": "Inspects code diffs for boundary bugs, resource leaks, and missing tests.",
      "tool": "detect_antipatterns",
      "inputKey": "diff_snippet",
      "outputKey": "review_comments",
      "sampleInput": "for item in items: db.query(item.id) # N+1 inside loop"
    },
    {
      "id": "03-refactor-planner",
      "name": "Refactor Planner",
      "description": "Plans incremental strangler-fig extractions without breaking public callers.",
      "tool": "plan_strangler_steps",
      "inputKey": "module_metrics",
      "outputKey": "refactor_plan",
      "sampleInput": "monolith_auth.py: 1850 LOC, 14 callers, 0% unit tests"
    },
    {
      "id": "04-api-contract-designer",
      "name": "API Contract Designer",
      "description": "Designs versioned REST/OpenAPI schemas and detects breaking field changes.",
      "tool": "validate_openapi_diff",
      "inputKey": "endpoint_spec",
      "outputKey": "contract_yaml",
      "sampleInput": "POST /v2/agents/{id}/deploy returning crate bundle"
    },
    {
      "id": "05-sql-query-optimizer",
      "name": "SQL Query Optimizer",
      "description": "Analyzes EXPLAIN plans and recommends composite indexes and query rewrites.",
      "tool": "suggest_indexes",
      "inputKey": "sql_query",
      "outputKey": "optimization_plan",
      "sampleInput": "SELECT * FROM runs WHERE org_id = $1 ORDER BY created_at DESC"
    },
    {
      "id": "06-dependency-auditor",
      "name": "Dependency Auditor",
      "description": "Checks lockfiles for unmaintained packages, license conflicts, and bloat.",
      "tool": "scan_licenses",
      "inputKey": "dependencies",
      "outputKey": "audit_report",
      "sampleInput": "requests==2.32.0, pyyaml==6.0.2, gpl-lib==1.0"
    },
    {
      "id": "07-migration-assistant",
      "name": "Migration Assistant",
      "description": "Generates reversible expand-and-contract database migration scripts.",
      "tool": "gen_expand_contract",
      "inputKey": "schema_change",
      "outputKey": "migration_sql",
      "sampleInput": "Rename users.full_name to display_name without downtime"
    },
    {
      "id": "08-tech-debt-triager",
      "name": "Tech Debt Triager",
      "description": "Ranks tech debt hotspots by churn frequency multiplied by complexity.",
      "tool": "score_debt_roi",
      "inputKey": "debt_items",
      "outputKey": "prioritized_debt",
      "sampleInput": "Legacy YAML parser (high churn, 12 bugs/quarter)"
    },
    {
      "id": "09-concurrency-debugger",
      "name": "Concurrency Debugger",
      "description": "Identifies lock ordering inversions, unawaited futures, and race windows.",
      "tool": "analyze_lock_graph",
      "inputKey": "async_trace",
      "outputKey": "deadlock_report",
      "sampleInput": "Task A holds lock1->lock2 while Task B holds lock2->lock1"
    },
    {
      "id": "10-rust-port-advisor",
      "name": "Rust Port Advisor",
      "description": "Profiles CPU-bound Python hotspots and plans zero-GIL PyO3/Tokio ports.",
      "tool": "estimate_rust_speedup",
      "inputKey": "profile_stats",
      "outputKey": "port_blueprint",
      "sampleInput": "json_validator.py: 68% CPU time, 42ms p99"
    },
    {
      "id": "11-error-handling-auditor",
      "name": "Error Handling Auditor",
      "description": "Audits code for swallowed exceptions, vague errors, missing retries, and unsafe fallbacks.",
      "tool": "audit_error_paths",
      "inputKey": "code_excerpt",
      "outputKey": "error_audit",
      "sampleInput": "try: charge(card) except Exception: pass  # then marks the order paid"
    },
    {
      "id": "12-api-sunset-planner",
      "name": "API Version Sunset Planner",
      "description": "Plans API version retirement with usage data, client notice, brownouts, and migration support.",
      "tool": "plan_api_sunset",
      "inputKey": "api_usage",
      "outputKey": "sunset_schedule",
      "sampleInput": "v1 receives 2.1M calls a day from 140 clients; top 5 clients are 70% of traffic; v2 is stable"
    },
    {
      "id": "13-feature-flag-cleaner",
      "name": "Feature Flag Cleaner",
      "description": "Finds stale feature flags and plans safe removal with owners, tests, and rollout checks.",
      "tool": "find_stale_flags",
      "inputKey": "flag_inventory",
      "outputKey": "cleanup_plan",
      "sampleInput": "214 flags, 88 older than 6 months, 31 at 100% rollout for over 90 days, owners missing on 40"
    },
    {
      "id": "14-module-boundary-checker",
      "name": "Module Boundary Checker",
      "description": "Checks dependency graphs for cycles, layer violations, and hidden coupling between modules.",
      "tool": "check_module_boundaries",
      "inputKey": "dependency_graph",
      "outputKey": "boundary_report",
      "sampleInput": "billing imports orders; orders imports billing; reports reads the orders table directly"
    },
    {
      "id": "15-logging-quality-reviewer",
      "name": "Logging Quality Reviewer",
      "description": "Reviews log statements for structure, levels, sensitive data, noise, and missing context.",
      "tool": "review_log_statements",
      "inputKey": "log_samples",
      "outputKey": "logging_review",
      "sampleInput": "logger.info(\"user \" + email + \" paid \" + card_number); logger.debug(\"here\")"
    },
    {
      "id": "16-cache-strategy-advisor",
      "name": "Cache Strategy Advisor",
      "description": "Designs cache layers, keys, expiry, and invalidation from the observed access pattern.",
      "tool": "design_cache_strategy",
      "inputKey": "access_pattern",
      "outputKey": "cache_design",
      "sampleInput": "Product pages: 800 reads/s, 2 writes/s, 95% of reads hit 5% of products, stale up to 60s is fine"
    },
    {
      "id": "17-type-safety-planner",
      "name": "Type Safety Hardener",
      "description": "Plans gradual type-checking adoption with strictness steps, hotspots, and CI gates.",
      "tool": "plan_type_hardening",
      "inputKey": "codebase_stats",
      "outputKey": "typing_roadmap",
      "sampleInput": "TypeScript 180k lines, strict off, 1,900 uses of any, 22% of bugs last quarter were undefined errors"
    },
    {
      "id": "18-idempotency-reviewer",
      "name": "Idempotency Reviewer",
      "description": "Reviews endpoints and consumers for safe retries, duplicate delivery, and exactly-once illusions.",
      "tool": "check_idempotency",
      "inputKey": "endpoint_spec",
      "outputKey": "idempotency_review",
      "sampleInput": "POST /payments creates a charge; mobile app retries on timeout; webhook consumer processes events"
    },
    {
      "id": "19-code-owner-mapper",
      "name": "Code Ownership Mapper",
      "description": "Maps files to owners from commit history and flags orphaned or overloaded areas.",
      "tool": "map_code_owners",
      "inputKey": "commit_history",
      "outputKey": "owners_map",
      "sampleInput": "payments/ last 12 months: 3 authors left, 1 remaining (62% of commits); search/ has no commits in 9 months"
    },
    {
      "id": "20-codebase-onboarding-guide",
      "name": "Codebase Onboarding Guide",
      "description": "Writes a first-week onboarding guide for a repository with setup, code map, first task, and norms.",
      "tool": "write_onboarding_guide",
      "inputKey": "repo_overview",
      "outputKey": "onboarding_guide",
      "sampleInput": "Monorepo with 3 services and a web app; setup takes a day; tests flaky on the first run"
    }
  ]
};
