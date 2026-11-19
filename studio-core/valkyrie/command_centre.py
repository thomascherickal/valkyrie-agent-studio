"""Command Centre module to start, monitor, visualize, stop agents, and run admin tasks."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

AgentState = Literal["idle", "running", "stopped"]


@dataclass
class AgentTrace:
    """Visual trace record for an agent execution."""

    agent_id: str
    state: AgentState
    steps: list[str] = field(default_factory=list)


class CommandCentre:
    """Centralized lifecycle, monitoring, and admin controller for every agent."""

    def __init__(self) -> None:
        self._agents: dict[str, AgentTrace] = {}

    def start_agent(self, agent_id: str) -> AgentTrace:
        """Start an agent and record its initial trace."""
        trace = AgentTrace(agent_id=agent_id, state="running", steps=["initialized", "running"])
        self._agents[agent_id] = trace
        return trace

    def stop_agent(self, agent_id: str) -> AgentTrace:
        """Stop a running agent."""
        trace = self._agents.get(agent_id) or AgentTrace(agent_id=agent_id, state="stopped")
        trace.state = "stopped"
        trace.steps.append("stopped")
        self._agents[agent_id] = trace
        return trace

    def list_traces(self) -> list[AgentTrace]:
        """Return visual traces for all tracked agents."""
        return list(self._agents.values())

    def admin_stop_all(self) -> int:
        """Admin action: stop all running agents and return count stopped."""
        stopped = 0
        for trace in self._agents.values():
            if trace.state == "running":
                trace.state = "stopped"
                trace.steps.append("admin_stopped")
                stopped += 1
        return stopped

