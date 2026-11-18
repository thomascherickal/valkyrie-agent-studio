export interface AgentBlueprint {
  id: string;
  name: string;
  description: string;
  tool: string;
  inputKey: string;
  outputKey: string;
  sampleInput: string;
}

export interface RoleCatalog {
  id: string;
  name: string;
  agents: AgentBlueprint[];
}
