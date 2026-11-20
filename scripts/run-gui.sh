#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$(readlink -f "$0")")/.." && pwd)"
API_PID=""

cleanup() {
  if [[ -n "$API_PID" ]] && kill -0 "$API_PID" 2>/dev/null; then
    kill "$API_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM

if ! (echo > /dev/tcp/127.0.0.1/8000) 2>/dev/null; then
  (cd "$ROOT_DIR/studio-core" && .venv/bin/uvicorn valkyrie.api_server:app --port 8000) &
  API_PID=$!
fi

BIN="$ROOT_DIR/target/debug/valkyrie-studio-tauri"
if [[ -x "$BIN" ]]; then
  "$BIN"
else
  cd "$ROOT_DIR/studio-ui" && npm run desktop:start
fi

