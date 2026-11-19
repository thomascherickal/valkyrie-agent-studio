import { useCallback, useEffect, useState } from "react";
import { getHealth } from "../api/client";
import { useAsync } from "./useAsync";

export const HEALTH_RETRY_MS = 1500;
export const HEALTH_MAX_DELAY_MS = 15000;
export const HEALTH_MAX_TRIES = 12;

/** Wait before retry number `tries` (0 is the first): 1.5 s, 3 s, 6 s, 12 s, then 15 s at most. */
export const retryDelay = (tries: number) => Math.min(HEALTH_RETRY_MS * 2 ** tries, HEALTH_MAX_DELAY_MS);

/**
 * Checks the API right away and retries with a growing wait (the desktop app starts it and it needs a moment).
 * After HEALTH_MAX_TRIES failed retries it stops and reports `gaveUp`; `retry` starts over.
 */
export function useHealth() {
  const health = useAsync(getHealth);
  const [failures, setFailures] = useState(0);
  const online = health.state.kind === "done";
  const gaveUp = failures > HEALTH_MAX_TRIES;
  const { run } = health;

  useEffect(() => {
    if (online || gaveUp) return;
    const check = () => run().then((res) => res || setFailures((n) => n + 1));
    const timer = setTimeout(check, failures === 0 ? 0 : retryDelay(failures - 1));
    return () => clearTimeout(timer);
  }, [online, gaveUp, failures, run]);

  const retry = useCallback(() => setFailures(0), []);
  return { state: health.state, gaveUp, retry };
}
