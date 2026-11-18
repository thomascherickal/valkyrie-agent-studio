import React, { useState } from "react";
import { draftFor, type Draft } from "../components/studioState";

export const agent = {
  id: "a1", name: "Agent A", description: "d", tool: "t", inputKey: "feature_brief", outputKey: "o", sampleInput: "sample",
};

type Render = (draft: Draft, change: (p: Partial<Draft>) => void) => React.ReactNode;

/** Holds a real draft so panels are tested with their onChange wired back in. */
export function Held({ render, initial }: { render: Render; initial?: Partial<Draft> }) {
  const [draft, setDraft] = useState<Draft>({ ...draftFor(agent), ...initial });
  return <>{render(draft, (p) => setDraft((d) => ({ ...d, ...p })))}</>;
}
