"""View, edit, check, save and revert the Python implementations of each agent.

Every agent has three built-in implementations (rules, pipeline, hybrid). Their originals are rendered from the
repo and never written. An edit is saved apart in edits_dir()/<role>/<agent>/<impl>.py and reverting deletes it.
New implementations you save live in edits_dir()/<role>/<agent>/saved/<slug>.py and are always extra: they never
replace an original.
"""

from __future__ import annotations

from pathlib import Path
import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from valkyrie import tracing
from valkyrie.agent_explanation import explanation
from valkyrie.agent_impls import REPO, VARIANTS, AgentSpec, load_spec, playbook_for, render
from valkyrie.python_runner import run_custom_python, validate_python_source
from valkyrie.storage import edits_dir

router = APIRouter(prefix="/api/agents/{role_id}/{agent_id}", tags=["agent-implementations"])

MAX_CODE_CHARS = 100_000
SAVED_PREFIX = "saved-"


class CodeBody(BaseModel):
    """Source to save or check."""

    code: str = Field(max_length=MAX_CODE_CHARS)


class NewImplementation(CodeBody):
    """A new implementation to save next to the built-in ones."""

    name: str = Field(max_length=60)


def _spec(role_id: str, agent_id: str) -> AgentSpec:
    try:
        return load_spec(role_id, agent_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except LookupError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


def _folder(spec: AgentSpec) -> Path:
    return edits_dir() / spec.role_id / spec.agent_id


def _check_source(code: str) -> None:
    """Reject code that cannot even be loaded. Whether it runs correctly is what /check is for."""
    try:
        compile(code, "agent.py", "exec")
        validate_python_source(code)
    except (SyntaxError, ValueError) as exc:
        line = f" (line {exc.lineno})" if isinstance(exc, SyntaxError) and exc.lineno else ""
        raise HTTPException(status_code=400, detail=f"{type(exc).__name__}: {getattr(exc, 'msg', exc)}{line}") from exc


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:40]


def _saved_file(spec: AgentSpec, impl: str) -> Path | None:
    """The file of a saved implementation, or None when `impl` is not a saved id."""
    slug = impl.removeprefix(SAVED_PREFIX)
    if not impl.startswith(SAVED_PREFIX) or slug != _slug(slug) or not slug:
        return None
    return _folder(spec) / "saved" / f"{slug}.py"


def _meta(spec: AgentSpec) -> list[dict[str, object]]:
    items: list[dict[str, object]] = [
        {"id": v, "label": label, "kind": "builtin", "edited": (_folder(spec) / f"{v}.py").is_file()}
        for v, (label, _) in VARIANTS.items()
    ]
    for saved in sorted((_folder(spec) / "saved").glob("*.py")):
        label = saved.stem.replace("-", " ").title()
        items.append({"id": SAVED_PREFIX + saved.stem, "label": label, "kind": "saved", "edited": False})
    return items


def resolve_code(role_id: str, agent_id: str, impl: str) -> str:
    """The code to run for an implementation: your saved edit, or the original. Used by Run."""
    return _view(_spec(role_id, agent_id), impl)["code"]  # type: ignore[return-value]


def _view(spec: AgentSpec, impl: str) -> dict[str, object]:
    saved = _saved_file(spec, impl)
    if impl in VARIANTS:
        original = render(spec, impl)
        edit = _folder(spec) / f"{impl}.py"
        edited = edit.is_file()
        return {"role_id": spec.role_id, "agent_id": spec.agent_id, "impl": impl, "label": VARIANTS[impl][0],
                "kind": "builtin", "original": original, "code": edit.read_text() if edited else original, "edited": edited}
    if saved is not None and saved.is_file():
        return {"role_id": spec.role_id, "agent_id": spec.agent_id, "impl": impl,
                "label": saved.stem.replace("-", " ").title(), "kind": "saved", "original": "", "code": saved.read_text(),
                "edited": False}
    raise HTTPException(status_code=404, detail=f"No implementation {impl} for {spec.agent_id}")


