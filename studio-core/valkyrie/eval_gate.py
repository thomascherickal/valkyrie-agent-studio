"""Automated evaluation gate verifying accuracy, schema, latency, and cost."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from valkyrie.ir_schema import AgentIR


@dataclass(frozen=True)
class EvalReport:
    """Outcome of running the automated evaluation gate."""

    passed: bool
    schema_valid: bool
    latency_ok: bool
    cost_ok: bool
    guardrails_ok: bool
    reasons: list[str]


def evaluate_agent_output(
    ir: AgentIR,
    output: dict[str, Any],
    latency_ms: float,
    cost_usd: float,
) -> EvalReport:
    """Verify agent output against IR schema, guardrails, latency, and cost budgets."""
    reasons: list[str] = []

    missing_keys = [k for k in ir.output_schema if k not in output]
    schema_valid = len(missing_keys) == 0
    if not schema_valid:
        reasons.append(f"Missing output keys: {', '.join(missing_keys)}")

    latency_ok = latency_ms <= ir.guardrails.max_latency_ms
    if not latency_ok:
        reasons.append(f"Latency {latency_ms}ms exceeds max {ir.guardrails.max_latency_ms}ms")

    cost_ok = cost_usd <= ir.guardrails.max_cost_usd
    if not cost_ok:
        reasons.append(f"Cost ${cost_usd:.6f} exceeds max ${ir.guardrails.max_cost_usd:.6f}")

    serialized = str(output)
    blocked = [p for p in ir.guardrails.blocked_patterns if p in serialized]
    guardrails_ok = len(blocked) == 0
    if not guardrails_ok:
        reasons.append(f"Blocked patterns detected: {', '.join(blocked)}")

    passed = schema_valid and latency_ok and cost_ok and guardrails_ok
    return EvalReport(
        passed=passed,
        schema_valid=schema_valid,
        latency_ok=latency_ok,
        cost_ok=cost_ok,
        guardrails_ok=guardrails_ok,
        reasons=reasons,
    )

