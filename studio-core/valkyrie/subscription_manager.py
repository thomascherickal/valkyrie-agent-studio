"""Subscription & free-tier LLM provider switcher (Gemini, OpenCode, OpenRouter, Ollama)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ProviderName = Literal["gemini_free", "opencode_free", "openrouter_free", "gemini_sub", "ollama"]


@dataclass
class ProviderStatus:
    """Tracks availability, rate-limit state, and cost tier for a provider."""

    name: ProviderName
    is_free: bool
    has_subscription: bool
    rate_limited: bool = False
    requests_remaining: int = 100


class SubscriptionManager:
    """Routes requests to free models first, falling back to subscriptions on rate limit."""

    def __init__(self, gemini_sub: bool = False, opencode_sub: bool = False, openrouter_sub: bool = False) -> None:
        self.providers: dict[ProviderName, ProviderStatus] = {
            "gemini_free": ProviderStatus("gemini_free", is_free=True, has_subscription=True),
            "opencode_free": ProviderStatus("opencode_free", is_free=True, has_subscription=opencode_sub),
            "openrouter_free": ProviderStatus("openrouter_free", is_free=True, has_subscription=openrouter_sub),
            "ollama": ProviderStatus("ollama", is_free=True, has_subscription=True),
            "gemini_sub": ProviderStatus("gemini_sub", is_free=False, has_subscription=gemini_sub),
        }
        self.active_provider: ProviderName = "gemini_free"

    def select_provider(self, preferred: ProviderName | None = None) -> tuple[ProviderName, str | None]:
        """Select the best available free provider, or notify and switch to subscription."""
        if preferred and not self.providers[preferred].rate_limited:
            self.active_provider = preferred
            return preferred, None

        for name in ("gemini_free", "opencode_free", "openrouter_free", "ollama"):
            status = self.providers[name]
            if not status.rate_limited and status.requests_remaining > 0:
                self.active_provider = name
                return name, None

        if self.providers["gemini_sub"].has_subscription:
            self.active_provider = "gemini_sub"
            return "gemini_sub", "Free models exhausted; switched to Gemini subscription."

        raise RuntimeError("No free models or active subscriptions available.")

    def mark_rate_limited(self, provider: ProviderName) -> None:
        """Mark a provider as rate-limited."""
        self.providers[provider].rate_limited = True
        self.providers[provider].requests_remaining = 0

