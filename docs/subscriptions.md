# Subscriptions & Free-Tier Routing

`SubscriptionManager` (`studio-core/valkyrie/subscription_manager.py`) minimizes LLM spend by prioritizing free-tier and local providers before falling back to paid subscriptions.

## Routing Order
1. `gemini_free` — Gemini 4 Hydrogen (`gemini-4-hydrogen`, `thinking_level: "low"`), free tier.
2. `opencode_free` — OpenCode free-tier model routing.
3. `openrouter_free` — OpenRouter `:free` model routing.
4. `ollama` — Local offline inference at `http://localhost:11434/v1` (`qwen3.5:latest`).
5. `gemini_sub` — Paid Gemini subscription fallback; only activated after all free providers are marked rate-limited or exhausted, returning an explicit user notification (`"Free models exhausted; switched to Gemini subscription."`).

## Pricing Reference (Paid Gemini 4 Hydrogen)
- **Input:** `$1.50 / 1M` tokens
- **Cached Input:** `$0.075 / 1M` tokens
- **Output:** `$7.50 / 1M` tokens
- **Ollama (Local):** `$0.00`
