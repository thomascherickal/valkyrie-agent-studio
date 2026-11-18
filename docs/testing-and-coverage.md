# Testing & 100% Coverage Guide

Valkyrie enforces **100% test coverage** across Python, TypeScript, and Rust, and keeps every source and test file under **200 lines**.

## Test Suites
1. **Python (`studio-core/`):**
   - Command: `.venv/bin/pytest`
   - Configuration (`pyproject.toml`): `--cov=valkyrie --cov-branch --cov-report=term-missing --cov-fail-under=100`
   - Covers: `api_server`, `command_centre`, `eval_gate`, `ir_schema`, `llm_router`, `metaheuristic_optimizer`, `python_runner`, `rust_transpiler`, and `subscription_manager` (19 tests, 341 statements, 48 branches, 100.00%).
2. **TypeScript & Desktop UI (`studio-ui/`):**
   - Command: `npm test` (`vitest run --coverage`) + `npm run desktop:build`
   - Configuration (`vitest.config.ts`): `lines: 100, branches: 100, functions: 100, statements: 100` across `src/components/**`, `src/theme/**`, and `src/App.tsx`.
3. **Rust Workspace (`Cargo.toml`):**
   - Command: `cargo test --workspace`
   - Covers `rust-runtime-template` (3 unit tests) and all 120 `agents/*/*/rust` crates (120 unit tests).
