import React from "react";

export type SubscriptionProvider =
  | "gemini_free"
  | "opencode_free"
  | "openrouter_free"
  | "ollama"
  | "gemini_sub";

interface SubscriptionSwitcherProps {
  selected: SubscriptionProvider;
  onSelect: (provider: SubscriptionProvider) => void;
}

export function SubscriptionSwitcher({ selected, onSelect }: SubscriptionSwitcherProps) {
  return (
    <section aria-label="Subscription and Provider Switcher">
      <h2>LLM Provider &amp; Subscriptions</h2>
      <label>
        Active Provider
        <select
          aria-label="Subscription Provider"
          value={selected}
          onChange={(e) => onSelect(e.target.value as SubscriptionProvider)}
        >
          <option value="gemini_free">Gemini 4 Hydrogen (Free Tier)</option>
          <option value="opencode_free">OpenCode (Free Tier)</option>
          <option value="openrouter_free">OpenRouter (Free Models)</option>
          <option value="ollama">Local Ollama (Offline Free)</option>
          <option value="gemini_sub">Gemini Subscription (Paid Fallback)</option>
        </select>
      </label>
    </section>
  );
}

