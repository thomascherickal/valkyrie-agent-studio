"""FastAPI router exposing Command Centre start, stop, traces, and admin endpoints, and the live trace stream."""

from __future__ import annotations

import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from valkyrie import tracing
from valkyrie.command_centre import CommandCentre

router = APIRouter(prefix="/api/command-centre", tags=["command-centre"])
stream_router = APIRouter(tags=["command-centre"])
_centre = CommandCentre()
STREAM_CHECK_S = 0.25


def _snapshot() -> list[dict[str, object]]:
    return [{"agent_id": t.agent_id, "state": t.state, "steps": list(t.steps)} for t in _centre.list_traces()]


@router.get("/traces")
def get_traces() -> dict[str, list[dict[str, object]]]:
    """List visual traces for all managed agents."""
    return {"traces": _snapshot()}


@router.post("/start/{agent_id}")
def start_agent_route(agent_id: str) -> dict[str, object]:
    """Start an agent via Command Centre."""
    t = _centre.start_agent(agent_id)
    tracing.step("command-centre.start", f"started {agent_id}", agent_id=agent_id, steps=t.steps)
    return {"agent_id": t.agent_id, "state": t.state, "steps": t.steps}


@router.post("/stop/{agent_id}")
def stop_agent_route(agent_id: str) -> dict[str, object]:
    """Stop an agent via Command Centre."""
    t = _centre.stop_agent(agent_id)
    tracing.step("command-centre.stop", f"stopped {agent_id}", agent_id=agent_id, steps=t.steps)
    return {"agent_id": t.agent_id, "state": t.state, "steps": t.steps}


@router.post("/admin/stop-all")
def admin_stop_all_route() -> dict[str, int]:
    """Admin action to stop all running agents."""
    stopped = _centre.admin_stop_all()
    tracing.step("command-centre.stop-all", f"stopped {stopped} running agent(s)", stopped=stopped)
    return {"stopped": stopped}


@stream_router.websocket("/ws/traces")
async def stream_traces(websocket: WebSocket) -> None:
    """Send the traces now and again every time they change, until the client leaves."""
    await websocket.accept()
    last: list[dict[str, object]] | None = None
    try:
        while True:
            current = _snapshot()
            if current != last:
                await websocket.send_json({"traces": current})
                last = current
            try:  # waiting for the client also notices when it disconnects
                await asyncio.wait_for(websocket.receive_text(), STREAM_CHECK_S)
            except asyncio.TimeoutError:
                continue
    except WebSocketDisconnect:
        return
