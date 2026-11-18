import { fail, ok } from "./http";

/** A stateful stand-in for the implementation endpoints. Reset by every stubFetch. */
const edits = new Map<string, string>();
const saved = new Map<string, { label: string; code: string }>();
export const resetApi = () => { edits.clear(); saved.clear(); };

const BUILTINS = [["rules", "Rules"], ["pipeline", "Pipeline"], ["hybrid", "Hybrid"]];
export const originalOf = (roleId: string, agentId: string, id = "rules") => `# original ${id} ${roleId}/${agentId}`;
export const FIELDS = [
  { key: "audience", label: "Audience", kind: "text", example: "engineers" },
  { key: "budget", label: "Budget", kind: "number", example: "100" },
];
export const EXPLANATION = {
  title: "About",
  words: 9,
  sections: [
    { heading: "What it does", bullets: ["Writes PRDs", "Lists risks"] },
    { heading: "Data it needs", bullets: ["Audience"] },
  ],
};

const slug = (name: string) => `saved-${name.toLowerCase().replace(/\W+/g, "-")}`;

/** Adds a saved implementation straight into the fake API. Returns its id. */
export function seedSaved(roleId: string, agentId: string, name: string, code: string) {
  saved.set(`${roleId}/${agentId}/${slug(name)}`, { label: name, code });
  return slug(name);
}

function info(r: string, a: string, id: string) {
  const key = `${r}/${a}/${id}`;
  const base = { role_id: r, agent_id: a, impl: id };
  const s = saved.get(key);
  if (s) return { ...base, label: s.label, kind: "saved", edited: false, original: "", code: s.code };
  const b = BUILTINS.find(([i]) => i === id);
  if (!b) return undefined;
  const original = originalOf(r, a, id);
  return { ...base, label: b[1], kind: "builtin", edited: edits.has(key), original, code: edits.get(key) ?? original };
}

const metas = (r: string, a: string) =>
  [...BUILTINS.map(([id]) => id), ...[...saved.keys()].filter((k) => k.startsWith(`${r}/${a}/`)).map((k) => k.split("/")[2])]
    .map((id) => info(r, a, id)!)
    .map(({ impl, label, kind, edited }) => ({ id: impl, label, kind, edited }));

export function implRoute(path: string, init?: RequestInit) {
  const m = path.match(/^\/api\/agents\/([^/]+)\/([^/]+)\/(implementations|check|fields|explanation)(?:\/([^/]+))?$/);
  if (!m) return undefined;
  const [, r, a, part, id] = m;
  const method = init?.method ?? "GET";
  const body = init?.body ? JSON.parse(init.body as string) : {};
  if (part === "fields") return ok({ fields: FIELDS });
  if (part === "explanation") return ok(EXPLANATION);
  if (part === "check") {
    const bad = String(body.code).includes("BOOM");
    return ok({ ok: !bad, error: bad ? "BOOM happened" : null, line: bad ? 3 : null, warnings: [] });
  }
  if (!id) {
    if (method === "GET") return ok({ implementations: metas(r, a) });
    if (info(r, a, slug(body.name))) return fail(409, "That name is already used");
    return ok(info(r, a, seedSaved(r, a, body.name, body.code)));
  }
  const key = `${r}/${a}/${id}`;
  const cur = info(r, a, id);
  if (!cur) return fail(404, "No such implementation");
  if (method === "PUT") {
    if (body.code === "FAIL") return fail(400, "Code is not allowed");
    if (cur.kind === "saved") saved.set(key, { label: cur.label, code: body.code });
    else if (body.code === cur.original) edits.delete(key);
    else edits.set(key, body.code);
  } else if (method === "DELETE") {
    if (saved.delete(key)) return ok({ deleted: id });
    edits.delete(key);
  }
  return ok(info(r, a, id));
}

/** Echoes which implementation ran. A payload value of "BOOM" answers 400. */
export function runRoute(path: string, init?: RequestInit) {
  if (path !== "/api/agents/run") return undefined;
  const body = JSON.parse(init!.body as string);
  if (Object.values(body.payload).includes("BOOM")) return fail(400, "Run blew up");
  if (!body.impl) return undefined;
  const { role_id, agent_id, impl } = body;
  return ok({ mode: "python", impl, output: { role_id, agent_id, impl }, latency_ms: 3, cost_usd: 0 });
}
