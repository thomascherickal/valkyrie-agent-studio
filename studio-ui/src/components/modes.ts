export type ExperienceMode = "beginner" | "intermediate" | "advanced";
export type TabId = "run" | "create" | "design" | "code";

export const TAB_LABELS: Record<TabId, string> = {
  run: "Run",
  create: "Create agent",
  design: "Design",
  code: "Python",
};

/** Each experience level reveals more of the studio. */
export const MODE_TABS: Record<ExperienceMode, TabId[]> = {
  beginner: ["run", "create"],
  intermediate: ["run", "create", "design"],
  advanced: ["run", "create", "design", "code"],
};
