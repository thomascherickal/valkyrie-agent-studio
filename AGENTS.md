# AGENTS.md

Project-wide rules and automation standards for all coding agents and contributors.

## 1. Testing & Coverage

- **100% Test & Code Coverage**: Maintain 100% test pass rate and 100% code coverage before any commit.
- **Core Test Scope**: Tests must cover:
  - Functional scenarios
  - Edge-case scenarios
  - Regression scenarios
- **Expanded Test Categories** (introduce and maintain as the project grows):
  - **Unit tests** (isolated component/function behavior)
  - **Integration tests** (interactions between modules, services, and data layers)
  - **Smoke tests** (fast sanity checks verifying critical paths work after builds/deployments)
  - **End-to-end (E2E) tests** (full user-facing workflows across the entire stack)
  - **Performance & load tests** (latency, throughput, and behavior under expected/peak load)
  - **Security tests** (authentication, authorization, input validation, and vulnerability checks)
- **Test Suite Runtime Limit**: Optimize the complete test suite so that it never takes more than **30 minutes** to run.
- **Live Test Timing**: Maintain `test-time-report.md` in every repository to record live execution times for all tests and suites, flagging slow tests for optimization.
- **Commit Gate**: Enforce a commit/CI gate that blocks commits and merges if any test fails, if code coverage drops below 100%, or if the test suite exceeds the 30-minute limit.

## 2. Code Quality, Modularity & Optimization

