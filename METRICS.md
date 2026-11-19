# Software Metrics

## Test Coverage & Build Gate
| Component | Test Suite / Build | Coverage | Status |
| :--- | :--- | :--- | :--- |
| `studio-core` (Python) | `pytest` (168 passed) | 100.00% (stmts and branches) | Green |
| `command-centre` (Python) | `pytest` (1 passed) | 100.00% (40 stmts, 6 branches) | Green |
| `studio-ui` (TypeScript + Tauri v2) | `desktop:build` + `vitest` (156 passed, 37 files) | 100.00% (stmts, branch, funcs, lines) | Green |
| `Cargo.toml` Workspace (Rust) | `cargo test --workspace` (242 crates incl. `valkyrie-studio-tauri`, 12 shell tests) | 100.00% | Green |
| `agents/` (12 Roles × 20) | 240 focused Python + 240 Rust crates; 240 playbooks; all 720 generated Python versions run in the sandbox with only their example data; the UI catalog and `agents/` folders are checked against each other | 100% populated & verified | Green |

## Source Files & Line Counts by Language
*(Excludes generated dependencies/artifacts ignored by `.gitignore`, `package-lock.json`, and `Cargo.lock`. Reproduce with `python3 scripts/count_loc.py`, which counts tracked and untracked files by extension.)*

| Language | Source Files | Total Lines |
| :--- | ---: | ---: |
| Python | 606 | 16,795 |
| Markdown | 307 | 11,299 |
| TypeScript (`.ts`/`.tsx`) | 89 | 6,688 |
| Rust | 248 | 5,769 |
| YAML | 241 | 5,301 |
| JSON | 247 | 1,275 |
| TOML | 245 | 1,062 |
| CSS | 7 | 682 |
| SVG | 240 | 242 |
| HTML | 1 | 20 |
| **Total** | **2,231** | **49,133** |
