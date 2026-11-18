"""FastAPI server powering the Valkyrie AI Agent Studio GUI."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from fastapi import FastAPI, HTTPException, WebSocket
from pydantic import BaseModel

from valkyrie.command_centre import CommandCentre
from valkyrie.command_centre_routes import router as command_centre_router

from valkyrie.eval_gate import evaluate_agent_output
from valkyrie.ir_schema import AgentIR, load_ir_from_yaml
from valkyrie.llm_router import LLMRouter
from valkyrie.python_runner import run_custom_python
from valkyrie.rust_transpiler import transpile_ir_to_rust

app = FastAPI(title="Valkyrie AI Agent Studio API", version="0.1.0")
app.include_router(command_centre_router)


class RunRequest(BaseModel):
    """Payload to execute an agent in the sandbox console."""

    ir_yaml: str
    prompt: str
    custom_python: str | None = None
    payload: dict[str, Any] = {}


class DeployRequest(BaseModel):
    """Payload to transpile an agent into a standalone Rust crate."""

    ir_yaml: str


@app.get("/health")
def health() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "ok", "default_model": "gemini-4-hydrogen", "thinking_level": "low"}


@app.post("/api/agents/run")
def run_agent_endpoint(req: RunRequest) -> dict[str, Any]:
    """Run an agent via Gemini 4 Hydrogen (Low) or custom Python, then evaluate."""
    try:
        ir: AgentIR = load_ir_from_yaml(req.ir_yaml)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    if ir.custom_python_enabled and req.custom_python:
        py_res = run_custom_python(req.custom_python, req.payload)
        if not py_res.ok:
            raise HTTPException(status_code=400, detail=py_res.error or "Python execution failed")
        return {
            "mode": "python",
            "output": py_res.output,
            "latency_ms": py_res.latency_ms,
            "cost_usd": 0.0,
        }

    router = LLMRouter()
    llm_res = router.invoke(ir.model_config_spec, ir.system_prompt, req.prompt)
    eval_report = evaluate_agent_output(
        ir=ir,
        output={k: llm_res.content for k in ir.output_schema},
        latency_ms=12.5,
        cost_usd=llm_res.cost_usd,
    )
    return {
        "mode": "llm",
        "model": llm_res.model,
        "thinking_level": llm_res.thinking_level,
        "content": llm_res.content,
        "input_tokens": llm_res.input_tokens,
        "output_tokens": llm_res.output_tokens,
        "cost_usd": llm_res.cost_usd,
        "eval_passed": eval_report.passed,
        "eval_reasons": eval_report.reasons,
    }


@app.post("/api/agents/deploy-rust")
def deploy_rust_endpoint(req: DeployRequest) -> dict[str, str]:
    """One-click Deploy: transpile AgentIR into a standalone Rust crate."""
    try:
        ir = load_ir_from_yaml(req.ir_yaml)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    bundle = transpile_ir_to_rust(ir)
    return {
        "crate_name": bundle.crate_name,
        "cargo_toml": bundle.cargo_toml,
        "main_rs": bundle.main_rs,
        "estimated_speedup": bundle.estimated_speedup,
    }


@app.get("/api/agents")
def list_agents_catalog() -> dict[str, Any]:
    """List all 12 roles and 120 agents from the agents/ directory."""
    agents_root = Path(__file__).resolve().parents[2] / "agents"
    roles: list[dict[str, Any]] = []
    for role_dir in sorted(p for p in agents_root.iterdir() if p.is_dir()):
        agents = [{"id": a.name, "name": a.name} for a in sorted(role_dir.iterdir()) if a.is_dir()]
        roles.append({"id": role_dir.name, "name": role_dir.name, "agents": agents})
    return {"roles": roles}


@app.websocket("/ws/traces")
async def stream_traces(websocket: WebSocket) -> None:
    """Stream CommandCentre agent traces over WebSocket."""
    await websocket.accept()
    cc = CommandCentre()
    trace = cc.start_agent("01-prd-architect")
    await websocket.send_json({"agent_id": trace.agent_id, "state": trace.state, "steps": trace.steps})
    await websocket.close()

