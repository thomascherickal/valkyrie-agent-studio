"""Tests for verifying an agent's Python versions before deploy."""

import pytest

from valkyrie import verify
from valkyrie.agent_impls import load_spec, playbook_for, render
from valkyrie.storage import edits_dir
from valkyrie.verify import SAMPLE, check_version, payload_sets, result_problem, verify_agent

ROLE, AGENT = "01-product-management", "02-roadmap-prioritizer"


def spec_and_sets():
    spec = load_spec(ROLE, AGENT)
    return spec, payload_sets(spec, playbook_for(spec)["fields"])


def save_edit(impl: str, code: str) -> None:
    folder = edits_dir() / ROLE / AGENT
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{impl}.py").write_text(code)


def test_the_inputs_include_awkward_ones_and_number_fields_get_text() -> None:
    spec, sets = spec_and_sets()
    names = [label for label, _ in sets]
    assert names == [SAMPLE, "no data", "blank fields", "very long text", "unicode and symbols", "text where numbers belong"]
    by_name = dict(sets)
    assert by_name["no data"] == {} and by_name["blank fields"][spec.input_key] == ""
    assert len(by_name["very long text"][spec.input_key]) > 10000 and by_name["text where numbers belong"]["reach"] == "not a number"
    plain = payload_sets(spec, [{"key": "note", "kind": "text", "example": "x"}])  # no number fields: no such input
    assert "text where numbers belong" not in [label for label, _ in plain]


def test_a_built_in_agent_passes_every_version_on_every_input() -> None:
    result = verify_agent(ROLE, AGENT)
    assert result["ok"] is True and result["agent"] == "Roadmap Prioritizer" and result["problem_count"] == 0 and result["warning_count"] == 0
    assert [(c["impl"], c["ok"], c["runs"]) for c in result["checks"]] == [("rules", True, 6), ("pipeline", True, 6), ("hybrid", True, 6)]


def test_a_saved_edit_is_what_gets_checked_and_a_syntax_error_names_its_line() -> None:
    save_edit("rules", "def run_agent(p):\n    return {'a': \n")
    result = verify_agent(ROLE, AGENT)
    bad = result["checks"][0]
    assert result["ok"] is False and bad["ok"] is False and bad["problems"][0]["stage"] == "syntax" and bad["problems"][0]["line"] == 2
    assert result["checks"][1]["ok"] is True and result["problem_count"] == 1


def test_blocked_code_a_crash_on_awkward_input_and_a_missing_result_are_all_found() -> None:
    spec, sets = spec_and_sets()
    problems, _ = check_version("def run_agent(p):\n    return open('x')\n", spec, sets)
    assert [(p["stage"], p["payload"]) for p in problems] == [("blocked", None)] and "open(" in problems[0]["message"]
    crashes_without_data = f"def run_agent(p):\n    return {{'{spec.output_key}': p['{spec.input_key}'].upper()}}\n"
    problems, _ = check_version(crashes_without_data, spec, sets)
    assert [(p["payload"], p["stage"]) for p in problems] == [("no data", "run"), ("blank fields", "result")]  # a crash, then an empty result
    assert problems[0]["line"] == 2 and "KeyError" in problems[0]["message"]
    problems, _ = check_version("def run_agent(p):\n    return {'other': 1}\n", spec, sets)
    assert len(problems) == 5 and {p["stage"] for p in problems} == {"result"} and "no \"" in problems[0]["message"]  # capped at five


def test_a_result_that_cannot_be_sent_as_json_is_a_problem() -> None:
    spec, sets = spec_and_sets()
    problems, _ = check_version(f"def run_agent(p):\n    return {{'{spec.output_key}': 'text', 'bad': {{1, 2}}}}\n", spec, sets[:1])
    assert problems[0]["message"] == "The result cannot be sent as JSON"
    assert result_problem({"r": "ok"}, "r") == "" and result_problem({"r": "  "}, "r").startswith("The result has no")


def test_an_endless_loop_is_stopped_and_reported(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(verify, "LIMIT_S", 0.2)
    spec, sets = spec_and_sets()
    problems, _ = check_version("def run_agent(p):\n    while True:\n        pass\n", spec, sets[:1])
    assert "time limit" in problems[0]["message"]


def test_missing_example_data_is_only_a_warning() -> None:
    spec = load_spec(ROLE, AGENT)
    code = render(spec, "rules")
    sets = payload_sets(spec, [{"key": "reach", "kind": "number", "example": ""}])
    problems, warnings = check_version(code, spec, sets)
    assert problems == [] and warnings and warnings[0].startswith("No example data for:")


def test_bad_ids_raise_like_the_rest_of_the_api() -> None:
    with pytest.raises(ValueError):
        verify_agent("Bad_Role", AGENT)
    with pytest.raises(LookupError):
        verify_agent(ROLE, "no-such-agent")
