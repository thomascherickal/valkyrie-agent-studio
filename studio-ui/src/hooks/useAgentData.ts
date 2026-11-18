import { useEffect, useRef } from "react";
import { getFields, listImpls } from "../api/client";
import { toField, type Draft, type Patch } from "../components/studioState";
import { useAsync } from "./useAsync";

/**
 * Loads an agent's implementations and its data fields into its draft, once. A reply that lands after you moved
 * to another agent is dropped, and loading twice (React strict mode) never adds the fields twice.
 */
export function useAgentData(roleId: string, agentId: string, draft: Draft, onChange: (patch: Patch) => void) {
  const impls = useAsync(listImpls);
  const fields = useAsync(getFields);
  const live = useRef(true);

  useEffect(() => {
    live.current = true;
    if (draft.impls === null) {
      impls.run(roleId, agentId).then((res) => {
        if (res && live.current) onChange({ impls: res.implementations });
      });
    }
    if (!draft.fieldsLoaded) {
      fields.run(roleId, agentId).then((res) => {
        if (res && live.current) {
          onChange((d) => (d.fieldsLoaded ? {} : { fieldsLoaded: true, fields: [d.fields[0], ...res.fields.map(toField), ...d.fields.slice(1)] }));
        }
      });
    }
    return () => {
      live.current = false;
    };
  }, [roleId, agentId]);
}
