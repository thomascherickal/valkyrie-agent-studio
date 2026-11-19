"""POST /api/agents/run: run an agent and trace every step (request, keys, definition, code, sandbox, providers, checks)."""

from __future__ import annotations

import time
from typing import Any, NoReturn

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from valkyrie import tracing
from valkyrie.agent_impl_routes import resolve_code
from valkyrie.env_file import load_env_file
from valkyrie.eval_gate import evaluate_agent_output
from valkyrie.fallback import AllProvidersFailed, invoke_with_fallback
from valkyrie.ir_schema import AgentIR, load_ir_from_yaml
from valkyrie.llm_router import LLMRouter
from valkyrie.model_helper import server_model
from valkyrie.python_runner import SandboxResult, run_custom_python

router = APIRouter(tags=["run"])


class RunRequest(BaseModel):
    """Payload to execute an agent in the sandbox console."""

    ir_yaml: str
    prompt: str
    custom_python: str | None = None
    payload: dict[str, Any] = {}
    # To run one of an agent's Python implementations, name it: its saved edit, or its original, is used.
    role_id: str | None = None
    agent_id: str | None = None
    impl: str | None = None
    # Source of that implementation as it is in the editor, saved or not. When given it is run instead.
    code: str | None = None


def _fail(status: int, detail: str, stage: str = "run.error") -> NoReturn:
    tracing.step(stage, detail, "error", http_status=status)
    raise HTTPException(status_code=status, detail=detail)


def _sandbox(code: str, payload: dict[str, Any], label: str) -> SandboxResult:
    """Run code in the sandbox and trace the start, the result and each stage the code reports."""
    tracing.step("sandbox.start", f"running {label} in the sandbox", code_chars=len(code), code_lines=code.count("\n") + 1,
                 payload_keys=sorted(payload))
    result = run_custom_python(code, payload, model=server_model)
    if not result.ok:
        tracing.step("sandbox.error", result.error or "the code failed", "error", line=result.line, ms_taken=result.latency_ms)
        return result
    out = result.output
    tracing.step("sandbox.end", "the code returned", "ok", ms_taken=result.latency_ms, output_keys=sorted(out))
    for stage in out.get("stages", []):
        tracing.step("stage", f"stage {stage.get('stage')}", **{k: v for k, v in stage.items() if k != "stage"})
    for key in ("implementation", "completeness", "missing", "metrics", "model_used", "review", "confidence"):
        if key in out:
            tracing.step("result", f"{key}", value=out[key])
    return result


def _run_python(req: RunRequest, label: str) -> dict[str, Any]:
    if req.impl:
        if not (req.role_id and req.agent_id):
            _fail(400, "Running an implementation needs role_id and agent_id")
        code = req.code if req.code is not None else resolve_code(req.role_id, req.agent_id, req.impl)
        tracing.step("code", "using the editor text (unsaved)" if req.code is not None else "using the saved or original code",
                     source="editor" if req.code is not None else "saved", impl=req.impl)
    else:
        code = req.custom_python or ""
    result = _sandbox(code, req.payload, label)
    if not result.ok:
        _fail(400, f"{req.impl}: {result.error}" if req.impl else (result.error or "Python execution failed"))
    body: dict[str, Any] = {"mode": "python", "output": result.output, "latency_ms": result.latency_ms, "cost_usd": 0.0}
    return {**body, "impl": req.impl} if req.impl else body


def _run_model(ir: AgentIR, req: RunRequest) -> dict[str, Any]:
    tracing.step("prompt", "prompt built", system_chars=len(ir.system_prompt), prompt_chars=len(req.prompt), system=ir.system_prompt, prompt=req.prompt)
    try:
        answer = invoke_with_fallback(LLMRouter(), ir.model_config_spec, ir.system_prompt, req.prompt)
    except AllProvidersFailed as exc:
        _fail(502, str(exc), "run.error")
    report = evaluate_agent_output(ir=ir, output={k: answer.content for k in ir.output_schema}, latency_ms=12.5, cost_usd=answer.cost_usd)
    tracing.step("eval", "evaluation gate " + ("passed" if report.passed else "failed"), "ok" if report.passed else "warn",
                 schema_valid=report.schema_valid, latency_ok=report.latency_ok, cost_ok=report.cost_ok,
                 guardrails_ok=report.guardrails_ok, reasons=report.reasons)
    return {
        "mode": "llm", "model": answer.model, "provider": answer.provider, "thinking_level": answer.thinking_level,
        "content": answer.content, "input_tokens": answer.input_tokens, "output_tokens": answer.output_tokens,
        "cost_usd": answer.cost_usd, "eval_passed": report.passed, "eval_reasons": report.reasons,
    }


@router.post("/api/agents/run")
def run_agent_endpoint(req: RunRequest) -> dict[str, Any]:
    """Run an agent via the provider chain or custom Python, then evaluate. Every step is traced."""
    started = time.perf_counter()
    with tracing.traced_run(req.agent_id or "model run") as run:
        mode = "implementation" if req.impl else "custom python" if req.custom_python else "model"
        tracing.step("run.start", f"run started ({mode})", mode=mode, role=req.role_id, agent=req.agent_id, impl=req.impl,
                     payload=req.payload, run_id=run.run)
        changed = load_env_file()  # keys you changed in .env are used without a restart
        tracing.step("env", ".env re-read", names_changed=changed)
        try:
            ir: AgentIR = load_ir_from_yaml(req.ir_yaml)
        except Exception as exc:  # noqa: BLE001
            _fail(400, str(exc), "ir.error")
        spec = ir.model_config_spec
        tracing.step("ir", f"agent definition {ir.name} is valid", "ok", name=ir.name, provider=spec.provider, model=spec.model,
                     thinking_level=spec.thinking_level, custom_python_enabled=ir.custom_python_enabled)
        if req.impl or (ir.custom_python_enabled and req.custom_python):
            body = _run_python(req, req.impl or "custom Python")
        else:
            body = _run_model(ir, req)
        tracing.step("run.done", "run finished", "ok", total_ms=round((time.perf_counter() - started) * 1000, 1), cost_usd=body["cost_usd"])
        return body
