"""FastAPI router exposing Command Centre start, stop, traces, and admin endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from valkyrie.command_centre import CommandCentre

router = APIRouter(prefix="/api/command-centre", tags=["command-centre"])
_centre = CommandCentre()


@router.get("/traces")
def get_traces() -> dict[str, list[dict[str, object]]]:
    """List visual traces for all managed agents."""
    return {
        "traces": [
            {"agent_id": t.agent_id, "state": t.state, "steps": t.steps}
            for t in _centre.list_traces()
        ]
    }


@router.post("/start/{agent_id}")
def start_agent_route(agent_id: str) -> dict[str, object]:
    """Start an agent via Command Centre."""
    t = _centre.start_agent(agent_id)
    return {"agent_id": t.agent_id, "state": t.state, "steps": t.steps}


@router.post("/stop/{agent_id}")
def stop_agent_route(agent_id: str) -> dict[str, object]:
    """Stop an agent via Command Centre."""
    t = _centre.stop_agent(agent_id)
    return {"agent_id": t.agent_id, "state": t.state, "steps": t.steps}


@router.post("/admin/stop-all")
def admin_stop_all_route() -> dict[str, int]:
    """Admin action to stop all running agents."""
    return {"stopped": _centre.admin_stop_all()}

