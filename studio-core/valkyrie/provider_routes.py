"""Which model providers have a key, and a way to re-read the .env file. Keys themselves are never sent anywhere."""

from __future__ import annotations

from fastapi import APIRouter

from valkyrie import tracing
from valkyrie.env_file import env_file_path, load_env_file
from valkyrie.fallback import CHAIN, FREE_MODELS, free_models
from valkyrie.llm_router import HOSTED_COMPAT, LLMRouter

router = APIRouter(prefix="/api/providers", tags=["providers"])
KEY_VARS = {"gemini": "GEMINI_API_KEY", **{name: var for name, (_, var) in HOSTED_COMPAT.items()}}


def status() -> dict[str, object]:
    router_ = LLMRouter()
    return {
        "env_file": env_file_path().name,
        "env_path": str(env_file_path()),
        "providers": [{"id": p, "env_var": v, "key_set": router_.has_key(p)} for p, v in KEY_VARS.items()],
        # The order a run falls back in, and the free models each hosted fallback tries.
        "fallback": [{"provider": p, "models": list(free_models(p)) if p in FREE_MODELS else ["gemini-4-hydrogen"]} for p in CHAIN],
    }


@router.get("")
def providers() -> dict[str, object]:
    """For each provider: the variable that holds its key and whether a key is set (never its value)."""
    return status()


@router.post("/reload")
def reload_keys() -> dict[str, object]:
    """Re-read the .env file, so a key you just pasted is used without restarting the API."""
    changed = load_env_file()
    tracing.step("providers.reload", ".env re-read from the Providers tab", names_changed=changed, providers=status()["providers"])
    return {**status(), "changed": changed}
