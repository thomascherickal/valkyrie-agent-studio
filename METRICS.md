# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (20 passed) | 100.00% (362 stmts, 48 branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (1 passed) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (122 crates incl. `valkyrie-studio-tauri`) | 100.00% | Green |
| `agents/` (12 Roles × 10) | 120 focused Python + 120 Rust crates | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 264 | 5,198 |
| Rust | 125 | 2,838 |
| YAML | 121 | 2,661 |
| Markdown | 146 | 2,265 |
| TypeScript (`.ts`/`.tsx`) | 28 | 1,776 |
| TOML | 125 | 577 |
| JSON | 124 | 445 |
| CSS | 1 | 142 |
| SVG | 120 | 122 |
| HTML | 1 | 19 |
| **Total** | **1,055** | **16,043** |
