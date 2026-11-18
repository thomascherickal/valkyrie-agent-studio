# Valkyrie Project Rules

- **100% Test Coverage:** Maintain 100% test coverage across TypeScript (`vitest`), Python (`pytest --cov-fail-under=100`), and Rust (`cargo test --workspace`).
- **Pre-Commit Gate:** Run `make test-all`, `cd studio-ui && npm run desktop:build`, and `cargo test --workspace` before every commit; do not commit unless all checks are green.
- **Metrics & Next Steps Tracking:** Update `METRICS.md` (including the per-language source file and line count summary table) and `NEXT-STEPS.md` after every commit.
- **Modularity:** Keep every source and test file under 200 lines and decompose modules, catalog data, and tests into focused folders.
- **Modern Web Standards:** Use native `<dialog>`, `<meta name="color-scheme">` + `light-dark()` with fallbacks, CSS Grid/Container Queries, and `overscroll-behavior: contain` in `studio-ui/`.
