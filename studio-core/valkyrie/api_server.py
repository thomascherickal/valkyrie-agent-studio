"""FastAPI server powering the Valkyrie AI Agent Studio GUI."""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from valkyrie.agent_generator_routes import router as agent_generator_router
from valkyrie.agent_impl_routes import router as agent_impl_router
from valkyrie.command_centre_routes import router as command_centre_router, stream_router
from valkyrie.env_file import load_env_file
from valkyrie.ir_schema import load_ir_from_yaml
from valkyrie.provider_routes import router as provider_router
from valkyrie.run_routes import router as run_router
from valkyrie.secrets_routes import router as secrets_router
from valkyrie.storage import agents_dir
from valkyrie.trace_routes import router as trace_router
from valkyrie.rust_transpiler import transpile_ir_to_rust


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None]:
    """Load keys from the repo's .env file when the server starts (real environment variables win)."""
    load_env_file()
    yield


app = FastAPI(title="Valkyrie AI Agent Studio API", version="0.1.0", lifespan=lifespan)
# Origins of the Vite dev server and the Tauri webview (Linux/macOS and Windows).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "tauri://localhost", "http://tauri.localhost"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(command_centre_router)
app.include_router(stream_router)
app.include_router(provider_router)
app.include_router(secrets_router)
app.include_router(run_router)
app.include_router(trace_router)
app.include_router(agent_generator_router)
app.include_router(agent_impl_router)


class DeployRequest(BaseModel):
    """Payload to transpile an agent into a standalone Rust crate."""

    ir_yaml: str


@app.get("/health")
def health() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "ok", "default_model": "gemini-4-hydrogen", "thinking_level": "low"}


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
    """List every role and agent found in the agents/ directory."""
    agents_root = agents_dir()
    roles: list[dict[str, Any]] = []
    for role_dir in sorted(p for p in agents_root.iterdir() if p.is_dir()):
        agents = [{"id": a.name, "name": a.name} for a in sorted(role_dir.iterdir()) if a.is_dir()]
        roles.append({"id": role_dir.name, "name": role_dir.name, "agents": agents})
    return {"roles": roles}
