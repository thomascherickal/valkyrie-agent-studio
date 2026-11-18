"""Standalone Command Centre fleet controller for all 120 agents."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AgentSnapshot:
    """Live runtime snapshot and trace timeline for a managed agent."""

    agent_id: str
    status: str = "idle"
    traces: list[str] = field(default_factory=list)


class FleetController:
    """Manages agent lifecycle, trace visualization, and admin commands."""

    def __init__(self) -> None:
        self._fleet: dict[str, AgentSnapshot] = {}

    def start(self, agent_id: str, engine: str = "gemini-4-hydrogen:low") -> AgentSnapshot:
        """Start an agent and append its startup trace."""
        snap = AgentSnapshot(agent_id=agent_id, status="running", traces=["boot", engine, "active"])
        self._fleet[agent_id] = snap
        return snap

    def record_step(self, agent_id: str, step: str) -> AgentSnapshot:
        """Append a visual trace step for a running agent."""
        snap = self._fleet.get(agent_id)
        if snap is None:
            raise KeyError(f"Agent not started: {agent_id}")
        snap.traces.append(step)
        return snap

    def stop(self, agent_id: str) -> AgentSnapshot:
        """Stop an individual agent cleanly."""
        snap = self._fleet.get(agent_id) or AgentSnapshot(agent_id=agent_id)
        snap.status = "stopped"
        snap.traces.append("stopped")
        self._fleet[agent_id] = snap
        return snap

    def admin_stop_all(self) -> int:
        """Admin command: halt every running agent in the fleet."""
        halted = 0
        for snap in self._fleet.values():
            if snap.status == "running":
                snap.status = "stopped"
                snap.traces.append("admin_halt")
                halted += 1
        return halted

    def summary(self) -> dict[str, int]:
        """Return fleet-wide counts for monitoring dashboards."""
        running = sum(1 for s in self._fleet.values() if s.status == "running")
        stopped = sum(1 for s in self._fleet.values() if s.status == "stopped")
        return {"total": len(self._fleet), "running": running, "stopped": stopped}

