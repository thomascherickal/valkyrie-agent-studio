"""Verify an agent before it is deployed or saved: every Python version must load, run and stay up on awkward input.

Each version is compiled, checked for blocked constructs, then run in the sandbox on several payloads: the sample,
no data, blank fields, very long text, unicode and symbols, and text where numbers belong. An error on any of them
is a problem that blocks. A data field that has no example is only a warning.
"""

from __future__ import annotations

import json
from typing import Any

from valkyrie.agent_impl_routes import code_of, implementation_labels
from valkyrie.agent_impls import AgentSpec, load_spec, playbook_for
from valkyrie.python_runner import run_custom_python, validate_python_source

LIMIT_S = 3.0
MAX_PROBLEMS = 5
LONG_TEXT = "word " * 4000
ODD_TEXT = "Ünïcödé ✓ 日本語 {braces} %s <b>\n\t"
SAMPLE = "the sample data"


def payload_sets(spec: AgentSpec, fields: list[dict[str, str]]) -> list[tuple[str, dict[str, str]]]:
    """The inputs every version is run with. The first is the agent's own sample."""
    keys = [spec.input_key, *(f["key"] for f in fields)]
    sample = {spec.input_key: spec.sample, **{f["key"]: f["example"] for f in fields}}
    sets = [(SAMPLE, sample), ("no data", {}), ("blank fields", {k: "" for k in keys}),
            ("very long text", {**sample, spec.input_key: LONG_TEXT}), ("unicode and symbols", {**sample, spec.input_key: ODD_TEXT})]
    numbers = [f["key"] for f in fields if f["kind"] == "number"]
    if numbers:
        sets.append(("text where numbers belong", {**sample, **{k: "not a number" for k in numbers}}))
    return sets


def result_problem(output: dict[str, Any], output_key: str) -> str:
    """What is wrong with a returned result, or an empty string."""
    if not str(output.get(output_key, "")).strip():
        return f'The result has no "{output_key}" text'
    try:
        json.dumps(output)
    except (TypeError, ValueError):
        return "The result cannot be sent as JSON"
    return ""


def check_version(code: str, spec: AgentSpec, sets: list[tuple[str, dict[str, str]]]) -> tuple[list[dict[str, Any]], list[str]]:
    """(problems, warnings) for one version's code."""
    try:
        compile(code, "agent.py", "exec")
    except SyntaxError as exc:
        return [{"stage": "syntax", "payload": None, "message": f"SyntaxError: {exc.msg}", "line": exc.lineno}], []
    try:
        validate_python_source(code)
    except ValueError as exc:
        return [{"stage": "blocked", "payload": None, "message": str(exc), "line": None}], []
    problems: list[dict[str, Any]] = []
    warnings: list[str] = []
    for label, payload in sets:
        outcome = run_custom_python(code, payload, time_limit=LIMIT_S)
        if not outcome.ok:
            problems.append({"stage": "run", "payload": label, "message": outcome.error, "line": outcome.line})
        elif (problem := result_problem(outcome.output, spec.output_key)):
            problems.append({"stage": "result", "payload": label, "message": problem, "line": None})
        elif label == SAMPLE and outcome.output.get("missing"):
            warnings.append("No example data for: " + ", ".join(outcome.output["missing"]))
    return problems[:MAX_PROBLEMS], warnings


def verify_agent(role_id: str, agent_id: str) -> dict[str, Any]:
    """Check every Python version of the agent. Raises ValueError or LookupError like load_spec for a bad id."""
    spec = load_spec(role_id, agent_id)
    sets = payload_sets(spec, playbook_for(spec)["fields"])
    checks = []
    for impl, label in implementation_labels(spec):
        problems, warnings = check_version(code_of(spec, impl), spec, sets)
        checks.append({"impl": impl, "label": label, "ok": not problems, "runs": len(sets), "problems": problems, "warnings": warnings})
    return {"agent": spec.name, "ok": all(c["ok"] for c in checks), "checks": checks,
            "problem_count": sum(len(c["problems"]) for c in checks), "warning_count": sum(len(c["warnings"]) for c in checks)}
