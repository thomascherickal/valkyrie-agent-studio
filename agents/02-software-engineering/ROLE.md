# Software Engineering

Software Engineering suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
