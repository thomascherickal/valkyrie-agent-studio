"""100% coverage pytest suite for 17-feature-store-reviewer."""

from agent import run_agent


def test_17_feature_store_reviewer() -> None:
    res = run_agent({"feature_specs": "user_30d_spend computed in SQL for training, recomputed in the service for serving; refreshed nightly"})
    assert res["agent_id"] == "17-feature-store-reviewer"
    assert res["tool_used"] == "review_feature_store"
    assert "review_feature_store" in res["store_review"]
