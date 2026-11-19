import { useEffect, useState } from "react";
import { WS_URL } from "../api/config";
import type { Trace } from "../api/types";

/**
 * Live traces from the API's WebSocket: the list now and again on every change.
 * Returns null while there is no connection, so the caller shows the list it fetched over REST instead.
 */
export function useTraceStream(online: boolean): Trace[] | null {
  const [traces, setTraces] = useState<Trace[] | null>(null);
  useEffect(() => {
    if (!online) return;
    const socket = new WebSocket(`${WS_URL}/ws/traces`);
    socket.onmessage = (e) => setTraces(JSON.parse(e.data).traces);
    socket.onclose = socket.onerror = () => setTraces(null);
    return () => {
      socket.onclose = socket.onerror = null;
      socket.close();
    };
  }, [online]);
  return traces;
}
