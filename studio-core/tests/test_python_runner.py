"""Tests for sandboxed Python execution."""

import json
from pathlib import Path
import time
from types import SimpleNamespace
import typing

import pytest

from valkyrie.python_runner import (
    SandboxTimeout, _deadline_tracer, _public, _sandbox_import, run_custom_python,
)


def test_sandbox_helpers_directly() -> None:
    """Sandboxed code runs under the time-limit tracer, where coverage cannot see it, so check the helpers here."""
    public = _public(typing)
    assert public.Any is typing.Any and not hasattr(public, "sys") and not hasattr(public, "_cast")
    assert _sandbox_import("re").findall(r"\d", "a1") == ["1"]
    with pytest.raises(ImportError, match="only typing, re, json, math"):
        _sandbox_import("sys")
    with pytest.raises(ImportError):
        _sandbox_import("re", level=1)

    mine = SimpleNamespace(f_code=SimpleNamespace(co_filename="<valkyrie-sandbox>"))
    other = SimpleNamespace(f_code=SimpleNamespace(co_filename="httpx.py"))
    tracer = _deadline_tracer([time.perf_counter() + 60])
    assert tracer(mine, "call", None) is tracer and tracer(other, "call", None) is None
    with pytest.raises(SandboxTimeout):
        _deadline_tracer([0.0])(mine, "line", None)
    assert _deadline_tracer([0.0])(other, "call", None) is None  # not timed even when late


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


def run(source: str, payload: dict | None = None):
    return run_custom_python(source, payload or {})


def test_sandbox_allows_typing_re_json_and_math_only() -> None:
    ok = run("from typing import Any\nimport typing, re, json, math\n"
             "def run_agent(p: dict[str, Any]):\n"
             "    return {'t': typing.Any is Any, 're': re.findall(r'\\d+', 'a1b22'), 'j': json.dumps({'a': 1}), 'm': math.sqrt(16)}")
    assert ok.ok and ok.output == {"t": True, "re": ["1", "22"], "j": '{"a": 1}', "m": 4.0}

    for source in ("import sys", "import socket", "import importlib", "from pathlib import Path", "import typing.io", "from . import x"):
        res = run(source + "\ndef run_agent(p): return {}")
        assert not res.ok and "not allowed in the sandbox" in (res.error or ""), source

    # The modules' own imports must stay out of reach: typing.sys would lead to sys.modules and os.
    for leak in ("typing.sys", "re.enum", "json.decoder", "math.sys"):
        mod = leak.split(".")[0]
        res = run(f"import {mod}\ndef run_agent(p): return {{'m': str({leak})}}")
        assert not res.ok and "AttributeError" in (res.error or ""), leak


def test_sandbox_has_the_common_pure_helpers_and_classes() -> None:
    code = """
class Counter:
    def __init__(self):
        self.n = 0
    def bump(self):
        self.n += 1
        return self

def run_agent(p):
    try:
        1 / 0
    except ZeroDivisionError:
        caught = True
    c = Counter().bump().bump()
    return {'range': list(range(3)), 'abs': abs(-2), 'round': round(2.567, 1), 'any': any([0, 1]), 'all': all([1, 0]),
            'set': sorted(set([2, 1, 2])), 'is': isinstance(3, int), 'zip': list(zip([1], ['a'])), 'caught': caught, 'n': c.n}
"""
    res = run(code)
    assert res.ok, res.error
    assert res.output == {"range": [0, 1, 2], "abs": 2, "round": 2.6, "any": True, "all": False, "set": [1, 2],
                          "is": True, "zip": [(1, "a")], "caught": True, "n": 2}
    for name in ("getattr", "type", "vars", "globals", "compile", "input"):
        missing = run(f"def run_agent(p):\n    return {{'x': {name}}}")
        assert not missing.ok and "NameError" in (missing.error or ""), name


def test_errors_say_what_and_where() -> None:
    syntax = run("def run_agent(p):\n    return {'a': \n")
    assert not syntax.ok and syntax.line == 2 and syntax.error.startswith("SyntaxError") and "(line 2)" in syntax.error

    runtime = run("def helper(x):\n    return 1 / x\n\ndef run_agent(p):\n    return {'v': helper(0)}\n")
    assert not runtime.ok and runtime.line == 2
    assert runtime.error == "ZeroDivisionError: division by zero (line 2)"

    no_line = run("x = 1")  # fails in the runner, not in the user's code
    assert no_line.line is None and "run_agent" in (no_line.error or "") and "line" not in (no_line.error or "")


def test_runaway_code_is_stopped() -> None:
    forever = run_custom_python("def run_agent(p):\n    while True:\n        pass\n", {}, time_limit=0.2)
    assert not forever.ok and "time limit" in (forever.error or "") and forever.line in (2, 3)  # the loop header or its body
    hidden = run_custom_python(
        "def run_agent(p):\n    while True:\n        try:\n            pass\n        except Exception:\n            pass\n", {}, time_limit=0.2)
    assert not hidden.ok and "time limit" in (hidden.error or "")  # `except Exception` cannot swallow it
    assert run("def run_agent(p): return {}").ok  # the tracer was removed again


def test_every_original_agent_runs_in_the_sandbox_with_its_own_sample() -> None:
    root = Path(__file__).resolve().parents[2] / "agents"
    agents = sorted(root.glob("*/*/agent.py"))
    assert len(agents) == 240
    for agent_py in agents:
        sample = json.loads((agent_py.parent / "sample_data.json").read_text())
        res = run_custom_python(agent_py.read_text(), sample)
        assert res.ok, f"{agent_py.parent.name}: {res.error}"
        assert res.output["agent_id"] == agent_py.parent.name

