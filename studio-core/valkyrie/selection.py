"""The provider, model and effort you chose in the Secrets tab. They are saved in .env as VALKYRIE_* variables."""

from __future__ import annotations

import os

# The model each provider uses until you pick another one.
DEFAULT_MODELS = {"gemini": "gemini-4-hydrogen", "openrouter": "openrouter/free", "opencode": "big-pickle"}
EFFORTS = ("low", "medium", "high")
DEFAULT_PROVIDERS = ("gemini", "openrouter", "opencode", "ollama")


def model_var(provider: str) -> str:
    """The .env variable that holds the chosen model of a provider, for example VALKYRIE_OPENCODE_MODEL."""
    return f"VALKYRIE_{provider.upper()}_MODEL"


def chosen_model(provider: str) -> str | None:
    """The model you picked for this provider, or None."""
    return os.environ.get(model_var(provider)) or None


def selected_model(provider: str) -> str:
    return chosen_model(provider) or DEFAULT_MODELS[provider]


def selected_effort(default: str = "low") -> str:
    """The Gemini effort (thinking level) you picked, or `default` when none is set or the value is not valid."""
    value = os.environ.get("VALKYRIE_GEMINI_EFFORT", "")
    return value if value in EFFORTS else default


def default_provider() -> str:
    return os.environ.get("VALKYRIE_MODEL_PROVIDER", "gemini")
