# Software Engineering

Software Engineering suite of 20 focused autonomous agents in Valkyrie Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-architecture-reviewer` — **Architecture Reviewer**: Audits RFCs for single points of failure, coupling, and backpressure gaps. (Tool: `check_failure_modes`)
- `02-pr-code-reviewer` — **PR Code Reviewer**: Inspects code diffs for boundary bugs, resource leaks, and missing tests. (Tool: `detect_antipatterns`)
- `03-refactor-planner` — **Refactor Planner**: Plans incremental strangler-fig extractions without breaking public callers. (Tool: `plan_strangler_steps`)
- `04-api-contract-designer` — **API Contract Designer**: Designs versioned REST/OpenAPI schemas and detects breaking field changes. (Tool: `validate_openapi_diff`)
- `05-sql-query-optimizer` — **SQL Query Optimizer**: Analyzes EXPLAIN plans and recommends composite indexes and query rewrites. (Tool: `suggest_indexes`)
- `06-dependency-auditor` — **Dependency Auditor**: Checks lockfiles for unmaintained packages, license conflicts, and bloat. (Tool: `scan_licenses`)
- `07-migration-assistant` — **Migration Assistant**: Generates reversible expand-and-contract database migration scripts. (Tool: `gen_expand_contract`)
- `08-tech-debt-triager` — **Tech Debt Triager**: Ranks tech debt hotspots by churn frequency multiplied by complexity. (Tool: `score_debt_roi`)
- `09-concurrency-debugger` — **Concurrency Debugger**: Identifies lock ordering inversions, unawaited futures, and race windows. (Tool: `analyze_lock_graph`)
- `10-rust-port-advisor` — **Rust Port Advisor**: Profiles CPU-bound Python hotspots and plans zero-GIL PyO3/Tokio ports. (Tool: `estimate_rust_speedup`)
- `11-error-handling-auditor` — **Error Handling Auditor**: Audits code for swallowed exceptions, vague errors, missing retries, and unsafe fallbacks. (Tool: `audit_error_paths`)
- `12-api-sunset-planner` — **API Version Sunset Planner**: Plans API version retirement with usage data, client notice, brownouts, and migration support. (Tool: `plan_api_sunset`)
- `13-feature-flag-cleaner` — **Feature Flag Cleaner**: Finds stale feature flags and plans safe removal with owners, tests, and rollout checks. (Tool: `find_stale_flags`)
- `14-module-boundary-checker` — **Module Boundary Checker**: Checks dependency graphs for cycles, layer violations, and hidden coupling between modules. (Tool: `check_module_boundaries`)
- `15-logging-quality-reviewer` — **Logging Quality Reviewer**: Reviews log statements for structure, levels, sensitive data, noise, and missing context. (Tool: `review_log_statements`)
- `16-cache-strategy-advisor` — **Cache Strategy Advisor**: Designs cache layers, keys, expiry, and invalidation from the observed access pattern. (Tool: `design_cache_strategy`)
- `17-type-safety-planner` — **Type Safety Hardener**: Plans gradual type-checking adoption with strictness steps, hotspots, and CI gates. (Tool: `plan_type_hardening`)
- `18-idempotency-reviewer` — **Idempotency Reviewer**: Reviews endpoints and consumers for safe retries, duplicate delivery, and exactly-once illusions. (Tool: `check_idempotency`)
- `19-code-owner-mapper` — **Code Ownership Mapper**: Maps files to owners from commit history and flags orphaned or overloaded areas. (Tool: `map_code_owners`)
- `20-codebase-onboarding-guide` — **Codebase Onboarding Guide**: Writes a first-week onboarding guide for a repository with setup, code map, first task, and norms. (Tool: `write_onboarding_guide`)
