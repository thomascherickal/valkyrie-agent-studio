# Valkyrie Project Rules

- **100% Test Coverage:** Maintain 100% test coverage across TypeScript (`vitest`), Python (`pytest --cov-fail-under=100`), and Rust (`cargo test --workspace`).
- **Pre-Commit Gate:** Run `make test-all`, `cd studio-ui && npm run desktop:build`, and `cargo test --workspace` before every commit; do not commit unless all checks are green.
- **Metrics & Next Steps Tracking:** Update `METRICS.md` (including the per-language source file and line count summary table) and `NEXT-STEPS.md` after every commit.
- **Modularity:** Keep every source and test file under 200 lines and decompose modules, catalog data, and tests into focused folders.
- **Autonomous Delivery:** Work autonomously without asking for confirmation between steps. Keep `NEXT-STEPS.md` current as you go: tick what is done, add what you discover. When a task finishes, pick up the next step listed there and continue. Once a feature is complete and every gate in the Pre-Commit Gate is green, commit it, push the branch, and merge it into `main` (through a pull request) without waiting for approval. Never force-push, never merge or push with a failing gate, and stop to ask only when blocked by something that needs the user (credentials, a destructive or irreversible action, or an ambiguous requirement where a wrong guess is costly).
- **Modern Web Standards:** Use native `<dialog>`, `<meta name="color-scheme">` + `light-dark()` with fallbacks, CSS Grid/Container Queries, and `overscroll-behavior: contain` in `studio-ui/`.