- **File Size Limit**: No source code or test file may exceed **200 lines**. Split larger files into smaller, coherent modules.
- **Design Principles**: Strictly enforce **DRY** (Don't Repeat Yourself) and **SOLID** principles.
- **Duplicate Code Detection**: Continuously scan for and eliminate duplicate code.
- **Per-Commit Code Optimization**: On every commit, review and optimize the code to check whether it can run faster and remove any unnecessary, redundant, or dead blocks of code.
- **Language-Specific Tooling**: Suggest, install, and configure appropriate linters, formatters, type checkers, and static analysis tools for the project's language(s).

## 3. Resource Management & Performance

- **CPU & GPU Profiling**: Profile CPU and GPU usage during builds, test runs, and runtime execution to detect bottlenecks and prevent system overload.
- **Profile Reporting**: Store and keep CPU and GPU profile results up to date in `system-profile.md`.

## 4. Documentation & Project Files

Every project must include and keep up to date (after every push):

- `readme.md` (both full documentation and a quick-start guide)
- `next-steps.md` (reusable post-commit/push checklist)
- `metrics.md` (project health, coverage, performance, and quality metrics)
- `test-time-report.md` (live timing report tracking how long all tests take to run)
- `system-profile.md` (CPU and GPU profiling results and resource-usage trends)

> **Naming Convention**: Name all Markdown files in lowercase `kebab-case` (e.g., `readme.md`, `next-steps.md`, `metrics.md`, `test-time-report.md`, `system-profile.md`), keeping uppercase only where strictly required by external tools (`AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `SKILL.md`).

## 5. Licensing

- **Default License**: **AGPL-v3**.
- **Terms**: Free for internal use; commercial use requires a separate commercial license from **Thomas Cherickal**.

## 6. Automation

- Automate all of the above—testing across all applicable categories, 100% coverage verification, 30-minute test-suite runtime enforcement, live `test-time-report.md` updates, 200-line file-length checks, duplicate-code detection, per-commit optimization checks, linting/formatting, CPU/GPU profiling (`system-profile.md`), commit gates, and documentation/metrics updates—via Git hooks and CI/CD pipelines.

## 7. Post-Commit / Post-Push Checklist (`next-steps.md`)

Run the following steps after each commit/push:

1. Verify all functional, edge-case, regression, and applicable expanded tests (unit, integration, smoke, E2E, performance/load, security) pass.
2. Confirm 100% code coverage with zero regressions.
3. Verify the complete test suite runs in under 30 minutes and update `test-time-report.md` with live timings.
4. Verify no code or test file exceeds 200 lines.
5. Run duplicate-code detection, review for per-commit performance optimizations, and remove any unnecessary or dead code blocks.
6. Run language-specific linters, formatters, and static analysis checks (DRY/SOLID compliance).
7. Profile CPU and GPU usage, verify no resource overload or performance regressions, and update `system-profile.md`.
8. Confirm the commit/CI gate passed cleanly.
9. Update `metrics.md` with the latest test, coverage, and performance metrics.
10. Update `readme.md` (full docs and quick-start) to reflect any changes.
11. Review and update `next-steps.md` with any follow-up actions for the next iteration.
12. After all that is done, commit or push the changes to the repository.

---

## Project-Specific Rules & Context

# Valkyrie Project Rules

- **100% Test Coverage:** Maintain 100% test coverage across TypeScript (`vitest`), Python (`pytest --cov-fail-under=100`), and Rust (`cargo test --workspace`).
- **Pre-Commit Gate:** Run `make test-all`, `cd studio-ui && npm run desktop:build`, and `cargo test --workspace` before every commit; do not commit unless all checks are green.
- **Metrics & Next Steps Tracking (automatic, enforced by git hooks):** Never commit or push without `METRICS.md` and `NEXT-STEPS.md` being current, and do it without being asked. The hooks in `.githooks/` enforce it; run `make hooks` once in every clone (it sets `core.hooksPath`).
  - **On every commit** (`pre-commit`): the hook rewrites the per-language table in `METRICS.md` from the real counts (`scripts/update_metrics.py`, also `make metrics`) and stages it, and it refuses the commit unless `NEXT-STEPS.md` is part of it. You still update the rest by hand in the same commit: the test counts and coverage rows from the gate run, and `NEXT-STEPS.md` (tick what is done, add what you discovered, remove what no longer applies, renumber).
  - **Before every push** (`pre-push`): the hook refuses to push while the table in `METRICS.md` differs from the real counts (for example after a merge or a rebase). Run `make metrics`, commit, and push again.
  - **A docs-only change still counts:** it changes the Markdown line counts, so `METRICS.md` changes too.
  - `SKIP_TRACKING=1` skips both hooks for one command (a revert, say). Never use `--no-verify` to get around them.
- **Merge and Clean Up (STRICT, no exceptions):**
  - **Merge automatically when work is finished.** Once a piece of work is complete and every gate in the Pre-Commit Gate is green, commit, push, open the pull request and merge it into `main` yourself straight away (`gh pr merge --merge`). Never ask first, never leave finished work on an unmerged branch or in an open PR, and never end a session with finished work unmerged. The only exceptions are a failing gate (do not merge; report it) and work still in progress.
  - **Remove stale worktrees.** Right after every merge, and at the start of every session, run `make clean-worktrees` (`DRY=1` to preview). It prunes worktrees whose folder is gone, unlocks and prunes ones locked by an ended session, and deletes local branches already merged into `main`. Once your own worktree's work is merged, leave it and remove it and its branch too. Never leave stale worktrees or merged branches behind.
  - **Never remove work that is not merged.** Do not delete a worktree that has uncommitted or unmerged changes or whose folder still exists and may be in use; the script only touches stale ones and deletes branches with `git branch -d`, which refuses unmerged work.
- **Modularity:** Keep every source and test file under 200 lines and decompose modules, catalog data, and tests into focused folders. The `.claude/skills/` directory is excluded from this limit (it is vendored skill tooling, not project source).
- **Autonomous Delivery:** Work autonomously without asking for confirmation between steps. Keep `NEXT-STEPS.md` current as you go: tick what is done, add what you discover. When a task finishes, pick up the next step listed there and continue. Once a feature is complete and every gate in the Pre-Commit Gate is green, commit it, push the branch, and merge it into `main` (through a pull request) without waiting for approval. Never force-push, never merge or push with a failing gate, and stop to ask only when blocked by something that needs the user (credentials, a destructive or irreversible action, or an ambiguous requirement where a wrong guess is costly).
- **Modern Web Standards:** Use native `<dialog>`, `<meta name="color-scheme">` + `light-dark()` with fallbacks, CSS Grid/Container Queries, and `overscroll-behavior: contain` in `studio-ui/`.
