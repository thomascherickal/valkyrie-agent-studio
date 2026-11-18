# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (29 passed) | 100.00% (454 stmts, 54 branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (40 passed, 15 files) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (122 crates incl. `valkyrie-studio-tauri`; 131 tests) | 100.00% | Green |
| `agents/` (12 Roles × 10) | 120 focused Python + 120 Rust crates | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 269 | 5,537 |
| Rust | 126 | 3,039 |
| TypeScript (`.ts`/`.tsx`) | 53 | 2,716 |
| YAML | 121 | 2,661 |
| Markdown | 146 | 2,308 |
| TOML | 125 | 577 |
| CSS | 4 | 483 |
| JSON | 124 | 443 |
| SVG | 120 | 122 |
| HTML | 1 | 19 |
| **Total** | **1,089** | **17,905** |
