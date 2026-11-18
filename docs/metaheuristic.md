# Metaheuristic Optimization (`pymoo`)

`MetaheuristicOptimizer` (`studio-core/valkyrie/metaheuristic_optimizer.py`) continuously improves per-agent execution parameters using only local run telemetry stored on the user's machine.

## How It Works
1. **Run Counter:** `record_run(agent_id, latency_ms)` increments the local counter for `agent_id`.
2. **Trigger Cadence:** Runs 1 and 2 return `None`; every **3rd run** (`count % 3 == 0`) triggers optimization.
3. **Genetic Algorithm (`pymoo.algorithms.soo.nonconvex.ga.GA`):**
   - Search variables: `temperature` in `[0.0, 1.0]` and `max_tokens_scale` in `[0.25, 1.0]`.
   - Objective: Minimizes deviation from low-variance deterministic output (`0.15`), balanced token scaling (`0.5`), and observed latency penalty.
   - Output: `OptimizationResult(temperature, max_tokens_scale, loss)`.
