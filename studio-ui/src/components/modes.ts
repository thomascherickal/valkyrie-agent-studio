export type ExperienceMode = "beginner" | "advanced";
export type TabId = "run" | "about" | "create" | "design" | "code" | "providers";

export const TAB_LABELS: Record<TabId, string> = {
  run: "Run",
  about: "About this agent",
  create: "Create agent",
  design: "Design",
  code: "Python",
  providers: "Providers",
};

/** Each experience level reveals more of the studio. */
export const MODE_TABS: Record<ExperienceMode, TabId[]> = {
  beginner: ["run", "about", "create"],
  advanced: ["run", "about", "create", "design", "code", "providers"], // Design and Python are Advanced only
};