@router.get("/implementations")
def list_implementations(role_id: str, agent_id: str) -> dict[str, object]:
    return {"implementations": _meta(_spec(role_id, agent_id))}


@router.get("/implementations/{impl}")
def get_implementation(role_id: str, agent_id: str, impl: str) -> dict[str, object]:
    return _view(_spec(role_id, agent_id), impl)


@router.put("/implementations/{impl}")
def save_implementation(role_id: str, agent_id: str, impl: str, body: CodeBody) -> dict[str, object]:
    """Save an edit. Code equal to the original is not an edit, so any saved edit is dropped."""
    spec = _spec(role_id, agent_id)
    current = _view(spec, impl)
    _check_source(body.code)
    target = _saved_file(spec, impl) if current["kind"] == "saved" else _folder(spec) / f"{impl}.py"
    assert target is not None
    if current["kind"] == "builtin" and body.code == current["original"]:
        target.unlink(missing_ok=True)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body.code)
    tracing.step("editor.save", f"saved {impl} for {spec.agent_id}", agent=spec.agent_id, impl=impl, chars=len(body.code))
    return _view(spec, impl)


@router.delete("/implementations/{impl}")
def revert_or_delete_implementation(role_id: str, agent_id: str, impl: str) -> dict[str, object]:
    """Revert a built-in implementation to its original, or delete a saved one."""
    spec = _spec(role_id, agent_id)
    current = _view(spec, impl)
    if current["kind"] == "saved":
        _saved_file(spec, impl).unlink()  # type: ignore[union-attr]
        tracing.step("editor.delete", f"deleted saved version {impl} of {spec.agent_id}", agent=spec.agent_id, impl=impl)
        return {"deleted": impl}
    (_folder(spec) / f"{impl}.py").unlink(missing_ok=True)
    tracing.step("editor.revert", f"reverted {impl} of {spec.agent_id} to the original", agent=spec.agent_id, impl=impl)
    return _view(spec, impl)


@router.post("/implementations")
def save_new_implementation(role_id: str, agent_id: str, body: NewImplementation) -> dict[str, object]:
    """Save a new implementation next to the built-in ones. It never replaces an original."""
    spec = _spec(role_id, agent_id)
    slug = _slug(body.name)
    if not slug:
        raise HTTPException(status_code=400, detail="Give the implementation a name")
    _check_source(body.code)
    target = _folder(spec) / "saved" / f"{slug}.py"
    if target.exists():
        raise HTTPException(status_code=409, detail=f"An implementation named {body.name} already exists")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body.code)
    return _view(spec, SAVED_PREFIX + slug)


@router.post("/check")
def check_code(role_id: str, agent_id: str, body: CodeBody) -> dict[str, object]:
    """Load the code and run it once with the agent's own sample, so errors show up before a real run."""
    spec = _spec(role_id, agent_id)
    try:
        _check_source(body.code)
    except HTTPException as exc:
        return {"ok": False, "error": exc.detail, "line": None, "warnings": []}
    result = run_custom_python(body.code, {spec.input_key: spec.sample})
    tracing.step("editor.check", "checked the code with the sample input", "ok" if result.ok else "error", agent=spec.agent_id,
                 error=result.error, line=result.line, ms_taken=result.latency_ms)
    if not result.ok:
        return {"ok": False, "error": result.error, "line": result.line, "warnings": []}
    warnings = [] if spec.output_key in result.output else [f"The result has no \"{spec.output_key}\" key."]
    return {"ok": True, "error": None, "line": None, "warnings": warnings, "output": result.output}


@router.get("/fields")
def get_fields(role_id: str, agent_id: str) -> dict[str, object]:
    """The extra data this agent needs (key, label, kind, example), so the Run tab can show a box for each."""
    return {"fields": playbook_for(_spec(role_id, agent_id))["fields"]}


@router.get("/explanation")
def get_explanation(role_id: str, agent_id: str) -> dict[str, object]:
    return explanation(_spec(role_id, agent_id))
