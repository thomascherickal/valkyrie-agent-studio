export type TabId = "run" | "about" | "create" | "design" | "code" | "secrets";

export const TAB_LABELS: Record<TabId, string> = {
  run: "Run",
  about: "About this agent",
  create: "Create agent",
  design: "Design",
  code: "Python",
  secrets: "Secrets",
};

/** All studio tabs are always available. */
export const ALL_TABS: TabId[] = ["run", "about", "create", "design", "code", "secrets"];
