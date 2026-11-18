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
    }
  ]
};
