"""Tests for automated evaluation gate."""

from valkyrie.eval_gate import evaluate_agent_output
from valkyrie.ir_schema import AgentIR, GuardrailConfig


def _sample_ir() -> AgentIR:
    return AgentIR(
        id="eval-test",
        name="Eval Test",
        role="QA",
        description="Test",
        system_prompt="Test",
        output_schema={"summary": "string"},
        guardrails=GuardrailConfig(
            max_latency_ms=100,
            max_cost_usd=0.01,
            blocked_patterns=["SECRET_LEAK"],
        ),
    )


def test_eval_gate_pass_and_fail() -> None:
    ir = _sample_ir()
    ok = evaluate_agent_output(ir, {"summary": "All good"}, latency_ms=50.0, cost_usd=0.001)
    assert ok.passed is True
    assert ok.reasons == []

    fail = evaluate_agent_output(
        ir,
        {"other": "SECRET_LEAK"},
        latency_ms=250.0,
        cost_usd=0.5,
    )
    assert fail.passed is False
    assert not fail.schema_valid
    assert not fail.latency_ok
    assert not fail.cost_ok
    assert not fail.guardrails_ok
    assert len(fail.reasons) == 4

