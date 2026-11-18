"""Tests for SubscriptionManager."""

import pytest

from valkyrie.subscription_manager import SubscriptionManager


def test_subscription_manager_free_first_and_fallback() -> None:
    mgr = SubscriptionManager(gemini_sub=True)
    provider, notice = mgr.select_provider()
    assert provider == "gemini_free"
    assert notice is None

    # Preferred provider
    p2, n2 = mgr.select_provider("opencode_free")
    assert p2 == "opencode_free"
    assert n2 is None

    # Exhaust all free providers
    for free_p in ("gemini_free", "opencode_free", "openrouter_free", "ollama"):
        mgr.mark_rate_limited(free_p)

    p3, n3 = mgr.select_provider()
    assert p3 == "gemini_sub"
    assert n3 is not None and "switched to Gemini subscription" in n3


def test_subscription_manager_no_providers_left() -> None:
    mgr = SubscriptionManager(gemini_sub=False)
    for free_p in ("gemini_free", "opencode_free", "openrouter_free", "ollama"):
        mgr.mark_rate_limited(free_p)

    with pytest.raises(RuntimeError, match="No free models or active subscriptions"):
        mgr.select_provider()

