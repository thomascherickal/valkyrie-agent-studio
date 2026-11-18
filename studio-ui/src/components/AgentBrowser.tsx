import React, { useState } from "react";
import type { RoleCatalog } from "../data/types";

interface AgentBrowserProps {
  roles: RoleCatalog[];
  selectedAgentId: string;
  onSelect: (roleId: string, agentId: string) => void;
}

export function AgentBrowser({ roles, selectedAgentId, onSelect }: AgentBrowserProps) {
  const [query, setQuery] = useState("");
  const needle = query.trim().toLowerCase();
  const visible = roles
    .map((role) => ({ ...role, agents: role.agents.filter((a) => a.name.toLowerCase().includes(needle)) }))
    .filter((role) => role.agents.length > 0);

  return (
    <nav className="browser" aria-label="Agents">
      <input
        type="search"
        aria-label="Search agents"
        placeholder="Search agents"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {visible.length === 0 && <p className="empty">No agent matches “{query}”.</p>}
      {visible.map((role) => (
        <details key={role.id} open={needle !== "" || role.agents.some((a) => a.id === selectedAgentId)}>
          <summary>
            {role.name} <span className="count">{role.agents.length}</span>
          </summary>
          <ul>
            {role.agents.map((agent) => (
              <li key={agent.id}>
                <button
                  type="button"
                  aria-current={agent.id === selectedAgentId}
                  onClick={() => onSelect(role.id, agent.id)}
                >
                  {agent.name}
                </button>
              </li>
            ))}
          </ul>
        </details>
      ))}
    </nav>
  );
}
