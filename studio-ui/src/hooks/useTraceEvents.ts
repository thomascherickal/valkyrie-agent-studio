import { useCallback, useEffect, useRef, useState } from "react";
import { clearTraceEvents, listTraceEvents } from "../api/client";
import { WS_URL } from "../api/config";
import type { TraceEvent } from "../api/types";

export const MAX_EVENTS = 1000;
export const POLL_MS = 2000;

/**
 * Every recorded step, live. It loads what the API already has, then follows the WebSocket from the last id.
 * If the socket is not available it polls the REST list instead, so the pane keeps filling either way.
 */
export function useTraceEvents(online: boolean) {
  const [events, setEvents] = useState<TraceEvent[]>([]);
  const [live, setLive] = useState(false);
  const [logFile, setLogFile] = useState("");
  const last = useRef(0);

  const add = useCallback((fresh: TraceEvent[]) => {
    if (fresh.length === 0) return;
    last.current = fresh[fresh.length - 1].id;
    setEvents((prev) => [...prev, ...fresh].slice(-MAX_EVENTS));
  }, []);

  useEffect(() => {
    if (!online) return;
    let stopped = false;
    let socket: WebSocket | null = null;
    let timer: ReturnType<typeof setTimeout> | undefined;

    const poll = async () => {
      const res = await listTraceEvents(last.current).catch(() => null);
      if (stopped) return;
      if (res) add(res.events);
      timer = setTimeout(poll, POLL_MS);
    };

    (async () => {
      const first = await listTraceEvents(0).catch(() => null);
      if (stopped) return;
      if (first) {
        setLogFile(first.log_file);
        add(first.events);
      }
      socket = new WebSocket(`${WS_URL}/ws/trace?after=${last.current}`);
      socket.onopen = () => setLive(true);
      socket.onmessage = (e) => add(JSON.parse(e.data).events);
      socket.onclose = socket.onerror = () => {
        if (socket) socket.onclose = socket.onerror = null;
        setLive(false);
        poll();
      };
    })();

    return () => {
      stopped = true;
      clearTimeout(timer);
      if (socket) {
        socket.onclose = socket.onerror = null;
        socket.close();
      }
    };
  }, [online, add]);

  const clear = useCallback(async () => {
    await clearTraceEvents();
    setEvents([]);
  }, []);

  return { events, live, logFile, clear };
}
