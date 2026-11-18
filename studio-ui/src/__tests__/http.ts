export const ok = (data: unknown) => ({ ok: true, json: async () => data });
export const fail = (status = 500, detail?: string) => ({
  ok: false,
  status,
  json: detail === undefined ? async () => { throw new Error("no body"); } : async () => ({ detail }),
});
