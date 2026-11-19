# Studio UI & Standalone Desktop Guide (`studio-ui`)

## Standalone Desktop Architecture (Tauri v2 Rust Shell)
- **Entrypoint:** `studio-ui/src-tauri/src/lib.rs` launches a `1440×920` native WebView window loading `../dist` (or `http://localhost:5173` in dev mode).
- **Native Rust Commands:** `get_runtime_info()` and `run_rust_agent(agent_id, prompt)` invoke `valkyrie-rust-runtime` directly in Rust.
- **Build Command:** `npm run desktop:build` runs `tsc && vite build && cargo build --manifest-path src-tauri/Cargo.toml`.

## Modern Web Standards Compliance
- **3-State Color Scheme (`index.html`, `ThemeProvider.tsx`, `studio.css`):**
  - `<meta name="color-scheme" content="light dark">` paired with an inline FOUC-prevention script in `<head>`.
  - `:root` binds `color-scheme: light dark` and maps `<meta>` overrides via `:has(> head > meta[name="color-scheme"][content="dark"|"light"])`.
  - Uses `light-dark()` tokens with `@media (prefers-color-scheme: dark)` and `@supports (color: light-dark(white, black))` fallbacks.
  - Choosing **System** removes the `localStorage` override rather than pinning the current OS theme.
- **Layout & Scroll Containment (`studio.css`):**
  - CSS Grid `grid-template-areas` (`titlebar`, `sidebar`, `workspace`) with `min-block-size: 100dvb`, `scrollbar-gutter: stable`, and `overscroll-behavior: contain`.
  - Named container query (`container: workspace / inline-size`) switches cards to 2 columns above `720px`.
- **Native Modal (`RustDeployModal.tsx`):**
  - Uses native `<dialog>` controlled via `showModal()` and `close()`, with `overscroll-behavior: contain` on `dialog:modal` and `dialog::backdrop`.

## Experience Modes
- **Beginner Mode:** Visual Agent Builder, 240-Agent Role Tree, Focused Tool & Demo Preview, Subscription Switcher, and Sandbox Console.
- **Intermediate Mode:** Unlocks `CustomPythonEditor.tsx` for bespoke `run_agent(payload)` logic.
- **Advanced Mode:** Unlocks `CommandCentre.tsx` with Start, Stop, Admin Stop All, and live visual step traces.
