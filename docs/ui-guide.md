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
- **Advanced Mode:** Unlocks the **Design** and **Python** tabs (bespoke `run_agent(payload)` logic) and adds the **Providers** tab: which keys are set (never the key), the fallback order with the free models in use, and a **Reload .env** button.

## Command Centre
The right-hand pane has Start, Stop and Stop all, a **Problems** list, the agent traces, and the **Trace log**:
- Every step of every run appears live, newest first: time since the run started, status (info, ok, warn, error), stage and message. Click a step to open its full recorded detail (the payload, the code size, each provider attempt and its error, token counts, the model's answer, the checks).
- Filter by **Run** or **Status**, **Copy** what is shown, or **Clear** the pane. The same steps are also written to `logs/trace.jsonl`, which Clear does not touch.
- The pane follows the `/ws/trace` WebSocket and polls the REST list if the socket is not available. Secrets are removed before a step is recorded.
