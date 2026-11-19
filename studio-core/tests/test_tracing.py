"""Tests for the step trace: redaction, the in-memory store, the JSONL log and run contexts."""

import json
from pathlib import Path

import pytest

from valkyrie import tracing
from valkyrie.tracing import STORE, Tracer, redact, step, traced_run


@pytest.fixture(autouse=True)
def _empty_store() -> None:
    STORE.clear()


def test_redact_hides_key_values_key_parameters_and_bearer_tokens(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GEMINI_API_KEY", "AIza-secret-123")
    monkeypatch.setenv("OPENCODE_API_KEY", "")  # an empty value must not blank out every string
    text = "call https://x.test/v1?key=abc123&b=1 with Bearer sk-zzz and AIza-secret-123 and x-goog-api-key: hunter2"
    out = redact(text)
    for leaked in ("abc123", "sk-zzz", "AIza-secret-123", "hunter2"):
        assert leaked not in out
    assert "b=1" in out and out.count("***") == 4
    assert redact({"a": ["Bearer tok", 3, None, True], 5: 1.5}) == {"a": ["Bearer ***", 3, None, True], "5": 1.5}
    assert redact(("x", "y")) == ["x", "y"] and redact(object).startswith("<class")


def test_long_text_is_cut_and_says_how_long_it_was() -> None:
    out = redact("a" * (tracing.MAX_TEXT + 50))
    assert len(out) < tracing.MAX_TEXT + 40 and out.endswith(f"({tracing.MAX_TEXT + 50} characters)")


def test_store_keeps_order_filters_by_run_and_clears() -> None:
    first = Tracer("agent-a", run="r1").step("s1", "one")
    Tracer("agent-b", run="r2").step("s2", "two", "warn", n=2)
    assert [e["id"] for e in STORE.since()] == [first["id"], first["id"] + 1]
    assert [e["stage"] for e in STORE.since(first["id"])] == ["s2"]
    assert [e["stage"] for e in STORE.since(0, "r1")] == ["s1"]
    event = STORE.since(0, "r2")[0]
    assert event["status"] == "warn" and event["detail"] == {"n": 2} and event["agent"] == "agent-b" and event["at"].endswith("+00:00")
    assert STORE.clear() == 2 and STORE.since() == []


def test_a_run_groups_its_steps_and_steps_outside_a_run_go_to_system() -> None:
    with traced_run("my agent") as run:
        first = step("a", "first")
        second = step("b", "second")
    assert first["run"] == second["run"] == run.run and run.agent == "my agent"
    assert 0 <= first["ms"] <= second["ms"]
    outside = step("c", "no run here")
    assert outside["run"] == "system" and outside["agent"] == "system"
    assert len({run.run, Tracer("x").run}) == 2


def test_every_step_is_appended_to_the_log_file_without_secrets(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-very-secret")
    step("provider.attempt", "calling with sk-or-very-secret", token="Bearer sk-or-very-secret")
    step("done", "ok")
    lines = (tmp_path / "logs" / "trace.jsonl").read_text().splitlines()
    assert [json.loads(l)["stage"] for l in lines] == ["provider.attempt", "done"]
    assert "very-secret" not in "".join(lines)


def test_the_log_rotates_when_it_gets_big(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(tracing, "MAX_LOG_BYTES", 10)
    step("a", "x" * 50)
    step("b", "after rotation")
    assert (tmp_path / "logs" / "trace.jsonl.1").is_file()
    assert [json.loads(l)["stage"] for l in (tmp_path / "logs" / "trace.jsonl").read_text().splitlines()] == ["b"]


def test_an_unwritable_log_never_breaks_a_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture) -> None:
    blocker = tmp_path / "not-a-folder"
    blocker.write_text("x")
    monkeypatch.setenv("VALKYRIE_LOG_DIR", str(blocker))
    with caplog.at_level("WARNING", logger="valkyrie.trace"):
        event = step("still", "works")
    assert event["stage"] == "still" and STORE.since()[-1]["stage"] == "still"
    assert "could not write the trace log" in caplog.text
