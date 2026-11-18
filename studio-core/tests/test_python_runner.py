"""Tests for sandboxed Python execution."""

import json
from pathlib import Path

from valkyrie.python_runner import run_custom_python


def test_run_custom_python_success() -> None:
    code = """
def run_agent(payload):
    return {"doubled": payload["x"] * 2}
"""
    res = run_custom_python(code, {"x": 21})
    assert res.ok is True
    assert res.output == {"doubled": 42}
    assert res.error is None


def test_run_custom_python_forbidden_and_errors() -> None:
    bad_code = "import os\ndef run_agent(p): return {}"
    res = run_custom_python(bad_code, {})
    assert res.ok is False
    assert "Forbidden construct" in (res.error or "")

    missing_fn = "x = 1"
    res2 = run_custom_python(missing_fn, {})
    assert res2.ok is False
    assert "run_agent" in (res2.error or "")

    non_dict = "def run_agent(p): return [1, 2]"
    res3 = run_custom_python(non_dict, {})
    assert res3.ok is False
    assert "must return a dict" in (res3.error or "")


def test_sandbox_allows_typing_only() -> None:
    ok = run_custom_python("from typing import Any\nimport typing\ndef run_agent(p: dict[str, Any]):\n    return {'t': typing.Any is Any}", {})
    assert ok.ok and ok.output == {"t": True}

    for source in ("import json", "from json import dumps", "import typing.io", "from . import x"):
        res = run_custom_python(source + "\ndef run_agent(p): return {}", {})
        assert not res.ok and "not allowed in the sandbox" in (res.error or ""), source

    # The module's own imports must stay out of reach: typing.sys would lead to sys.modules and os.
    leak = run_custom_python("import typing\ndef run_agent(p): return {'m': str(typing.sys)}", {})
    assert not leak.ok and "sys" in (leak.error or "")


def test_every_original_agent_runs_in_the_sandbox_with_its_own_sample() -> None:
    root = Path(__file__).resolve().parents[2] / "agents"
    agents = sorted(root.glob("*/*/agent.py"))
    assert len(agents) == 120
    for agent_py in agents:
        sample = json.loads((agent_py.parent / "sample_data.json").read_text())
        res = run_custom_python(agent_py.read_text(), sample)
        assert res.ok, f"{agent_py.parent.name}: {res.error}"
        assert res.output["agent_id"] == agent_py.parent.name

