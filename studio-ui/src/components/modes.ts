export type ExperienceMode = "beginner" | "intermediate" | "advanced";
export type TabId = "run" | "about" | "create" | "design" | "code";

export const TAB_LABELS: Record<TabId, string> = {
  run: "Run",
  about: "About this agent",
  create: "Create agent",
  design: "Design",
  code: "Python",
};

/** Each experience level reveals more of the studio. */
// ponytail: advanced currently shows the same tabs as intermediate. Give it its own extras when there are some.
export const MODE_TABS: Record<ExperienceMode, TabId[]> = {
  beginner: ["run", "about", "create"],
  intermediate: ["run", "about", "create", "design", "code"],
  advanced: ["run", "about", "create", "design", "code"],
};
