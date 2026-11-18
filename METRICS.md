# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (40 passed) | 100.00% (528 stmts, 64 branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (60 passed, 19 files) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (122 crates incl. `valkyrie-studio-tauri`; 131 tests) | 100.00% | Green |
| `agents/` (12 Roles × 10) | 120 focused Python + 120 Rust crates; all 120 `agent.py` also run in the sandbox | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 271 | 5,821 |
| TypeScript (`.ts`/`.tsx`) | 58 | 3,175 |
| Rust | 126 | 3,039 |
| YAML | 121 | 2,661 |
| Markdown | 146 | 2,317 |
| TOML | 125 | 577 |
| CSS | 4 | 506 |
| JSON | 124 | 443 |
| SVG | 120 | 122 |
| HTML | 1 | 19 |
| **Total** | **1,096** | **18,680** |
