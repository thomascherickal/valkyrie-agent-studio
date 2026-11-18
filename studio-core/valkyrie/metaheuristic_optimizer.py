"""Lightweight metaheuristic agent optimizer using pymoo, triggered every 3 runs."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize


@dataclass(frozen=True)
class OptimizationResult:
    """Optimized agent hyperparameters (temperature, max_tokens_scale)."""

    temperature: float
    max_tokens_scale: float
    loss: float


class _AgentTuningProblem(ElementwiseProblem):
    def __init__(self, target_latency_ms: float) -> None:
        super().__init__(n_var=2, n_obj=1, xl=np.array([0.0, 0.25]), xu=np.array([1.0, 1.0]))
        self.target_latency_ms = target_latency_ms

    def _evaluate(self, x: np.ndarray, out: dict[str, object], *args: object, **kwargs: object) -> None:
        temp, scale = float(x[0]), float(x[1])
        # Minimize deviation from ideal low-temperature deterministic behavior and token efficiency
        out["F"] = (temp - 0.15) ** 2 + (scale - 0.5) ** 2 + (self.target_latency_ms / 10000.0)


class MetaheuristicOptimizer:
    """Tracks local run counts per agent and optimizes parameters every 3 runs."""

    def __init__(self) -> None:
        self.run_counts: dict[str, int] = {}

    def record_run(self, agent_id: str, latency_ms: float) -> OptimizationResult | None:
        """Record a run; every 3rd run, execute pymoo GA optimization."""
        count = self.run_counts.get(agent_id, 0) + 1
        self.run_counts[agent_id] = count
        if count % 3 != 0:
            return None

        problem = _AgentTuningProblem(target_latency_ms=latency_ms)
        algorithm = GA(pop_size=10)
        res = minimize(problem, algorithm, ("n_gen", 5), seed=42, verbose=False)
        best_x = res.X
        return OptimizationResult(
            temperature=round(float(best_x[0]), 4),
            max_tokens_scale=round(float(best_x[1]), 4),
            loss=round(float(res.F[0]), 6),
        )

