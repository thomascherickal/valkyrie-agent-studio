"""Tests for sandboxed Python execution."""

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

