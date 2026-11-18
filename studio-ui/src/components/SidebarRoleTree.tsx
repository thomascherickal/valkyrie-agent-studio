import React, { useState } from "react";

export interface RoleEntry {
  id: string;
  name: string;
  agents: { id: string; name: string }[];
}

interface SidebarRoleTreeProps {
  roles: RoleEntry[];
  selectedAgentId: string;
  onSelectAgent: (roleId: string, agentId: string) => void;
}

export function SidebarRoleTree({ roles, selectedAgentId, onSelectAgent }: SidebarRoleTreeProps) {
  const [query, setQuery] = useState("");
  const filtered = roles
    .map((role) => ({
      ...role,
      agents: role.agents.filter((a) => a.name.toLowerCase().includes(query.toLowerCase())),
    }))
    .filter((role) => role.agents.length > 0);

  return (
    <aside className="studio-sidebar" aria-label="Role and Agent Tree">
      <input
        type="search"
        placeholder="Search 120 agents..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <ul>
        {filtered.map((role) => (
          <li key={role.id}>
            <strong>{role.name}</strong>
            <ul>
              {role.agents.map((agent) => (
                <li key={agent.id}>
                  <button
                    type="button"
                    aria-pressed={selectedAgentId === agent.id}
                    onClick={() => onSelectAgent(role.id, agent.id)}
                  >
                    {agent.name}
                  </button>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </aside>
  );
}

