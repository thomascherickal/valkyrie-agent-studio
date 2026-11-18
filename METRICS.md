# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (70 passed) | 100.00% (803 stmts, 116 branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (118 passed, 29 files) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (122 crates incl. `valkyrie-studio-tauri`; 131 tests) | 100.00% | Green |
| `agents/` (12 Roles × 10) | 120 focused Python + 120 Rust crates; 120 playbooks; all 360 generated Python versions run in the sandbox with only their example data | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 295 | 8,644 |
| TypeScript (`.ts`/`.tsx`) | 74 | 4,331 |
| Rust | 126 | 3,039 |
| YAML | 121 | 2,661 |
| Markdown | 146 | 2,344 |
| TOML | 125 | 577 |
| CSS | 4 | 544 |
| JSON | 124 | 443 |
| SVG | 120 | 122 |
| HTML | 1 | 20 |
| **Total** | **1,136** | **22,725** |
