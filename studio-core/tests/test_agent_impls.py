"""Tests for the three built-in Python implementations of every agent, their playbooks and explanations."""

import json
from pathlib import Path
import re

import pytest

from valkyrie.agent_impls import (
    VARIANTS, agent_dir, derive_facets, derive_playbook, facets_for, load_spec, parse_playbook,
    parse_profile, playbook_for, render,
)
from valkyrie.impl_common import COMMON
from valkyrie.profiles import PROFILES
from valkyrie.playbooks import PLAYBOOKS
from valkyrie.python_runner import FORBIDDEN_TOKENS, run_custom_python

AGENTS = Path(__file__).resolve().parents[2] / "agents"
KEYS = sorted(f"{p.parent.parent.name}/{p.parent.name}" for p in AGENTS.glob("*/*/agent.ir.yaml"))
KINDS = {"text", "longtext", "number", "list"}


def payload_for(key: str) -> dict:
    """The agent's own sample input plus the worked example of each of its data fields."""
    role_id, agent_id = key.split("/")
    spec = load_spec(role_id, agent_id)
    data = {spec.input_key: spec.sample}
    data.update({f["key"]: f["example"] for f in playbook_for(spec)["fields"]})
    return data


def test_every_agent_has_an_authored_profile() -> None:
    assert len(KEYS) == 240 and sorted(PROFILES) == KEYS
    for key, text in PROFILES.items():
        facets = parse_profile(text)
        assert 3 <= len(facets) <= 4, key
        assert not any(t in w for ws in facets.values() for w in ws for t in FORBIDDEN_TOKENS), (key, "trips the sandbox")


def test_every_agent_has_a_well_formed_playbook() -> None:
    assert sorted(PLAYBOOKS) == KEYS
    for key in KEYS:
        spec = load_spec(*key.split("/"))
        book = playbook_for(spec)
        fields = book["fields"]
        names = {f["key"] for f in fields}
        assert 3 <= len(fields) <= 6 and len(names) == len(fields) and "input" not in names, key
        for f in fields:
            assert f["kind"] in KINDS and f["label"] and f["example"].strip(), (key, f)
            assert re.fullmatch(r"[a-z][a-z0-9_]*", f["key"]), (key, f["key"])
            if f["kind"] == "number":
                float(f["example"])
        assert 4 <= len(book["sections"]) <= 7, key
        for section in book["sections"]:
            assert 2 <= len(section) <= 6 and all(isinstance(s, str) and s for s in section), (key, section[0])
            for line in section[1:]:
                assert set(re.findall(r"\{(\w+)\}", line)) <= names | {"input"}, (key, line)
                assert not any(t in line for t in FORBIDDEN_TOKENS), (key, line)
        numbers = {f["key"] for f in fields if f["kind"] == "number"}
        for m in book["metrics"]:
            names_used = set(re.findall(r"[a-z_][a-z0-9_]*", re.sub(r"\b(?:min|max)\b(?=\s*\()", "", m["formula"])))
            assert names_used <= numbers, (key, m)
            assert m["format"].count("{}") + m["format"].count("{:") == 1, (key, m)


def test_all_720_implementations_finish_the_job_with_only_their_example_data() -> None:
    for key in KEYS:
        role_id, agent_id = key.split("/")
        spec = load_spec(role_id, agent_id)
        data = payload_for(key)
        book = playbook_for(spec)
        for variant in VARIANTS:
            res = run_custom_python(render(spec, variant), data)
            assert res.ok, f"{key} {variant}: {res.error}"
            out = res.output
            report = out[spec.output_key]
            assert out["implementation"] == variant and out["agent_id"] == agent_id and out["tool_used"] == spec.tool
            assert report.startswith("# " + spec.name)
            assert all(f"## {s[0]}\n- " in report for s in book["sections"]), (key, variant, "a section is missing")
            assert "Add the data this section needs" not in report, (key, variant, "a section came out empty")
            assert out["missing"] == [] and out["completeness"] == 1.0 and "Data still needed" not in report, (key, variant)
            assert len(out["metrics"]) == len(book["metrics"]), (key, variant, "a formula could not be calculated")
            assert all(v in report for v in out["metrics"].values()) and 0 < out["confidence"] <= 1


def test_the_three_implementations_really_differ() -> None:
    key = "01-product-management/01-prd-architect"
    spec = load_spec(*key.split("/"))
    sources = {v: render(spec, v) for v in VARIANTS}
    assert len(set(sources.values())) == 3
    out = {v: run_custom_python(src, payload_for(key)).output for v, src in sources.items()}
    assert "stages" not in out["rules"] and "prompt" not in out["rules"]
    assert [s["stage"] for s in out["pipeline"]["stages"]] == ["validate", "calculate", "draft", "coverage", "review", "compose"]
    assert set(out["pipeline"]["coverage"]) == set(facets_for(spec))
    assert "## Input coverage" in out["pipeline"][spec.output_key] and "## Input coverage" not in out["rules"][spec.output_key]
    assert out["hybrid"]["model_used"] is False and spec.name in out["hybrid"]["prompt"] and out["hybrid"]["review"] == []
    assert "Target users" in out["hybrid"]["prompt"] and payload_for(key)["target_users"] in out["hybrid"]["prompt"]


