"""Entry point of the packaged API (`valkyrie-api`). It serves the same app as `uvicorn valkyrie.api_server:app`."""

from __future__ import annotations

import os

import uvicorn

from valkyrie.api_server import app

HOST = "127.0.0.1"


def main() -> None:
    """Serve on 127.0.0.1 only. The port is 8000, or VALKYRIE_PORT."""
    uvicorn.run(app, host=HOST, port=int(os.environ.get("VALKYRIE_PORT", "8000")), log_level="info")


if __name__ == "__main__":
    main()
