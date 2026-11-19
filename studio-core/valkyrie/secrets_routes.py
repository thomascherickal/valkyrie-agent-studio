"""The Secrets tab's API: keys (shown masked, never returned whole), model and effort choices, model lists, Test Key."""

from __future__ import annotations

import os
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from valkyrie import tracing
from valkyrie.key_check import check_key
from valkyrie.model_catalog import catalog
from valkyrie.provider_routes import status as provider_status
from valkyrie.secrets_store import KEY_VARS, key_preview, set_env_value
from valkyrie.selection import DEFAULT_PROVIDERS, EFFORTS, default_provider, model_var, selected_effort, selected_model

router = APIRouter(prefix="/api/secrets", tags=["secrets"])
LABELS = {"gemini": "Gemini", "openrouter": "OpenRouter", "opencode": "OpenCode"}


class SecretBody(BaseModel):
    """What to change. A field you leave out is left alone. An empty key removes the key."""

    key: str | None = Field(default=None, max_length=512)
    model: str | None = Field(default=None, max_length=200)
    effort: str | None = None


class TestBody(BaseModel):
    """Test the key you typed (not saved yet), or the saved one when `key` is left out, with this model."""

    key: str | None = Field(default=None, max_length=512)
    model: str | None = Field(default=None, max_length=200)


class DefaultBody(BaseModel):
    provider: str


def _provider(name: str) -> str:
    if name not in KEY_VARS:
        raise HTTPException(status_code=404, detail=f"Unknown provider {name}")
    return name


def _entry(provider: str) -> dict[str, Any]:
    return {
        "id": provider, "label": LABELS[provider], "env_var": KEY_VARS[provider], "key_set": bool(os.environ.get(KEY_VARS[provider])),
        "preview": key_preview(provider), "model": selected_model(provider), "effort": selected_effort() if provider == "gemini" else None,
    }


def _state() -> dict[str, Any]:
    entries = [_entry(p) for p in KEY_VARS]
    return {**provider_status(), "secrets": entries, "default_provider": default_provider(), "default_providers": list(DEFAULT_PROVIDERS),
            "efforts": list(EFFORTS), "simulated": not any(e["key_set"] for e in entries)}


def _save(name: str, value: str) -> None:
    try:
        set_env_value(name, value)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("")
def get_secrets() -> dict[str, Any]:
    """Every provider's masked key, chosen model and effort, plus the fallback order and whether output is simulated."""
    return _state()


@router.put("/default-provider")
def set_default_provider(body: DefaultBody) -> dict[str, Any]:
    if body.provider not in DEFAULT_PROVIDERS:
        raise HTTPException(status_code=400, detail=f"Choose one of {', '.join(DEFAULT_PROVIDERS)}")
    _save("VALKYRIE_MODEL_PROVIDER", body.provider)
    tracing.step("secrets.default", f"default provider is now {body.provider}", provider=body.provider)
    return _state()


@router.get("/{provider}/models")
def get_models(provider: str) -> dict[str, Any]:
    """The model slugs this provider offers (live when reachable, free ones first), and the effort levels."""
    name = _provider(provider)
    return {**catalog(name, os.environ.get(KEY_VARS[name], "")), "efforts": list(EFFORTS) if name == "gemini" else []}


@router.put("/{provider}")
def save_secret(provider: str, body: SecretBody) -> dict[str, Any]:
    """Save a key, a model or an effort to .env. The key is never echoed back, only its masked preview."""
    name = _provider(provider)
    if body.effort is not None and (name != "gemini" or body.effort not in EFFORTS):
        raise HTTPException(status_code=400, detail="Effort applies to Gemini and must be low, medium or high")
    changed = []
    if body.key is not None:
        _save(KEY_VARS[name], body.key.strip())
        changed.append("key")
    if body.model is not None:
        _save(model_var(name), body.model)
        changed.append("model")
    if body.effort is not None:
        _save("VALKYRIE_GEMINI_EFFORT", body.effort)
        changed.append("effort")
    tracing.step("secrets.save", f"saved {', '.join(changed) or 'nothing'} for {name}", provider=name, changed=changed)
    return _entry(name)


@router.post("/{provider}/test")
def test_secret(provider: str, body: TestBody) -> dict[str, Any]:
    """Test Key: one real request. The result says whether it worked and, if not, the likely causes."""
    name = _provider(provider)
    key = (body.key if body.key is not None else os.environ.get(KEY_VARS[name], "")).strip()
    if not key:
        return {"ok": False, "status": None, "ms": 0, "provider": name, "model": body.model or selected_model(name),
                "message": "No key to test.", "causes": ["No key is set for this provider: paste one first, or save it."]}
    return check_key(name, key, body.model or selected_model(name))
