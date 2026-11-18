import React, { useState } from "react";
import { render } from "@testing-library/react";
import { vi } from "vitest";
import { CodePanel } from "../components/CodePanel";
import { RunPanel } from "../components/RunPanel";
import type { Report } from "../hooks/useReported";
import { draftFor, type Draft, type Patch } from "../components/studioState";
import { appRoutes, stubFetch } from "./helpers";

export const agent = {
  id: "a1", name: "Agent A", description: "d", tool: "t", inputKey: "feature_brief", outputKey: "o", sampleInput: "sample",
};

type Render = (draft: Draft, change: (p: Patch) => void) => React.ReactNode;

/** Holds a real draft so panels are tested with their onChange wired back in. */
export function Held({ render: body, initial }: { render: Render; initial?: Partial<Draft> }) {
  const [draft, setDraft] = useState<Draft>({ ...draftFor(agent), ...initial });
  return <>{body(draft, (p) => setDraft((d) => ({ ...d, ...(typeof p === "function" ? p(d) : p) })))}</>;
}

type Routes = (path: string, init?: RequestInit) => unknown;

/** Mounts a panel against the fake API. `state` shows the bits of the draft a test asserts on. */
function mount(panel: (d: Draft, c: (p: Patch) => void, report: Report) => React.ReactNode, initial?: Partial<Draft>, routes: Routes = appRoutes) {
  const f = stubFetch(routes);
  const report = vi.fn();
  const view = render(
    <>
      <Held
        initial={initial}
        render={(d, c) => (
          <>
            {panel(d, c, report)}
            <span data-testid="state">{`${d.editing}|${d.runWith}`}</span>
          </>
        )}
      />
    </>,
  );
  return { f, report, ...view };
}

export const mountRun = (initial?: Partial<Draft>, routes?: Routes) =>
  mount((d, c, report) => <RunPanel agent={agent} roleId="r1" ir="IR" draft={d} onChange={c} report={report} />, initial, routes);

export const mountCode = (initial?: Partial<Draft>, routes?: Routes) =>
  mount((d, c, report) => <CodePanel roleId="r1" agentId="a1" agentName="Agent A" draft={d} onChange={c} report={report} />, initial, routes);

/** The status line next to the editor's buttons. */
export const status = () => document.querySelector(".hint[role=status]")!.textContent;

export const calls =(f: ReturnType<typeof stubFetch>, method: string, suffix: string) =>
  f.mock.calls.filter(([url, init]) => (init?.method ?? "GET") === method && String(url).endsWith(suffix));
