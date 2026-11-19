"""Read the step-by-step trace: a list for catching up, and a live stream for the Command Centre's trace pane."""

from __future__ import annotations

import asyncio
from typing import Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from valkyrie import tracing
from valkyrie.storage import logs_dir

router = APIRouter(tags=["trace"])
STREAM_CHECK_S = 0.25
BATCH = 500


@router.get("/api/trace/events")
def list_events(after: int = 0, run: str | None = None) -> dict[str, Any]:
    """Events newer than `after` (an event id), optionally for one run. `last_id` is where to continue from."""
    events = tracing.STORE.since(after, run)[:BATCH]
    return {"events": events, "last_id": events[-1]["id"] if events else after, "log_file": str(logs_dir() / "trace.jsonl")}


@router.delete("/api/trace/events")
def clear_events() -> dict[str, int]:
    """Clear the pane's memory. The log file on disk is kept."""
    return {"cleared": tracing.STORE.clear()}


@router.websocket("/ws/trace")
async def stream_events(websocket: WebSocket, after: int = 0) -> None:
    """Send every event newer than `after` as it happens, until the client leaves."""
    await websocket.accept()
    last = after
    try:
        while True:
            fresh = tracing.STORE.since(last)[:BATCH]
            if fresh:
                last = fresh[-1]["id"]
                await websocket.send_json({"events": fresh})
            try:  # waiting for the client also notices when it disconnects
                await asyncio.wait_for(websocket.receive_text(), STREAM_CHECK_S)
            except asyncio.TimeoutError:
                continue
    except WebSocketDisconnect:
        return
