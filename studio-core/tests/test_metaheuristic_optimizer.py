"""Tests for pymoo MetaheuristicOptimizer."""

from valkyrie.metaheuristic_optimizer import MetaheuristicOptimizer


def test_metaheuristic_optimizer_triggers_every_3_runs() -> None:
    opt = MetaheuristicOptimizer()
    assert opt.record_run("prd-architect", 15.0) is None
    assert opt.record_run("prd-architect", 12.0) is None
    res = opt.record_run("prd-architect", 10.0)
    assert res is not None
    assert 0.0 <= res.temperature <= 1.0
    assert 0.25 <= res.max_tokens_scale <= 1.0
    assert res.loss >= 0.0