def test_formulas_calculate_and_a_bad_number_or_division_by_zero_never_breaks_the_report() -> None:
    key = "01-product-management/02-roadmap-prioritizer"
    spec = load_spec(*key.split("/"))
    source = render(spec, "rules")
    ok = run_custom_python(source, payload_for(key)).output
    assert ok["metrics"]["RICE score"] == "3,000.0"  # 5000 reach x 3 impact x 0.8 confidence / 4 effort
    zero = run_custom_python(source, {**payload_for(key), "effort": "0"}).output
    assert zero["metrics"] == {}  # both formulas divide by effort, so both are skipped instead of crashing
    bad = run_custom_python(source, {**payload_for(key), "reach": "lots"}).output
    assert bad["completeness"] < 1.0 and "Fix the number in: Reach (users per quarter)" in bad[spec.output_key]
    assert run_custom_python(source, {**payload_for(key), "reach": "45%"}).output["metrics"]["RICE score"] != ok["metrics"]["RICE score"]


def test_missing_data_is_listed_and_the_lines_that_need_it_are_left_out() -> None:
    key = "01-product-management/01-prd-architect"
    spec = load_spec(*key.split("/"))
    data = payload_for(key)
    full = run_custom_python(render(spec, "rules"), data).output
    data["success_metric"] = ""
    gap = run_custom_python(render(spec, "rules"), data).output
    assert gap["missing"] == ["Success metric"] and gap["completeness"] < full["completeness"]
    assert "Provide: Success metric" in gap[spec.output_key] and "Primary goal" not in gap[spec.output_key]
    assert "Primary goal" in full[spec.output_key] and "Data still needed" not in full[spec.output_key]


def test_list_fields_expand_to_one_bullet_per_item_and_formulas_support_min_max_and_precedence() -> None:
    spec = load_spec("01-product-management", "01-prd-architect")
    source = render(spec, "rules")
    data = payload_for("01-product-management/01-prd-architect")
    data["constraints"] = "Must support SAML 2.0; no new database\nWorks offline, p95 under 2 s"
    report = run_custom_python(source, data).output[spec.output_key]
    for item in ("- Must support SAML 2.0", "- no new database", "- Works offline", "- p95 under 2 s"):
        assert item in report

    harness = COMMON.replace("__SPEC__", json.dumps({"fields": [], "sections": [], "metrics": []})) + (
        "\ndef run_agent(p):\n    return {'v': calc(p['f'], p['n'])}\n")
    numbers = {"a": 4.0, "b": 7.0}
    for formula, expected in [("2 + 3 * 4", 14.0), ("(2 + 3) * 4", 20.0), ("-a + b / 2", -0.5), ("min(a, b) + max(a, 10)", 14.0),
                              ("a * (b - 1) / 2", 12.0), ("max(a, b, 1) - min(1, a)", 6.0)]:
        res = run_custom_python(harness, {"f": formula, "n": numbers})
        assert res.ok and res.output["v"] == expected, (formula, res.error, res.output)
    assert run_custom_python(harness, {"f": "1 / 0", "n": {}}).error.startswith("ZeroDivisionError")
    assert "Unexpected" in run_custom_python(harness, {"f": "1 2", "n": {}}).error


def test_hybrid_review_catches_an_answer_that_drops_a_section_or_changes_a_figure() -> None:
    key = "01-product-management/02-roadmap-prioritizer"
    spec = load_spec(*key.split("/"))
    base = render(spec, "hybrid")
    draft = run_custom_python(base, payload_for(key)).output[spec.output_key]
    out = run_custom_python(base, payload_for(key), model=lambda prompt: draft).output
    assert out["model_used"] is True and out["review"] == [] and out["confidence"] > 0.9

    changed = draft.replace("3,000.0", "9,999.0").replace("## Tiering", "## Other")
    bad = run_custom_python(base, payload_for(key), model=lambda prompt: changed).output
    assert "The answer dropped the section: Tiering" in bad["review"]
    assert any(p.startswith("The answer changed or dropped RICE score") for p in bad["review"])


def test_pipeline_review_flags_thin_sections_and_topics_the_input_never_mentions() -> None:
    spec = load_spec("01-product-management", "01-prd-architect")
    out = run_custom_python(render(spec, "pipeline"), {spec.input_key: "hello", "target_users": ""}).output
    assert any("only" in n and "line(s)" in n for n in out["review"])
    assert any(n.startswith("Your input does not mention:") for n in out["review"])
    assert out["missing"] and out["completeness"] < 1.0


def test_agents_without_a_playbook_get_a_general_one_and_lookups_fail_cleanly() -> None:
    spec = load_spec("01-product-management", "01-prd-architect")
    custom = spec.__class__(**{**spec.__dict__, "role_id": "custom-agents", "agent_id": "made-up"})
    facets = derive_facets(custom)
    assert list(facets) == ["main points", "risks", "next actions"] and "feature" in facets["main points"]
    assert facets_for(custom) == facets
    book = derive_playbook(custom)
    assert [f["key"] for f in book["fields"]] == ["context", "owner", "deadline"] and playbook_for(custom) == book
    out = run_custom_python(render(custom, "rules"), {custom.input_key: "Ship it", "context": "Team A, Q3", "owner": "Sam"}).output
    assert out["missing"] == ["Deadline"] and "- Team A" in out[custom.output_key] and "Owner: Sam" in out[custom.output_key]

    assert parse_playbook({"fields": ["a|A|text|x"], "sections": [["T", "l"]]})["metrics"] == []
    with pytest.raises(ValueError):
        agent_dir("Bad_Role", "x")
    with pytest.raises(LookupError):
        agent_dir("01-product-management", "no-such-agent")
