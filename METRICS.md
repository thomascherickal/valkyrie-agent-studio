# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (85 passed) | 100.00% (stmts and branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (134 passed, 34 files) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (242 crates incl. `valkyrie-studio-tauri`) | 100.00% | Green |
| `agents/` (12 Roles × 20) | 240 focused Python + 240 Rust crates; 240 playbooks; all 720 generated Python versions run in the sandbox with only their example data; the UI catalog and `agents/` folders are checked against each other | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 580 | 14,644 |
| TypeScript (`.ts`/`.tsx`) | 82 | 5,863 |
| Rust | 246 | 5,679 |
| YAML | 241 | 5,301 |
| Markdown | 266 | 4,274 |
| TOML | 245 | 1,057 |
| JSON | 244 | 803 |
| CSS | 5 | 543 |
| SVG | 240 | 242 |
| HTML | 1 | 20 |
| **Total** | **2,150** | **38,426** |
